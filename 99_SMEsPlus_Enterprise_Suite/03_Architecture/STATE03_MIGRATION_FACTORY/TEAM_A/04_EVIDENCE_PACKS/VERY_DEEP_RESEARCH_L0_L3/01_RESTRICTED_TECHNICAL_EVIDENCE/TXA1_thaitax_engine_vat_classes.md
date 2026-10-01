# TXA1 - thaitax_engine_vat_classes - Restricted Technical Evidence

> **RESTRICTED - TECHNICAL EVIDENCE - NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Unit: TXA1 `thaitax_engine_vat_classes` (Thai Tax Core lane, Odoo-behaviour sub-lane) - Source revision `19.0.post20260921` (Odoo 19 Community only) - Date: 2026-10-02
> Modules read (installed in the restored dump): `account`, `l10n_th`, `product`, `base` (currency), `sale`, `purchase`, `stock_account`, `purchase_stock`, `sale_loyalty`, `delivery`, `hr_expense`, `account_edi_ubl_cii` (tax parts), plus override scan of all 356 installed modules; not-installed Community add-ons read only for the override map (`account_tax_python`, `l10n_account_withholding_tax`, `base_vat`, `account_update_tax_tags`, `account_debit_note`).
> Topics covered: (1) generic tax engine and calculation, (2) sales and purchase VAT, (3) standard-rated, zero-rated, exempt, non-deductible treatment, (6) price-included and excluded, rounding, currency conversion, (8) company, partner, product and fiscal configuration. Cross-topic hand-offs (4, 5, 9) are touched only where the engine is involved.
> Read-only on source; DB queried only for configuration (counts, flags, seeded configuration). No Odoo started, no L5/AWT claims; items needing execution are flagged `RT`. Nothing from `Extra_Thailand`, `Extra_Module_scgl`, Enterprise or proprietary code was opened.
> SEPARATION: this file states what Community source and the restored dump DO. It asserts no Thai statutory requirement; every Thai treatment is tagged `STATUTORY CHECK PENDING (TXS)`. Community absence is not proof that a business requirement does not exist. No V-level, Complete, coverage percentage or Gate PASS is asserted.
> Claim IDs `VDR-TXA1-C###`; neutral IDs `N-TXA1-###` (see `02_NEUTRAL_KNOWLEDGE/TXA1_thaitax_engine_vat_classes_NEUTRAL.md`). Claim references in the prose below are claim IDs resolved at generation time; every statement is backed by a row in the Claims table.

## 0. Scope, method and Function-ID mapping

| Capability | Function-ID | Note |
|---|---|---|
| CAP-TXA1-01 Generic tax calculation engine (types, ordering, base chains, price-included extraction) | FUNCTION MAPPING REQUIRED | no index entry for tax computation |
| CAP-TXA1-02 Rounding methods, totals summary, discounts and cash rounding | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-TXA1-03 Distribution lines, tax grid tags, accounts and tax journal items | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-TXA1-04 Sales VAT and purchase VAT on documents (default tax resolution and flows) | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-TXA1-05 Thai tax treatments represented in the Thai template and their document presentation | FUNCTION MAPPING REQUIRED | no index entry for tax treatments |
| CAP-TXA1-06 Non-deductible tax handling and tax on stock and cost flows | GRV-F04 on the receipt-valuation-price claim only; otherwise FUNCTION MAPPING REQUIRED | GRV-F04 is 'Inventory valuation at receipt'; matches only the stock-move price claim |
| CAP-TXA1-07 Price-included / price-excluded, currency conversion, multi-currency tax amounts | FUNCTION MAPPING REQUIRED | base currency model hand-off to U01/U25 |
| CAP-TXA1-08 Company, partner, product and fiscal-position configuration that drives tax behaviour | FUNCTION MAPPING REQUIRED | MCT-F03 (shared vs per-company chart) judged not to match tax-scope claims |
| CAP-TXA1-09 Tax record lifecycle, template loading, security and locks (tax scope) | PCO-F01 on lock-date claims; otherwise FUNCTION MAPPING REQUIRED | PCO-F01 is 'Lock Dates (... Tax ...)' |

Method: full read of `account/models/account_tax.py` (engine, rounding, aggregation, totals, tax-line generation, `compute_all`, repartition line), tax-related methods of `account_move.py` (base-line producers, `_sync_tax_lines`, non-deductible sync, fiscal position, currency rate, tax country, lock hooks), `account_move_line.py` (tax fields, default tax resolution, deductibility), `partner.py` (fiscal position finder, mapping, VAT stub), `product.py`, `company.py` and settings, `res_currency` (base and account), `account_cash_rounding.py`, chart-template tax loading, `l10n_th` (all model files, tax and tax-group CSV, template functions, invoice view); tax parts of `sale`, `purchase`, `purchase_stock`, `stock_account`, `sale_loyalty`, `delivery`, `hr_expense`, `account_edi_ubl_cii`. An override scan (method-name and inheritance grep, restricted to the 356 installed modules in `universe.json` key `dump`) produced the Source and Override Map. Prior evidence U13, U23, U24, U25 was read and re-verified for every statement relied on; no claim here is copied without a re-read of the cited line.

Thai-tax execution path traced: product/company/partner configuration -> default tax and fiscal position -> base-line description -> calculation -> rounding -> distribution lines, tags, accounts -> tax journal items -> totals -> printed document / EDI; cross-module triggers in sale, purchase, stock valuation, expense, delivery, loyalty.

---

## CAP-TXA1-01 Generic tax calculation engine (types, ordering, base chains, price-included extraction)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no index entry for tax computation; see U13 section 0).

### D1 Business purpose and process semantics
Turn the taxes attached to any document line into a base amount, per-tax amounts and line totals, in document and company currency, so that sales orders, purchase orders, customer invoices, vendor bills and expense claims show the same figures for the same inputs. VDR-TXA1-C001 VDR-TXA1-C028 VDR-TXA1-C039 For a Thai legal entity this is the only calculation path for 7% VAT, 0% and exempt records and negative-percentage withholding records (the Thai template adds no calculation code, VDR-TXA1-C189).

### D2 Architecture, data, objects
- Tax record: type VDR-TXA1-C001, usage scope VDR-TXA1-C002, goods/services scope VDR-TXA1-C003, sequence VDR-TXA1-C004, include-in-base flags VDR-TXA1-C005 VDR-TXA1-C006, price-include override VDR-TXA1-C007, label VDR-TXA1-C017.
- Generic base-line dictionary prepared from any record VDR-TXA1-C039 (special mode VDR-TXA1-C041, special type VDR-TXA1-C040); tax-line dictionary VDR-TXA1-C045; evaluation context VDR-TXA1-C036 VDR-TXA1-C019.
- Record-side producers of base lines: sales order line VDR-TXA1-C222, purchase order line VDR-TXA1-C231, journal item VDR-TXA1-C105, expense VDR-TXA1-C244; consumers: totals, tax lines, EDI (CAP-TXA1-05).
- Client-side mirror VDR-TXA1-C038 VDR-TXA1-C268.
- Legacy API `compute_all` VDR-TXA1-C085.

### D3 Source/technical/workflow logic
1. Flatten groups, sort by sequence, id VDR-TXA1-C020; filter group children rules VDR-TXA1-C015.
2. Batch taxes VDR-TXA1-C021; propagate extra base VDR-TXA1-C022.
3. Raw base = quantity x unit price (after discount VDR-TXA1-C047) VDR-TXA1-C032.
4. Passes: fixed VDR-TXA1-C023, price-included VDR-TXA1-C024 VDR-TXA1-C025, price-excluded VDR-TXA1-C026 VDR-TXA1-C027; order VDR-TXA1-C033.
5. Base of an included tax VDR-TXA1-C034; negative-factor mirrored entry VDR-TXA1-C030 VDR-TXA1-C031.
6. Totals VDR-TXA1-C035; hand-off to rounding (CAP-TXA1-02) via VDR-TXA1-C046.
Hook for products/units VDR-TXA1-C019. Formula-type taxes are not part of the installed set VDR-TXA1-C317; the discount helper still names the type VDR-TXA1-C084.

State list (tax calculation pipeline, per line):
- `record -> base line [prepare] (VDR-TXA1-C039)`
- `base line -> raw tax details [calculate] (VDR-TXA1-C046)`
- `raw tax details -> rounded details [round] (CAP-TXA1-02)`
- `rounded details -> tax items [repartition and sync] (CAP-TXA1-03)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Line with taxes -> base line -> details -> totals (VDR-TXA1-C039, VDR-TXA1-C046, VDR-TXA1-C035). |
| 2 | Reversal/cancel/negative path | Negative-factor taxes mirror (VDR-TXA1-C030); fixed tax keeps the sign of the unit price (VDR-TXA1-C023); credit-note side handled in CAP-TXA1-03. |
| 3 | Multi-company / data scope | Compute_all picks the first accessible branch company (VDR-TXA1-C090); company filtering in VDR-TXA1-C091. |
| 4 | Side effects and cross-module | Product and unit values via hook (VDR-TXA1-C019); expense extension (VDR-TXA1-C303); client mirror (VDR-TXA1-C038). |
| 5 | Configuration and optionality | Type, scope, sequence, include-in-base, price override per tax; formula type optional add-on not installed (VDR-TXA1-C317). |
| 6 | Validation and constraints | Group children rules (VDR-TXA1-C015); tax name uniqueness (VDR-TXA1-C010). |
| 7 | Roles and permissions | Read for all internal users; edit by accounting administrator (VDR-TXA1-C271). |
| 8 | Scheduled/automated | NOT APPLICABLE - synchronous calculation; no cron or automation row concerns taxes (DB 0 tax crons, 0 automations). |
| 9 | Exception and failure | No exception path in the pure routine; rate 0 gives zero company-currency amounts (VDR-TXA1-C050); numeric unknowns in Unknown list. |
| 10 | Accounting, audit, compliance | Same figures feed journal items, totals and EDI; statutory conformity of any figure is STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
18 taxes all percentage, sequence 1, no include-in-base, no analytic flag, base-affected true (VDR-TXA1-C275); no formula, fixed or division taxes exist; company global rounding and tax-excluded (VDR-TXA1-C276).

### Unknown / Runtime
- RT: numeric results for combinations (7% VAT plus withholding on one line, rounding deltas): never executed (compare U13 C088). VDR-TXA1-C033 VDR-TXA1-C022
- UNKNOWN: effect of equal sequences (all Thai taxes have sequence 1; tie broken by id) on any future include-in-base configuration.

---

## CAP-TXA1-02 Rounding methods, totals summary, discounts and cash rounding

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Make the tax and total shown on a document equal a total computed on the whole document, regardless of line count, by choosing per-line or global rounding, distributing rounding differences, supporting manual tax amounts, and presenting totals per tax group in both currencies. VDR-TXA1-C057 VDR-TXA1-C071 Also covers discounts, down payments, early-payment discounts and cash rounding, which all change the tax base.

### D2 Architecture, data, objects
- Company rounding setting VDR-TXA1-C169; settings screen VDR-TXA1-C181.
- Rounding helpers: delta distribution VDR-TXA1-C052, tax amounts VDR-TXA1-C053, base amounts VDR-TXA1-C054 VDR-TXA1-C055, tax-line re-alignment VDR-TXA1-C056, manual amounts VDR-TXA1-C058 VDR-TXA1-C043 VDR-TXA1-C044.
- Totals summary VDR-TXA1-C071 with group order VDR-TXA1-C072, display base VDR-TXA1-C073, same-base flag VDR-TXA1-C074.
- Discount, down payment helpers VDR-TXA1-C099 VDR-TXA1-C100 VDR-TXA1-C101 VDR-TXA1-C102; wizards VDR-TXA1-C226 VDR-TXA1-C227 VDR-TXA1-C228.
- Early-payment discount VDR-TXA1-C107 VDR-TXA1-C217 VDR-TXA1-C144; cash rounding VDR-TXA1-C211 VDR-TXA1-C212 VDR-TXA1-C075 VDR-TXA1-C108.

### D3 Source/technical/workflow logic
1. Round per line: tax amounts and raw base rounded while computing VDR-TXA1-C029 VDR-TXA1-C051.
2. Round globally: raw rounding in each currency VDR-TXA1-C059; manual amounts applied VDR-TXA1-C058; then document-level tax and base alignment VDR-TXA1-C053 VDR-TXA1-C055.
3. Method defaults to the company setting VDR-TXA1-C048 VDR-TXA1-C169.
4. Delta distribution VDR-TXA1-C052.
5. Totals per tax group; cash rounding by add-a-line or change-largest-tax VDR-TXA1-C075; non-deductible subtraction (CAP-TXA1-06) VDR-TXA1-C076.
6. Manual edits: totals widget rewrite VDR-TXA1-C127; sync decides keep or recompute VDR-TXA1-C114 VDR-TXA1-C116 VDR-TXA1-C110.

State list:
- `draft document, lines edited -> tax items re-synchronised [sync] (VDR-TXA1-C114)`
- `manual tax amount -> kept [only taxes-unaffecting changes] (VDR-TXA1-C114)`
- `currency changed or switched to credit note -> manual amounts discarded (VDR-TXA1-C116)`
- `rate changed only -> foreign amounts kept, company balances re-derived (VDR-TXA1-C115)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Two lines with the same tax: line taxes rounded, document tax rounded once, delta spread (VDR-TXA1-C053, VDR-TXA1-C052). |
| 2 | Reversal/cancel/negative path | Credit-note flag switches sign and distribution side; manual amounts discarded on type switch (VDR-TXA1-C116); returns netted (VDR-TXA1-C102). |
| 3 | Multi-company / data scope | Rounding setting is per company (VDR-TXA1-C169); cash-basis and fiscal-year fields delegated to root (VDR-TXA1-C176). |
| 4 | Side effects and cross-module | Sales and purchase orders and expenses reuse the same rounding (VDR-TXA1-C216, VDR-TXA1-C232, VDR-TXA1-C243); loyalty reuses aggregation (VDR-TXA1-C306). |
| 5 | Configuration and optionality | Rounding method; early-payment mode VDR-TXA1-C144; cash rounding strategy VDR-TXA1-C211. |
| 6 | Validation and constraints | Cash rounding precision > 0 VDR-TXA1-C212; currency precision cannot shrink VDR-TXA1-C210. |
| 7 | Roles and permissions | Cash rounding editable by invoicing role VDR-TXA1-C274. |
| 8 | Scheduled/automated | NOT APPLICABLE - no cron; early-payment discount entries are created at payment (U12). |
| 9 | Exception and failure | Biggest-tax cash rounding does nothing without a tax VDR-TXA1-C075; rate 0 gives zero company amounts VDR-TXA1-C050. |
| 10 | Accounting, audit, compliance | Rounded amounts equal posted journal items; raw amounts kept for e-invoicing precision VDR-TXA1-C057; Thai statutory rounding rule STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
Company: round_globally (VDR-TXA1-C276); 0 cash rounding rules (VDR-TXA1-C277); 10 payment terms all early-payment mode "included" (reduce tax on early payment), one with early discount (VDR-TXA1-C280); THB precision 0.01 (VDR-TXA1-C278).

### Unknown / Runtime
- RT: totals and per-line figures for multi-line documents (THB, 2 decimals) with VAT plus withholding under global rounding; client preview versus server equality (VDR-TXA1-C038).
- UNKNOWN: Thai statutory rounding convention (satang) for tax amounts - pending TXS.

---

## CAP-TXA1-03 Distribution lines, tax grid tags, accounts and tax journal items

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Convert calculated tax amounts into journal items on the right accounts with the right tax-report tags, for invoices and credit notes, merging equal items, dropping zero items and keeping draft documents in sync with their lines. VDR-TXA1-C094 VDR-TXA1-C062 VDR-TXA1-C063

### D2 Architecture, data, objects
- Distribution line VDR-TXA1-C094, account domain VDR-TXA1-C098, tag domain VDR-TXA1-C097, closing flag VDR-TXA1-C095, target account for cash-basis VDR-TXA1-C096.
- Tax group VDR-TXA1-C013; journal item fields VDR-TXA1-C133 VDR-TXA1-C132.
- Grouping keys VDR-TXA1-C060 VDR-TXA1-C061; tags VDR-TXA1-C065 VDR-TXA1-C066 VDR-TXA1-C069 VDR-TXA1-C070.

### D3 Source/technical/workflow logic
1. Select side by refund flag VDR-TXA1-C064; refund flag of a line VDR-TXA1-C262.
2. Amount per distribution line = tax amount x factor, rounded per currency, residual spread VDR-TXA1-C068.
3. Negative-factor lines used for the mirrored entry VDR-TXA1-C067.
4. Account: distribution account, else base account VDR-TXA1-C062.
5. Tags VDR-TXA1-C063; closing flag effect on analytic VDR-TXA1-C061 VDR-TXA1-C323.
6. Aggregate and update VDR-TXA1-C081 VDR-TXA1-C082; zero items dropped VDR-TXA1-C079; base items updated VDR-TXA1-C080; name VDR-TXA1-C083.
7. Validation of the structure VDR-TXA1-C014.
8. Cash-basis variants VDR-TXA1-C009 VDR-TXA1-C264 VDR-TXA1-C117 VDR-TXA1-C295.

State list:
- `tax created -> default base and tax distribution lines [create] (CAP-TXA1-09)`
- `draft document -> tax items created or updated or removed [sync] (VDR-TXA1-C114)`
- `on_invoice tax -> items with tags at posting (VDR-TXA1-C070)`
- `on_payment tax -> transition account until reconciliation (VDR-TXA1-C096, VDR-TXA1-C264)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | 7% sale: base item with tag, tax item on output VAT with tag (VDR-TXA1-C191, VDR-TXA1-C063). |
| 2 | Reversal/cancel/negative path | Credit note uses the refund side (VDR-TXA1-C064); structure must mirror (VDR-TXA1-C014); reverse-charge pair (VDR-TXA1-C067). |
| 3 | Multi-company / data scope | Distribution lines follow the tax company; rule allows records without company (VDR-TXA1-C272). |
| 4 | Side effects and cross-module | Tags feed tax reports (VDR-TXA1-C265); analytic copy (VDR-TXA1-C061); product tags (VDR-TXA1-C065). |
| 5 | Configuration and optionality | Per-tax distribution; closing flag; tags limited by country (VDR-TXA1-C097). |
| 6 | Validation and constraints | One base line per side, same count, mirrored, factor totals (VDR-TXA1-C014); account domain (VDR-TXA1-C098). |
| 7 | Roles and permissions | Edit by accounting administrator only (VDR-TXA1-C271). |
| 8 | Scheduled/automated | NOT APPLICABLE - no cron. |
| 9 | Exception and failure | Distribution error aborts export with the tax name (VDR-TXA1-C298). |
| 10 | Accounting, audit, compliance | Tax items identify originator tax and group (VDR-TXA1-C133); closing flag is stored but no closing routine found (VDR-TXA1-C323); statutory use of tags STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
72 distribution lines (36 invoice, 36 refund), 12 tax lines closing-flagged, 0 tax lines without account (VDR-TXA1-C275); 5 tax groups (VDR-TXA1-C199, VDR-TXA1-C200); 13 Thai tags, 3 unused (VDR-TXA1-C283); company cash-basis switch on with no cash-basis tax (VDR-TXA1-C186).

### Unknown / Runtime
- RT: whether zero-rate sale produces only base items with both tags (source says zero tax item is dropped VDR-TXA1-C079; U24 left this RT).
- RT: effect of the three unused tags on any report formula; closing routine absence confirmed only by grep (VDR-TXA1-C323).

---

## CAP-TXA1-04 Sales VAT and purchase VAT on documents (default tax resolution and document flows)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Decide which taxes land on each line of a sales order, purchase order, customer invoice, vendor bill, delivery charge, reward line and expense, from the product, the ledger account, the company and the partner's fiscal position, and keep them consistent as the document moves from order to invoice. VDR-TXA1-C134 VDR-TXA1-C218 VDR-TXA1-C230

### D2 Architecture, data, objects
- Product tax sets VDR-TXA1-C145 VDR-TXA1-C146 defaulting from company fields VDR-TXA1-C172; product creation propagation VDR-TXA1-C150; combo reset VDR-TXA1-C149.
- Ledger account default taxes VDR-TXA1-C260.
- Document line resolution VDR-TXA1-C135 VDR-TXA1-C136 VDR-TXA1-C137 VDR-TXA1-C138; order lines VDR-TXA1-C218 VDR-TXA1-C220 VDR-TXA1-C230; quick encoding VDR-TXA1-C291 VDR-TXA1-C130.
- Flows: order to invoice VDR-TXA1-C225 VDR-TXA1-C224; delivery VDR-TXA1-C250 VDR-TXA1-C251; loyalty VDR-TXA1-C247 VDR-TXA1-C249 VDR-TXA1-C248; expense VDR-TXA1-C245 VDR-TXA1-C244 VDR-TXA1-C246; project and service resale VDR-TXA1-C312 VDR-TXA1-C311.

### D3 Source/technical/workflow logic
1. Line taxes recompute when product or unit changes VDR-TXA1-C134.
2. Sale vs purchase source of taxes VDR-TXA1-C135 VDR-TXA1-C136; no company default at line level VDR-TXA1-C139.
3. Narrow to company tree VDR-TXA1-C138; map through fiscal position (CAP-TXA1-08).
4. Orders: product taxes only VDR-TXA1-C220 VDR-TXA1-C230; selectable taxes limited by country VDR-TXA1-C219.
5. Invoice from order copies taxes and engine data VDR-TXA1-C225; down payment lines VDR-TXA1-C227 VDR-TXA1-C228.
6. Totals on orders VDR-TXA1-C216 VDR-TXA1-C232; purchase total in company currency VDR-TXA1-C233.

State list:
- `order line created -> taxes defaulted [product, fiscal position] (VDR-TXA1-C218)`
- `order -> invoice [create invoice] -> taxes copied (VDR-TXA1-C225)`
- `fiscal position changed on order with lines -> update-taxes prompt (VDR-TXA1-C213)`
- `down payment invoice posted -> order down payment lines take invoice taxes (VDR-TXA1-C228)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Product with default 7% sale tax on a sales order -> invoice line with same tax (VDR-TXA1-C279, VDR-TXA1-C218, VDR-TXA1-C225). |
| 2 | Reversal/cancel/negative path | Credit note uses refund side (CAP-TXA1-03); expense reversal handled by expense module (U16). |
| 3 | Multi-company / data scope | Taxes narrowed by company tree VDR-TXA1-C138; product default for other companies VDR-TXA1-C150. |
| 4 | Side effects and cross-module | Delivery charge, rewards, expenses, project stock and service-resale lines all reuse the product tax and fiscal position path (VDR-TXA1-C250, VDR-TXA1-C247, VDR-TXA1-C245, VDR-TXA1-C312). |
| 5 | Configuration and optionality | Product tax sets; account default taxes (none in DB); company default taxes VDR-TXA1-C172; fiscal positions (none in DB). |
| 6 | Validation and constraints | Order-line taxes limited to sale-type and tax country VDR-TXA1-C219; off-balance accounts carry no tax VDR-TXA1-C261. |
| 7 | Roles and permissions | Product edit by product roles (U02); tax read for all, edit by administrator VDR-TXA1-C271. |
| 8 | Scheduled/automated | NOT APPLICABLE - no tax cron. |
| 9 | Exception and failure | Purchase line without a vendor tax gets none; combo lines no tax VDR-TXA1-C218; accounts of off-balance excluded. |
| 10 | Accounting, audit, compliance | Taxes on a line are stored and tracked on the journal item (VDR-TXA1-C131); order-only use does not block tax deletion VDR-TXA1-C302; statutory VAT treatment per transaction STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
Company defaults: sale = standard output VAT, purchase = standard input VAT (VDR-TXA1-C276); 16 seeded service products, 14 with sale tax, 16 with purchase tax, none with tags (VDR-TXA1-C279); 0 account default taxes, 0 fiscal positions (VDR-TXA1-C277).

### Unknown / Runtime
- UNKNOWN: partner-level automatic tax selection for Thai customers (no fiscal position seeded); resolve by configuring a position in a test database.
- RT: tax result of a down-payment invoice with price-included prices (VDR-TXA1-C227).

---

## CAP-TXA1-05 Thai tax treatments represented in the Thai template (standard-rated, zero-rated, exempt, withholding) and their document presentation

**Function-ID(s):** FUNCTION MAPPING REQUIRED. Statutory correctness of every treatment below: STATUTORY CHECK PENDING (TXS). Nothing here asserts that a seeded record is legally right.

### D1 Business purpose and process semantics
Show how the Thai localization represents VAT classes and withholding natively, using only generic engine features, so that later work can compare the representation with statutory validation from the statutory unit. VDR-TXA1-C189 VDR-TXA1-C184

### D2 Architecture, data, objects
- Template functions and company defaults VDR-TXA1-C184 VDR-TXA1-C185 VDR-TXA1-C183.
- Tax records: standard VDR-TXA1-C190 VDR-TXA1-C191; zero VDR-TXA1-C192 VDR-TXA1-C193; exempt VDR-TXA1-C194 VDR-TXA1-C195; withholding VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C198.
- Groups VDR-TXA1-C199 VDR-TXA1-C200; accounts VDR-TXA1-C282; tags VDR-TXA1-C283.
- Documents: layout choice VDR-TXA1-C188; notes VDR-TXA1-C284 VDR-TXA1-C290; e-invoicing classification VDR-TXA1-C296 VDR-TXA1-C297 VDR-TXA1-C299.

### D3 Source/technical/workflow logic
- Template load: the Thai chart is selected by company country (U24 CAP-U24-01); company defaults set VDR-TXA1-C185; all taxes recognised at posting (VDR-TXA1-C275).
- Treatment by engine mechanics (see Thai Tax Record Treatment Map register): every record is a percentage tax; zero and exempt differ from standard only by amount 0 and base tags; withholding differs by negative amount, accounts and closing flag.
- Zero tax item is dropped, leaving base items only VDR-TXA1-C079.
- Withholding tax line: amount = negative percent x untaxed base (price-excluded) VDR-TXA1-C026; recognised at posting VDR-TXA1-C009; sale side forced excluded VDR-TXA1-C198; purchase side follows the company default VDR-TXA1-C324.
- No payee-driven selection and no fiscal position shipped VDR-TXA1-C187.
- E-invoicing: zero 0% tax infers category exempt when no code VDR-TXA1-C297 VDR-TXA1-C299.

State list:
- `no Thai chart -> Thai chart loaded [module install on a company located in Thailand] (U24 CAP-U24-01)`
- `Thai invoice posted -> VAT items on 213200 or 114200 with grid tags (VDR-TXA1-C191, VDR-TXA1-C190)`
- `vendor bill posted with withholding tax -> withholding item on 213301 or 213302 (VDR-TXA1-C196, VDR-TXA1-C197)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Sale of 100 at 7%: base item 100 tag sales amount, tax item 7 on output VAT (VDR-TXA1-C191); numeric result RT. |
| 2 | Reversal/cancel/negative path | Refund distribution mirrors invoice distribution for every Thai tax (VDR-TXA1-C191, VDR-TXA1-C014). |
| 3 | Multi-company / data scope | Template loads per company; taxes follow company rule (VDR-TXA1-C272). |
| 4 | Side effects and cross-module | Tags and accounts feed Thai return definitions (U24); e-invoicing infers categories (VDR-TXA1-C297). |
| 5 | Configuration and optionality | Tax selection manual; no position; zero and exempt without group (VDR-TXA1-C200); withholding follows company price setting (VDR-TXA1-C324). |
| 6 | Validation and constraints | Generic constraints only (VDR-TXA1-C014, VDR-TXA1-C010); name "7%" is used for both purchase and sale (unique per usage). |
| 7 | Roles and permissions | Edit by accounting administrator; no Thai ACL or rule (VDR-TXA1-C189). |
| 8 | Scheduled/automated | NOT APPLICABLE - Thai module has no cron (DB 0). |
| 9 | Exception and failure | Zero and exempt classes have no distinct failure mode; classification risk from group fallback (VDR-TXA1-C200). |
| 10 | Accounting, audit, compliance | Statutory correctness of rates, grids, accounts, withholding categories: STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
18 taxes = 18 template taxes (VDR-TXA1-C275); 5 groups; accounts exist as listed (VDR-TXA1-C282); undue VAT and PND 54 accounts referenced by no tax (VDR-TXA1-C282); 13 tags (VDR-TXA1-C283); EDI category code null on all 18 (VDR-TXA1-C299).

### Unknown / Runtime
- UNKNOWN: statutory classification of each record (pending TXS).
- RT: printed Thai invoice layout and tax lines (VDR-TXA1-C188); e-invoice export of zero-rated Thai sales (VDR-TXA1-C297).

---

## CAP-TXA1-06 Non-deductible tax handling and tax on stock and cost flows

**Function-ID(s):** GRV-F04 on claims about receipt valuation price (genuine match: inventory valuation at receipt); otherwise FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Two native mechanisms move part of a tax out of the recoverable tax lines: (a) a per-line deductibility percentage on vendor bills that routes the private share and its taxes to a separate account, and (b) cost capitalisation of taxes whose distribution lines have no account when goods are received. Customer-invoice cost entries never carry tax. VDR-TXA1-C119 VDR-TXA1-C237 VDR-TXA1-C240

### D2 Architecture, data, objects
- Deductibility percentage VDR-TXA1-C123 and its constraint VDR-TXA1-C124; journal private-share account VDR-TXA1-C125; visibility group VDR-TXA1-C273.
- Engine special type VDR-TXA1-C049; base lines VDR-TXA1-C109; sync VDR-TXA1-C119 VDR-TXA1-C118; totals VDR-TXA1-C076; posting rename VDR-TXA1-C120 VDR-TXA1-C121.
- Stock valuation touch points VDR-TXA1-C236 VDR-TXA1-C237 VDR-TXA1-C238 VDR-TXA1-C239 VDR-TXA1-C322 VDR-TXA1-C242 VDR-TXA1-C178.

### D3 Source/technical/workflow logic
1. Vendor line with deductibility < 100: non-deductible base lines anticipated VDR-TXA1-C109; created at sync VDR-TXA1-C119; tax line VDR-TXA1-C118.
2. Engine drops reverse-charge entries and subtracts them for non-deductible lines VDR-TXA1-C049; totals subtract the non-deductible tax VDR-TXA1-C076.
3. Posting renames private-part lines with the move number VDR-TXA1-C120; user joins the group VDR-TXA1-C121.
4. Receipt cost: untaxed amount plus taxes without account via `total_void` VDR-TXA1-C237 VDR-TXA1-C236.
5. Customer invoice cost entries only for real-time valuation products, without tax VDR-TXA1-C322 VDR-TXA1-C240.

State list:
- `vendor bill line deductibility 100 -> normal`
- `deductibility < 100 -> private-part lines created [sync] (VDR-TXA1-C119)`
- `bill posted -> private-part lines renamed with number (VDR-TXA1-C120)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | 60% deductible line: 40% of subtotal and its tax go to the private-share account (VDR-TXA1-C119, VDR-TXA1-C118). |
| 2 | Reversal/cancel/negative path | Deductibility allowed only on vendor documents VDR-TXA1-C124; credit-note reversal of private-part lines is U11 (UNKNOWN here). |
| 3 | Multi-company / data scope | Private-share account per journal (company-checked) VDR-TXA1-C125. |
| 4 | Side effects and cross-module | Totals VDR-TXA1-C076; stock cost VDR-TXA1-C237; cost entries untaxed VDR-TXA1-C240. |
| 5 | Configuration and optionality | Group reveals column; journal account unset in DB (VDR-TXA1-C281); anglo-saxon off (VDR-TXA1-C178). |
| 6 | Validation and constraints | 0 to 100; vendor only VDR-TXA1-C124. |
| 7 | Roles and permissions | Column revealed by a dedicated group; account on journal shown to read-only accounting role (view). |
| 8 | Scheduled/automated | NOT APPLICABLE. |
| 9 | Exception and failure | If the private-share account is missing the default journal account is used VDR-TXA1-C118. |
| 10 | Accounting, audit, compliance | Mechanism is percentage based and not a statutory prohibited-input-VAT treatment; Thai prohibited input tax need: STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
Purchase journal has no private-share account; the group exists; anglo-saxon off; all 18 Thai tax lines have accounts so `total_void` equals the untaxed amount for Thai taxes (VDR-TXA1-C281, VDR-TXA1-C275).

### Unknown / Runtime
- UNKNOWN: whether a Thai prohibited-input-VAT treatment can be fully represented by the deductibility mechanism (the tag grid would still count the base as claimable) - pending TXS.
- RT: private-part entries on a posted Thai bill.

---

## CAP-TXA1-07 Price-included / price-excluded handling, currency conversion and multi-currency tax amounts

**Function-ID(s):** FUNCTION MAPPING REQUIRED (base currency model hand-off to U01/U25).

### D1 Business purpose and process semantics
Decide whether entered prices contain tax, extract tax from inclusive prices, and express every tax amount in both the document currency and the company currency (THB) with a stored rate, so that foreign-currency sales and purchases carry consistent tax amounts. VDR-TXA1-C008 VDR-TXA1-C046

### D2 Architecture, data, objects
- Price-inclusion: company default VDR-TXA1-C170 lock VDR-TXA1-C171; per-tax override VDR-TXA1-C007 VDR-TXA1-C008; onchange VDR-TXA1-C018; forced modes VDR-TXA1-C086 VDR-TXA1-C087; special modes VDR-TXA1-C041.
- Unit price helpers VDR-TXA1-C153 VDR-TXA1-C141 VDR-TXA1-C221 VDR-TXA1-C151 VDR-TXA1-C152; display VDR-TXA1-C287.
- Currency: document rate VDR-TXA1-C201 VDR-TXA1-C202 VDR-TXA1-C203 VDR-TXA1-C204; order rate VDR-TXA1-C215 VDR-TXA1-C234; line rate VDR-TXA1-C142 VDR-TXA1-C143; lookup VDR-TXA1-C205 VDR-TXA1-C207 VDR-TXA1-C206 VDR-TXA1-C209; company exchange accounts VDR-TXA1-C179; rounding guard VDR-TXA1-C208 VDR-TXA1-C210.
- Tax amounts in two currencies VDR-TXA1-C046 VDR-TXA1-C050 VDR-TXA1-C059 VDR-TXA1-C106 VDR-TXA1-C112 VDR-TXA1-C173.
- Tax-date hook VDR-TXA1-C267 VDR-TXA1-C122.

### D3 Source/technical/workflow logic
1. Effective price-include flag per tax VDR-TXA1-C008; batch extraction VDR-TXA1-C024 VDR-TXA1-C034.
2. Document currency rate at invoice date VDR-TXA1-C201; stored and recomputable VDR-TXA1-C202; positive VDR-TXA1-C128; refresh VDR-TXA1-C203.
3. Company amounts = document amounts / rate, rounded per currency VDR-TXA1-C050 VDR-TXA1-C059.
4. Sale order rate at order date; invoice created from order recomputes its own rate VDR-TXA1-C215 VDR-TXA1-C224.
5. Rate lookup fallback chain VDR-TXA1-C205; no feed in installed set; DB has no rate rows VDR-TXA1-C278.
6. Display of tax in company currency on foreign sale documents VDR-TXA1-C112; printed block VDR-TXA1-C288.

State list:
- `invoice date set or changed -> expected rate recomputed (VDR-TXA1-C202)`
- `user edits rate -> manual rate kept [protecting at post] (VDR-TXA1-C204)`
- `rate changed -> foreign tax amounts kept, company balances re-derived (VDR-TXA1-C115)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | USD sale with 7% VAT: tax in USD and THB from the invoice-date rate (VDR-TXA1-C050); numeric RT. |
| 2 | Reversal/cancel/negative path | Rate refresh and manual rate protection (VDR-TXA1-C203, VDR-TXA1-C204); credit note rate at its own date (U12/U25). |
| 3 | Multi-company / data scope | Rates only on the root company (VDR-TXA1-C206); price-include and rounding per company (VDR-TXA1-C170). |
| 4 | Side effects and cross-module | Sale and purchase orders, expenses and stock valuation convert with their own rate (VDR-TXA1-C215, VDR-TXA1-C234, VDR-TXA1-C237, VDR-TXA1-C244). |
| 5 | Configuration and optionality | Company price default; tax override; taxes-in-company-currency flag (VDR-TXA1-C173); rates optional. |
| 6 | Validation and constraints | Positive rate VDR-TXA1-C128; price default locked after invoicing VDR-TXA1-C171; precision cannot shrink VDR-TXA1-C210. |
| 7 | Roles and permissions | Currency and rate maintenance by accounting roles (U01/U25). |
| 8 | Scheduled/automated | NOT PRESENT - no installed module or cron fetches rates (search of installed modules and DB crons) VDR-TXA1-C278. |
| 9 | Exception and failure | Missing rate silently gives 1.0 VDR-TXA1-C205; zero rate gives zero company amounts VDR-TXA1-C050. |
| 10 | Accounting, audit, compliance | Stored rate on the document is the audit anchor; official rate source and tax-point rate date are STATUTORY CHECK PENDING (TXS); taxable supply date is a stub VDR-TXA1-C267. |

### DB reconciliation (config only)
THB (2 decimals, 0.01) and USD active, 0 rate rows (VDR-TXA1-C278); company tax_excluded, taxes in company currency on (VDR-TXA1-C276); Thai sale withholding records forced tax_excluded, purchase withholding not (VDR-TXA1-C198, VDR-TXA1-C324).

### Unknown / Runtime
- RT: numeric tax amounts of a foreign-currency Thai invoice in both currencies; interplay of rate date and posting date.
- RT: behaviour if the company default is switched to tax included with withholding (VDR-TXA1-C324).
- UNKNOWN: statutory rate source and rate date for VAT on foreign-currency transactions (pending TXS).

---

## CAP-TXA1-08 Company, partner, product and fiscal-position configuration that drives tax behaviour

**Function-ID(s):** FUNCTION MAPPING REQUIRED (MCT-F03 concerns chart sharing and was judged not to match tax-scope claims).

### D1 Business purpose and process semantics
Collect every configuration switch that changes which taxes and accounts a Thai legal entity gets on a document: company settings, partner fiscal position and VAT, product tax sets, ledger default taxes, fiscal-position tax and account mapping, tax country guards and company hierarchy scope. VDR-TXA1-C174 VDR-TXA1-C161

### D2 Architecture, data, objects
- Company: VDR-TXA1-C169 VDR-TXA1-C170 VDR-TXA1-C172 VDR-TXA1-C174 VDR-TXA1-C175 VDR-TXA1-C173 VDR-TXA1-C178 VDR-TXA1-C179 VDR-TXA1-C177; settings VDR-TXA1-C181.
- Partner: manual position VDR-TXA1-C162; VAT presence VDR-TXA1-C168; VAT validation stub VDR-TXA1-C167 VDR-TXA1-C180.
- Product: VDR-TXA1-C145 VDR-TXA1-C146 VDR-TXA1-C147 VDR-TXA1-C148.
- Fiscal position model VDR-TXA1-C155 VDR-TXA1-C163 VDR-TXA1-C164 VDR-TXA1-C165 VDR-TXA1-C166; mapping VDR-TXA1-C156 VDR-TXA1-C157 VDR-TXA1-C158; price adaptation VDR-TXA1-C037 VDR-TXA1-C154.
- Guards: VDR-TXA1-C126 VDR-TXA1-C113 VDR-TXA1-C214 VDR-TXA1-C235 VDR-TXA1-C219.
- Hierarchy: VDR-TXA1-C091 VDR-TXA1-C090 VDR-TXA1-C272 VDR-TXA1-C206 VDR-TXA1-C176.

### D3 Source/technical/workflow logic
1. Finder: partner? delivery address? manual? country? automatic candidates VDR-TXA1-C161 VDR-TXA1-C159 VDR-TXA1-C160.
2. Document callers VDR-TXA1-C103 VDR-TXA1-C213 VDR-TXA1-C229 VDR-TXA1-C309 VDR-TXA1-C310 VDR-TXA1-C311; no installed override of finder or mapping VDR-TXA1-C313.
3. Mapping of taxes and accounts VDR-TXA1-C157 VDR-TXA1-C158; price adapted VDR-TXA1-C037.
4. Tax country consistency VDR-TXA1-C126.
5. Defaults at company level VDR-TXA1-C172 VDR-TXA1-C254; partner-level default tax does not exist except through fiscal position VDR-TXA1-C162.

State list:
- `no position -> position found [partner, address or company change] (VDR-TXA1-C103)`
- `position changed on document with lines -> update prompt (VDR-TXA1-C213)`
- `foreign tax created from position -> localization of that country may be installed (VDR-TXA1-C166)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Domestic customer, no position: taxes unchanged (VDR-TXA1-C157). |
| 2 | Reversal/cancel/negative path | Archive positions rather than delete; used positions cannot be removed (VDR-TXA1-C328, VDR-TXA1-C330). |
| 3 | Multi-company / data scope | Company-specific positions before parent; rule parent-of (VDR-TXA1-C159, VDR-TXA1-C272); root rates (VDR-TXA1-C206). |
| 4 | Side effects and cross-module | Position maps taxes, accounts and unit prices (VDR-TXA1-C157, VDR-TXA1-C158, VDR-TXA1-C037); callers in order modules VDR-TXA1-C309. |
| 5 | Configuration and optionality | Automatic detection per position; none seeded (VDR-TXA1-C277, VDR-TXA1-C187). |
| 6 | Validation and constraints | Zip range, foreign VAT rules, account mapping unique (VDR-TXA1-C163, VDR-TXA1-C164, VDR-TXA1-C165); tax country guard (VDR-TXA1-C126). |
| 7 | Roles and permissions | Positions editable by accounting administrator; read for all internal users (VDR-TXA1-C271). |
| 8 | Scheduled/automated | NOT APPLICABLE - on-demand. |
| 9 | Exception and failure | Foreign taxes creation restricted to managers (VDR-TXA1-C166); missing partner country gives no position (VDR-TXA1-C161). |
| 10 | Accounting, audit, compliance | Position is stored on the document and drives tax mapping; Thai partner-driven rules (company vs individual payee, foreign payee) not shipped: STATUTORY CHECK PENDING (TXS). |

### DB reconciliation (config only)
Company (VDR-TXA1-C276); 0 fiscal positions, 0 mappings, 0 account default taxes (VDR-TXA1-C277); seeded products (VDR-TXA1-C279); 7 journals (VDR-TXA1-C281).

### Unknown / Runtime
- UNKNOWN: Thai VAT-number and branch validation (VAT validation add-on not installed, VDR-TXA1-C319; U24/U23).
- RT: detection and mapping with a sample position (never exercised: VDR-TXA1-C277).

---

## CAP-TXA1-09 Tax record lifecycle, template loading, security and locks (tax scope)

**Function-ID(s):** PCO-F01 on lock-date claims (genuine match: lock dates including tax lock); otherwise FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Control who can change taxes, when a tax may be archived or deleted, how a chart template creates or reloads taxes, how taxed entries interact with the tax lock date, and where optional add-ons sit. VDR-TXA1-C093 VDR-TXA1-C256 VDR-TXA1-C293

### D2 Architecture, data, objects
- Lifecycle: VDR-TXA1-C093 VDR-TXA1-C016 VDR-TXA1-C300 VDR-TXA1-C301 VDR-TXA1-C302.
- Constraints: VDR-TXA1-C010 VDR-TXA1-C011 VDR-TXA1-C012 VDR-TXA1-C013.
- Loader: VDR-TXA1-C254 VDR-TXA1-C255 VDR-TXA1-C256 VDR-TXA1-C257 VDR-TXA1-C258 VDR-TXA1-C259 VDR-TXA1-C315 VDR-TXA1-C316.
- Security: VDR-TXA1-C271 VDR-TXA1-C272 VDR-TXA1-C274.
- Locks: VDR-TXA1-C129 VDR-TXA1-C263 VDR-TXA1-C266 VDR-TXA1-C293 VDR-TXA1-C294.
- Add-ons not installed: VDR-TXA1-C317 VDR-TXA1-C318 VDR-TXA1-C319 VDR-TXA1-C320 VDR-TXA1-C321.

### D3 Source/technical/workflow logic
1. Create: default distribution lines (VDR-TXA1-C325); name and group checks VDR-TXA1-C010 VDR-TXA1-C011.
2. Use: first journal item, reconciliation model, purchase line or expense marks the tax used VDR-TXA1-C093 VDR-TXA1-C300 VDR-TXA1-C301; sales-only use does not VDR-TXA1-C302.
3. Reload template: changed taxes skipped or renamed VDR-TXA1-C256 VDR-TXA1-C257; tags preserved on upgrade VDR-TXA1-C258.
4. Lock: taxed non-sale entries moved to first open day VDR-TXA1-C266; posted taxed lines protected VDR-TXA1-C294.

State list:
- `tax created -> in use [first reference] (VDR-TXA1-C093)`
- `in use -> deletion refused (VDR-TXA1-C093)`
- `in use -> archived [write active=False; no guard] (VDR-TXA1-C326)`
- `template reloaded -> tax changed -> old tax renamed, new created [only when creation forced] (VDR-TXA1-C256)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Admin loads Thai chart; 18 taxes created (VDR-TXA1-C275). |
| 2 | Reversal/cancel/negative path | Used tax cannot be deleted; archive instead (VDR-TXA1-C093); template-change rename (VDR-TXA1-C256). |
| 3 | Multi-company / data scope | Company rule parent-of (VDR-TXA1-C272); company change blocked once used (VDR-TXA1-C016). |
| 4 | Side effects and cross-module | Purchase and expense mark taxes as used (VDR-TXA1-C300, VDR-TXA1-C301); sale does not (VDR-TXA1-C302); loader extended by sale and stock accounting (VDR-TXA1-C316, VDR-TXA1-C315). |
| 5 | Configuration and optionality | Tax lock date empty in DB (VDR-TXA1-C276); add-ons optional and not installed (VDR-TXA1-C317). |
| 6 | Validation and constraints | Unique names, group country, cash-basis account (VDR-TXA1-C010, VDR-TXA1-C011, VDR-TXA1-C012). |
| 7 | Roles and permissions | Read for all internal users and accounting roles; write/create/delete accounting administrator only (VDR-TXA1-C271); 4 multi-company rules in DB. |
| 8 | Scheduled/automated | NOT APPLICABLE - no tax cron, no automation (DB 0). |
| 9 | Exception and failure | Delete refused with message; lock violations refused (VDR-TXA1-C294); not-installed add-ons absent. |
| 10 | Accounting, audit, compliance | Tracked field changes logged only after first use (VDR-TXA1-C327); lock behaviour in U11/U24 CAP-U24-07. |

### DB reconciliation (config only)
ACL rows for tax models: tax 7, group 5, distribution line 4, fiscal position 3, position account 2, cash rounding 2; rules: tax, group, distribution line, fiscal position (4); 0 crons and 0 automations concern taxes; `l10n_th` declares no ACL, rule, group or cron.

### Unknown / Runtime
- RT: reload behaviour of the Thai template against modified taxes (U13 C184 aligned).
- UNKNOWN: whether a tax used only on sales order lines can be deleted in practice (foreign key behaviour not executed; VDR-TXA1-C302).

---

## REGISTER: Function Catalog

Cat-IDs are candidate catalogue ids, not Function-IDs. Native status vocabulary: NATIVE, PARTIAL, NATIVE GAP / EXTENSION REQUIRED, UNKNOWN. Where a status is NATIVE GAP / EXTENSION REQUIRED the statutory need is pending TXS validation; absence in Community source is not proof that no business requirement exists.

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Entry points / triggers | Claim-IDs | Statutory link (statutory-register id or n/a) | Native status |
|---|---|---|---|---|---|---|---|
| TXA1-F01 | Define a tax record: computation type, usage scope, goods or services scope, sequence, rate, label | 1 | FUNCTION MAPPING REQUIRED | account.tax form; chart template load; _constrains_name | VDR-TXA1-C001 VDR-TXA1-C002 VDR-TXA1-C003 VDR-TXA1-C004 VDR-TXA1-C017 | n/a | NATIVE |
| TXA1-F02 | Expand a group of taxes into ordered member taxes | 1 | FUNCTION MAPPING REQUIRED | _flatten_taxes_and_sort_them; _check_children_scope | VDR-TXA1-C020 VDR-TXA1-C015 | n/a | NATIVE |
| TXA1-F03 | Batch compatible taxes for joint calculation | 1 | FUNCTION MAPPING REQUIRED | _batch_for_taxes_computation | VDR-TXA1-C021 | n/a | NATIVE |
| TXA1-F04 | Compute a percentage tax added on top of the price for one line | 1 | FUNCTION MAPPING REQUIRED | _eval_tax_amount_price_excluded; _get_tax_details | VDR-TXA1-C026 VDR-TXA1-C032 VDR-TXA1-C033 VDR-TXA1-C331 | n/a | NATIVE |
| TXA1-F05 | Compute a fixed-amount tax | 1 | FUNCTION MAPPING REQUIRED | _eval_tax_amount_fixed_amount; _can_be_discounted | VDR-TXA1-C023 VDR-TXA1-C084 | n/a | NATIVE |
| TXA1-F06 | Compute a division-type tax | 1 | FUNCTION MAPPING REQUIRED | _eval_tax_amount_price_excluded; _eval_tax_amount_price_included | VDR-TXA1-C027 VDR-TXA1-C025 | n/a | NATIVE |
| TXA1-F07 | Formula-defined tax | 1 | FUNCTION MAPPING REQUIRED | NOT PRESENT in installed set: search = selection_add of amount_type across installed modules (none); add-on account_tax_python exists in source, not installed | VDR-TXA1-C317 VDR-TXA1-C001 | n/a | UNKNOWN |
| TXA1-F08 | Make a tax affect the base of later taxes (include-in-base chain) | 1 | FUNCTION MAPPING REQUIRED | _propagate_extra_taxes_base; include_base_amount; is_base_affected | VDR-TXA1-C005 VDR-TXA1-C006 VDR-TXA1-C022 | n/a | NATIVE |
| TXA1-F09 | Extract tax from a tax-included price | 1 | FUNCTION MAPPING REQUIRED | _eval_tax_amount_price_included; base minus batch tax | VDR-TXA1-C024 VDR-TXA1-C034 VDR-TXA1-C025 | n/a | NATIVE |
| TXA1-F10 | Choose price-included or price-excluded per tax and per company | 6 | FUNCTION MAPPING REQUIRED | price_include_override; company account_price_include; _compute_price_include | VDR-TXA1-C007 VDR-TXA1-C008 VDR-TXA1-C170 VDR-TXA1-C018 | n/a | NATIVE |
| TXA1-F11 | Force all taxes to included or excluded mode for one calculation | 6 | FUNCTION MAPPING REQUIRED | special_mode; force_price_include; handle_price_include | VDR-TXA1-C041 VDR-TXA1-C086 VDR-TXA1-C087 VDR-TXA1-C292 | n/a | NATIVE |
| TXA1-F12 | Compute line totals with and without tax | 1 | FUNCTION MAPPING REQUIRED | _get_tax_details; _add_tax_details_in_base_line; _compute_amount on lines | VDR-TXA1-C035 VDR-TXA1-C028 VDR-TXA1-C046 | n/a | NATIVE |
| TXA1-F13 | Apply line discount before tax | 1 | FUNCTION MAPPING REQUIRED | price_unit_after_discount in _add_tax_details_in_base_line | VDR-TXA1-C047 | n/a | NATIVE |
| TXA1-F14 | Split global discounts, down payments and returns across taxes | 1 | FUNCTION MAPPING REQUIRED | _prepare_global_discount_lines; _prepare_down_payment_lines; _dispatch_return_of_merchandise_lines; sale discount and advance wizards | VDR-TXA1-C099 VDR-TXA1-C100 VDR-TXA1-C101 VDR-TXA1-C102 VDR-TXA1-C226 VDR-TXA1-C227 VDR-TXA1-C228 VDR-TXA1-C252 VDR-TXA1-C253 | n/a | NATIVE |
| TXA1-F15 | Reduce tax for an early-payment discount (three modes) | 1 | FUNCTION MAPPING REQUIRED | early_pay_discount_computation; _prepare_epd_base_line_for_taxes_computation; _add_base_lines_for_early_payment_discount | VDR-TXA1-C107 VDR-TXA1-C217 VDR-TXA1-C144 VDR-TXA1-C280 | n/a | NATIVE |
| TXA1-F16 | Reverse-charge pair (negative-factor distribution) | 1 | FUNCTION MAPPING REQUIRED | has_negative_factor; reverse-charge tax data | VDR-TXA1-C030 VDR-TXA1-C031 VDR-TXA1-C067 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F17 | Round each line | 6 | FUNCTION MAPPING REQUIRED | round_per_line branches | VDR-TXA1-C029 VDR-TXA1-C051 VDR-TXA1-C169 | n/a | NATIVE |
| TXA1-F18 | Round globally and distribute the delta | 6 | FUNCTION MAPPING REQUIRED | _round_tax_details_tax_amounts; _round_tax_details_base_lines; _distribute_delta_amount_smoothly | VDR-TXA1-C053 VDR-TXA1-C054 VDR-TXA1-C055 VDR-TXA1-C052 VDR-TXA1-C057 VDR-TXA1-C332 | n/a | NATIVE |
| TXA1-F19 | Keep or discard manually edited tax amounts | 1 | FUNCTION MAPPING REQUIRED | manual_tax_amounts; _inverse_tax_totals; _sync_tax_lines | VDR-TXA1-C043 VDR-TXA1-C044 VDR-TXA1-C056 VDR-TXA1-C058 VDR-TXA1-C127 VDR-TXA1-C114 VDR-TXA1-C116 | n/a | NATIVE |
| TXA1-F20 | Cash rounding of document totals | 6 | FUNCTION MAPPING REQUIRED | account.cash.rounding; _get_tax_totals_summary cash branch | VDR-TXA1-C211 VDR-TXA1-C212 VDR-TXA1-C075 VDR-TXA1-C108 | n/a | NATIVE |
| TXA1-F21 | Document tax totals by tax group and subtotal | 1 | FUNCTION MAPPING REQUIRED | _get_tax_totals_summary; _compute_tax_totals | VDR-TXA1-C071 VDR-TXA1-C072 VDR-TXA1-C073 VDR-TXA1-C074 VDR-TXA1-C111 VDR-TXA1-C216 VDR-TXA1-C232 VDR-TXA1-C078 | n/a | NATIVE |
| TXA1-F22 | Distribute tax amount over base and tax distribution lines with account | 1 | FUNCTION MAPPING REQUIRED | _add_accounting_data_to_base_line_tax_details; repartition lines | VDR-TXA1-C014 VDR-TXA1-C094 VDR-TXA1-C098 VDR-TXA1-C062 VDR-TXA1-C068 VDR-TXA1-C064 VDR-TXA1-C262 | n/a | NATIVE |
| TXA1-F23 | Attach tax grid tags to base and tax items (including product tags) | 1 | FUNCTION MAPPING REQUIRED | tag_ids; product account_tag_ids | VDR-TXA1-C063 VDR-TXA1-C065 VDR-TXA1-C066 VDR-TXA1-C069 VDR-TXA1-C097 VDR-TXA1-C147 | n/a | NATIVE |
| TXA1-F24 | Generate and synchronise tax journal items on draft documents | 1 | FUNCTION MAPPING REQUIRED | _prepare_tax_lines; _sync_tax_lines | VDR-TXA1-C060 VDR-TXA1-C080 VDR-TXA1-C081 VDR-TXA1-C082 VDR-TXA1-C083 VDR-TXA1-C114 | n/a | NATIVE |
| TXA1-F25 | Suppress zero-amount tax items | 3 | FUNCTION MAPPING REQUIRED | __keep_zero_line; zero filter in _prepare_tax_lines | VDR-TXA1-C079 | n/a | NATIVE |
| TXA1-F26 | Allocate analytic split to tax items | 1 | FUNCTION MAPPING REQUIRED | _prepare_base_line_tax_repartition_grouping_key; tax analytic flag | VDR-TXA1-C061 | n/a | NATIVE |
| TXA1-F27 | Recognise tax on payment (cash basis) | 1 | FUNCTION MAPPING REQUIRED | tax_exigibility; cash_basis_transition_account_id; _create_tax_cash_basis_moves | VDR-TXA1-C009 VDR-TXA1-C012 VDR-TXA1-C096 VDR-TXA1-C264 VDR-TXA1-C117 VDR-TXA1-C295 VDR-TXA1-C070 VDR-TXA1-C270 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F28 | Tax closing flag per distribution line and month-end settlement of tax accounts | 1 | FUNCTION MAPPING REQUIRED | use_in_tax_closing; NOT PRESENT routine: search = every non-localization module for the flag (readers: account_tax.py and account_move_line_tax_details.py only) | VDR-TXA1-C095 VDR-TXA1-C323 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F29 | Query base-to-tax item mapping for tax reporting | 9 | FUNCTION MAPPING REQUIRED | _get_query_tax_details_from_domain | VDR-TXA1-C265 | n/a | NATIVE |
| TXA1-F30 | Legacy single-line tax computation API | 1 | FUNCTION MAPPING REQUIRED | compute_all | VDR-TXA1-C085 VDR-TXA1-C086 VDR-TXA1-C087 VDR-TXA1-C088 VDR-TXA1-C089 VDR-TXA1-C090 | n/a | NATIVE |
| TXA1-F31 | Client-side preview of tax results | 1 | FUNCTION MAPPING REQUIRED | account_tax.js mirror | VDR-TXA1-C038 VDR-TXA1-C268 VDR-TXA1-C269 | n/a | NATIVE |
| TXA1-F32 | Guard tax lifecycle: archive, delete, company change, used flag, change log | 1 | FUNCTION MAPPING REQUIRED | unlink_except_tax_used; _check_company_consistency; _compute_is_used overrides | VDR-TXA1-C093 VDR-TXA1-C016 VDR-TXA1-C300 VDR-TXA1-C301 VDR-TXA1-C302 VDR-TXA1-C325 VDR-TXA1-C326 VDR-TXA1-C327 VDR-TXA1-C338 | n/a | NATIVE |
| TXA1-F33 | Enforce tax and tax group constraints | 1 | FUNCTION MAPPING REQUIRED | _constrains_name; validate_tax_group_id; _check_children_scope | VDR-TXA1-C010 VDR-TXA1-C011 VDR-TXA1-C012 VDR-TXA1-C015 VDR-TXA1-C013 | n/a | NATIVE |
| TXA1-F34 | Load or reload taxes from a chart template | 1 | FUNCTION MAPPING REQUIRED | try_loading; _load_data tax branch | VDR-TXA1-C256 VDR-TXA1-C257 VDR-TXA1-C258 VDR-TXA1-C259 VDR-TXA1-C254 VDR-TXA1-C255 VDR-TXA1-C315 VDR-TXA1-C316 | n/a | NATIVE |
| TXA1-F35 | Apply sales VAT on sales order lines | 2 | FUNCTION MAPPING REQUIRED | sale.order.line _compute_tax_ids; _compute_amount | VDR-TXA1-C218 VDR-TXA1-C220 VDR-TXA1-C219 VDR-TXA1-C222 VDR-TXA1-C223 VDR-TXA1-C216 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F36 | Apply sales VAT on customer invoice lines | 2 | FUNCTION MAPPING REQUIRED | account.move.line _compute_tax_ids; _get_computed_taxes | VDR-TXA1-C134 VDR-TXA1-C135 VDR-TXA1-C138 VDR-TXA1-C131 VDR-TXA1-C225 VDR-TXA1-C224 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F37 | Apply purchase VAT on purchase order lines | 2 | FUNCTION MAPPING REQUIRED | purchase.order.line _compute_tax_id | VDR-TXA1-C230 VDR-TXA1-C231 VDR-TXA1-C232 VDR-TXA1-C229 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F38 | Apply purchase VAT on vendor bill lines | 2 | FUNCTION MAPPING REQUIRED | account.move.line _get_computed_taxes (purchase branch) | VDR-TXA1-C136 VDR-TXA1-C134 VDR-TXA1-C138 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F39 | Default tax from the product, and from the company into new products | 2 | FUNCTION MAPPING REQUIRED | product taxes_id; supplier_taxes_id; create; _force_default_tax | VDR-TXA1-C145 VDR-TXA1-C146 VDR-TXA1-C150 VDR-TXA1-C149 VDR-TXA1-C172 VDR-TXA1-C254 VDR-TXA1-C279 VDR-TXA1-C312 | n/a | NATIVE |
| TXA1-F40 | Default tax from the ledger account | 2 | FUNCTION MAPPING REQUIRED | account.account tax_ids | VDR-TXA1-C260 VDR-TXA1-C261 VDR-TXA1-C135 VDR-TXA1-C136 VDR-TXA1-C137 | n/a | NATIVE |
| TXA1-F41 | Default tax from the partner (through fiscal position) | 8 | FUNCTION MAPPING REQUIRED | property_account_position_id; _get_fiscal_position | VDR-TXA1-C162 VDR-TXA1-C161 VDR-TXA1-C103 | n/a | PARTIAL |
| TXA1-F42 | Default tax from the company at document level (quick encoding) | 8 | FUNCTION MAPPING REQUIRED | _get_quick_edit_suggestions fallback | VDR-TXA1-C291 VDR-TXA1-C139 VDR-TXA1-C172 | n/a | NATIVE |
| TXA1-F43 | Quick encoding by typed total with frequent tax suggestion | 2 | FUNCTION MAPPING REQUIRED | _get_frequent_account_and_taxes | VDR-TXA1-C130 VDR-TXA1-C292 VDR-TXA1-C291 | n/a | NATIVE |
| TXA1-F44 | Apply tax on delivery charge lines | 2 | FUNCTION MAPPING REQUIRED | delivery sale_order carrier line; delivery_carrier price helper | VDR-TXA1-C250 VDR-TXA1-C251 VDR-TXA1-C305 | n/a | NATIVE |
| TXA1-F45 | Apply tax on loyalty reward and discount lines | 2 | FUNCTION MAPPING REQUIRED | sale_loyalty reward line tax compute | VDR-TXA1-C247 VDR-TXA1-C248 VDR-TXA1-C249 VDR-TXA1-C306 | n/a | NATIVE |
| TXA1-F46 | Apply tax on expense claims | 2 | FUNCTION MAPPING REQUIRED | hr.expense tax compute; engine hook extensions | VDR-TXA1-C243 VDR-TXA1-C244 VDR-TXA1-C245 VDR-TXA1-C246 VDR-TXA1-C303 VDR-TXA1-C304 | n/a | NATIVE |
| TXA1-F47 | Represent standard-rated VAT (7 percent purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | l10n_th tax records tax_input_vat; tax_output_vat | VDR-TXA1-C190 VDR-TXA1-C191 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F48 | Represent zero-rated treatment (0 percent purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | l10n_th tax records tax_input_vat_0; tax_output_vat_0 | VDR-TXA1-C192 VDR-TXA1-C193 VDR-TXA1-C079 VDR-TXA1-C200 VDR-TXA1-C333 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F49 | Represent exempt treatment (0 percent exempt purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | l10n_th tax records tax_input_vat_exempted; tax_output_vat_exempted | VDR-TXA1-C194 VDR-TXA1-C195 VDR-TXA1-C079 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F50 | Partly deductible vendor-bill lines routed to a private-share account | 3 | FUNCTION MAPPING REQUIRED | deductible_amount; _sync_non_deductible_base_lines; non_deductible_account_id | VDR-TXA1-C123 VDR-TXA1-C124 VDR-TXA1-C109 VDR-TXA1-C119 VDR-TXA1-C118 VDR-TXA1-C076 VDR-TXA1-C120 VDR-TXA1-C121 VDR-TXA1-C273 VDR-TXA1-C125 VDR-TXA1-C049 VDR-TXA1-C281 VDR-TXA1-C077 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F51 | Capitalise taxes without account into inventory cost | 3 | GRV-F04 | _get_stock_move_price_unit using compute_all total_void | VDR-TXA1-C237 VDR-TXA1-C236 VDR-TXA1-C088 VDR-TXA1-C238 | n/a | NATIVE |
| TXA1-F52 | Prohibited or non-claimable input VAT as a distinct tax treatment with return-grid exclusion | 3 | FUNCTION MAPPING REQUIRED | NOT PRESENT: search = installed tax records, deductibility fields, tag definitions; only a zero-rate exempt purchase tax and the percentage mechanism exist | VDR-TXA1-C194 VDR-TXA1-C119 VDR-TXA1-C283 VDR-TXA1-C336 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F53 | Withholding tax computed on purchase documents at posting | 3 | FUNCTION MAPPING REQUIRED | l10n_th tax records tax_wht_co_*, tax_wht_pers_* | VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C324 VDR-TXA1-C026 VDR-TXA1-C009 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F54 | Withholding tax suffered on sales documents | 3 | FUNCTION MAPPING REQUIRED | l10n_th tax records tax_wht_income_* | VDR-TXA1-C198 VDR-TXA1-C026 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F55 | Choose withholding tax from payee type (company, individual, foreign) | 3 | FUNCTION MAPPING REQUIRED | NOT PRESENT: search = fiscal positions (none shipped), partner fields in the Thai module (branch label only), tax selection logic | VDR-TXA1-C187 VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C157 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F56 | Withholding tax registered at payment time | 3 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax _add_tax_details_in_base_line (add-on not installed) | VDR-TXA1-C318 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F57 | Lock the company price-inclusion default after invoicing | 6 | FUNCTION MAPPING REQUIRED | _check_set_account_price_include | VDR-TXA1-C171 | n/a | NATIVE |
| TXA1-F58 | Adapt unit price when a fiscal position maps included taxes | 6 | FUNCTION MAPPING REQUIRED | _adapt_price_unit_to_another_taxes; _fix_tax_included_price | VDR-TXA1-C037 VDR-TXA1-C154 VDR-TXA1-C092 VDR-TXA1-C221 VDR-TXA1-C251 VDR-TXA1-C153 VDR-TXA1-C141 | n/a | NATIVE |
| TXA1-F59 | Show amounts with and without tax on products and documents | 6 | FUNCTION MAPPING REQUIRED | _construct_tax_string; invoice report columns | VDR-TXA1-C152 VDR-TXA1-C151 VDR-TXA1-C287 | n/a | NATIVE |
| TXA1-F60 | Compute tax amounts in document currency and company currency | 6 | FUNCTION MAPPING REQUIRED | _add_tax_details_in_base_line (rate division) | VDR-TXA1-C046 VDR-TXA1-C050 VDR-TXA1-C059 VDR-TXA1-C042 VDR-TXA1-C143 | n/a | NATIVE |
| TXA1-F61 | Select, store, refresh and protect the invoice currency rate | 6 | FUNCTION MAPPING REQUIRED | invoice_currency_rate; refresh_invoice_currency_rate | VDR-TXA1-C201 VDR-TXA1-C202 VDR-TXA1-C203 VDR-TXA1-C204 VDR-TXA1-C106 VDR-TXA1-C115 VDR-TXA1-C128 VDR-TXA1-C142 | n/a | NATIVE |
| TXA1-F62 | Order-level currency rate (sales and purchase) | 6 | FUNCTION MAPPING REQUIRED | currency_rate on orders | VDR-TXA1-C215 VDR-TXA1-C234 VDR-TXA1-C224 VDR-TXA1-C233 VDR-TXA1-C334 | n/a | NATIVE |
| TXA1-F63 | Look up and apply exchange rates with fallback | 6 | FUNCTION MAPPING REQUIRED | res.currency _get_rates; _get_conversion_rate; _convert | VDR-TXA1-C205 VDR-TXA1-C207 VDR-TXA1-C206 VDR-TXA1-C209 VDR-TXA1-C278 | n/a | NATIVE |
| TXA1-F64 | Automatic exchange-rate feed | 6 | FUNCTION MAPPING REQUIRED | NOT PRESENT: search = cron rows and installed modules for rate providers (none) | VDR-TXA1-C278 VDR-TXA1-C205 VDR-TXA1-C337 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F65 | Tax-point date for tax and rate (taxable supply date) | 5 | FUNCTION MAPPING REQUIRED | _compute_taxable_supply_date stub | VDR-TXA1-C267 VDR-TXA1-C122 VDR-TXA1-C201 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F66 | Display tax in company currency on foreign sale documents | 6 | FUNCTION MAPPING REQUIRED | display_invoice_tax_company_currency | VDR-TXA1-C112 VDR-TXA1-C173 VDR-TXA1-C288 VDR-TXA1-C233 | n/a | NATIVE |
| TXA1-F67 | Exchange-difference accounts and currency precision guard | 6 | FUNCTION MAPPING REQUIRED | company exchange journal and accounts; currency write guard | VDR-TXA1-C179 VDR-TXA1-C208 VDR-TXA1-C210 | n/a | NATIVE |
| TXA1-F68 | Company tax settings and defaults | 8 | FUNCTION MAPPING REQUIRED | res.company tax fields; settings | VDR-TXA1-C169 VDR-TXA1-C170 VDR-TXA1-C172 VDR-TXA1-C174 VDR-TXA1-C175 VDR-TXA1-C173 VDR-TXA1-C178 VDR-TXA1-C181 VDR-TXA1-C182 VDR-TXA1-C276 | n/a | NATIVE |
| TXA1-F69 | Resolve the fiscal position for a document | 8 | FUNCTION MAPPING REQUIRED | _get_fiscal_position; _get_first_matching_fpos | VDR-TXA1-C161 VDR-TXA1-C159 VDR-TXA1-C160 VDR-TXA1-C177 VDR-TXA1-C103 VDR-TXA1-C213 VDR-TXA1-C229 VDR-TXA1-C309 VDR-TXA1-C310 VDR-TXA1-C311 VDR-TXA1-C313 VDR-TXA1-C329 VDR-TXA1-C277 | n/a | PARTIAL |
| TXA1-F70 | Map taxes through a fiscal position | 8 | FUNCTION MAPPING REQUIRED | map_tax; tax_map | VDR-TXA1-C156 VDR-TXA1-C157 VDR-TXA1-C138 | n/a | NATIVE |
| TXA1-F71 | Map ledger accounts through a fiscal position | 8 | FUNCTION MAPPING REQUIRED | map_account; get_product_accounts | VDR-TXA1-C158 VDR-TXA1-C148 VDR-TXA1-C241 VDR-TXA1-C308 VDR-TXA1-C307 | n/a | NATIVE |
| TXA1-F72 | Foreign-VAT fiscal positions and foreign tax creation | 8 | FUNCTION MAPPING REQUIRED | foreign_vat; action_create_foreign_taxes | VDR-TXA1-C155 VDR-TXA1-C164 VDR-TXA1-C166 VDR-TXA1-C163 VDR-TXA1-C165 VDR-TXA1-C330 VDR-TXA1-C328 | n/a | NATIVE |
| TXA1-F73 | Guard tax country consistency on documents | 8 | FUNCTION MAPPING REQUIRED | _validate_taxes_country; tax_country_id | VDR-TXA1-C126 VDR-TXA1-C113 VDR-TXA1-C214 VDR-TXA1-C235 VDR-TXA1-C219 | n/a | NATIVE |
| TXA1-F74 | Validate partner VAT number | 8 | FUNCTION MAPPING REQUIRED | _run_vat_checks stub; base_vat add-on not installed | VDR-TXA1-C167 VDR-TXA1-C168 VDR-TXA1-C180 VDR-TXA1-C319 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F75 | Scope taxes and rates to the company tree | 8 | FUNCTION MAPPING REQUIRED | parent-of rules; _filter_taxes_by_company; root company rates | VDR-TXA1-C272 VDR-TXA1-C091 VDR-TXA1-C176 VDR-TXA1-C206 | n/a | NATIVE |
| TXA1-F76 | Restrict tax maintenance by role | 8 | FUNCTION MAPPING REQUIRED | ACL rows on tax models | VDR-TXA1-C271 VDR-TXA1-C274 | n/a | NATIVE |
| TXA1-F77 | Exclude tax from stock valuation and cost-of-goods entries | 2 | FUNCTION MAPPING REQUIRED | stock_account _stock_account_prepare_realtime_out_lines_vals; price-difference lines | VDR-TXA1-C240 VDR-TXA1-C322 VDR-TXA1-C242 VDR-TXA1-C239 VDR-TXA1-C178 | n/a | NATIVE |
| TXA1-F78 | Print tax labels, legal notes and group totals on invoices | 4 | FUNCTION MAPPING REQUIRED | report_invoice document templates; taxes_legal_notes | VDR-TXA1-C284 VDR-TXA1-C285 VDR-TXA1-C286 VDR-TXA1-C288 VDR-TXA1-C289 VDR-TXA1-C290 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F79 | Move taxed entries clear of the tax lock date | 5 | PCO-F01 | _get_accounting_date; _check_tax_lock_date | VDR-TXA1-C293 VDR-TXA1-C294 VDR-TXA1-C266 VDR-TXA1-C129 VDR-TXA1-C263 | n/a | NATIVE |
| TXA1-F80 | Classify taxes for electronic invoices (category and exemption codes) | 9 | FUNCTION MAPPING REQUIRED | ubl_cii_tax_category_code; _get_tax_category_code | VDR-TXA1-C296 VDR-TXA1-C297 VDR-TXA1-C298 VDR-TXA1-C299 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F81 | Select Thai invoice layout and branch label | 4 | FUNCTION MAPPING REQUIRED | l10n_th _get_name_invoice_report | VDR-TXA1-C188 VDR-TXA1-C314 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F82 | Convert any business record into a neutral base line and tax line description | 1 | FUNCTION MAPPING REQUIRED | _prepare_base_line_for_taxes_computation; _prepare_tax_line_for_taxes_computation; move _get_rounded_base_and_tax_lines | VDR-TXA1-C039 VDR-TXA1-C045 VDR-TXA1-C040 VDR-TXA1-C036 VDR-TXA1-C019 VDR-TXA1-C105 VDR-TXA1-C110 VDR-TXA1-C048 | n/a | NATIVE |
| TXA1-F83 | Compute document untaxed, tax and total amounts and identify tax items | 1 | FUNCTION MAPPING REQUIRED | _compute_amount; tax_line_id; tax_group_id | VDR-TXA1-C104 VDR-TXA1-C140 VDR-TXA1-C133 VDR-TXA1-C132 | n/a | NATIVE |
| TXA1-F84 | Load the Thai template with tax defaults | 8 | FUNCTION MAPPING REQUIRED | _get_th_template_data; _get_th_res_company; auto-install by company country | VDR-TXA1-C183 VDR-TXA1-C184 VDR-TXA1-C185 VDR-TXA1-C189 VDR-TXA1-C199 VDR-TXA1-C186 VDR-TXA1-C275 VDR-TXA1-C282 VDR-TXA1-C335 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F85 | Issue debit notes and re-apply tax tags to existing items | 4 | FUNCTION MAPPING REQUIRED | account_debit_note; account_update_tax_tags (add-ons not installed) | VDR-TXA1-C321 VDR-TXA1-C320 | STATUTORY CHECK PENDING (TXS) | UNKNOWN |

### Native-status notes

| Cat-ID | Status | Note |
|---|---|---|
| TXA1-F05 | NATIVE | No Thai record uses it. |
| TXA1-F06 | NATIVE | No Thai record uses it. |
| TXA1-F07 | UNKNOWN | Statutory need not established; Community add-on exists but is not installed. |
| TXA1-F08 | NATIVE | No Thai record uses it. |
| TXA1-F16 | PARTIAL | Mechanism present; no Thai record uses it; statutory need pending TXS. |
| TXA1-F20 | NATIVE | No rule configured in this database. |
| TXA1-F25 | NATIVE | Resolves the RT flagged in U24; still RT numerically. |
| TXA1-F27 | PARTIAL | Mechanism present; all 18 Thai taxes are on invoice; suspense VAT accounts exist but are referenced by no tax; statutory need pending TXS. |
| TXA1-F28 | NATIVE GAP / EXTENSION REQUIRED | Candidate: closing entry moving input and output VAT to payable or receivable not present; statutory need pending TXS (also U24 CAP-U24-08). |
| TXA1-F29 | NATIVE | Thai return engine itself is outside this unit (U24). |
| TXA1-F32 | NATIVE | Sales-order-only use does not mark a tax used. |
| TXA1-F40 | NATIVE | No account default tax configured in this database. |
| TXA1-F41 | PARTIAL | No partner tax field exists; effect only via fiscal position; none seeded. |
| TXA1-F42 | NATIVE | Company default does not apply at ordinary line level. |
| TXA1-F47 | NATIVE | Representation only; statutory correctness pending TXS. |
| TXA1-F48 | NATIVE | Representation only; zero item not persisted; group fallback risk. |
| TXA1-F49 | NATIVE | Representation only; statutory correctness pending TXS. |
| TXA1-F50 | PARTIAL | Percentage mechanism native; not a prohibited-input-VAT tax treatment. |
| TXA1-F51 | NATIVE | All Thai tax lines have accounts, so no tax is capitalised under the Thai set. |
| TXA1-F52 | NATIVE GAP / EXTENSION REQUIRED | Candidate; statutory need pending TXS. |
| TXA1-F53 | PARTIAL | Document-time calculation native; certificate, return and payment-time handling outside this unit (U23, U24); price-include risk RT. |
| TXA1-F54 | PARTIAL | Credited to creditable asset account; certificate handling outside this unit. |
| TXA1-F55 | NATIVE GAP / EXTENSION REQUIRED | Candidate; foreign payee form has an account but no tax; statutory need pending TXS. |
| TXA1-F56 | PARTIAL | Community add-on in source, not installed (U23); need pending TXS. |
| TXA1-F63 | NATIVE | Manual rate entry only. |
| TXA1-F64 | NATIVE GAP / EXTENSION REQUIRED | Candidate; foreign-currency Thai transactions need a rate source; statutory rate basis pending TXS. |
| TXA1-F65 | NATIVE GAP / EXTENSION REQUIRED | Candidate; field exists but has no logic; statutory need pending TXS (topic 5 owner U24/TXS). |
| TXA1-F69 | PARTIAL | Mechanism native; no position seeded; no Thai criteria shipped. |
| TXA1-F74 | PARTIAL | Stub only in installed set; add-on not installed (U23). |
| TXA1-F77 | NATIVE | Periodic valuation and anglo-saxon off in this database. |
| TXA1-F78 | PARTIAL | Mechanism native; Thai legal notes none; layout in U24. |
| TXA1-F79 | NATIVE | Lock-date behaviour studied in U11 and U24. |
| TXA1-F80 | PARTIAL | No Thai e-invoice format; codes unset on Thai taxes. |
| TXA1-F81 | PARTIAL | Layout selection native; statutory presentation pending TXS (U24). |
| TXA1-F84 | NATIVE | Content correctness pending TXS (U24 CAP-U24-01). |
| TXA1-F85 | UNKNOWN | Add-ons exist in source, not installed; need pending TXS (U23, U24). |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Claim-IDs | Class |
|---|---|---|---|---|
| TXA1-BR01 | A tax has one computation type: percentage, fixed, percentage-included division, or group; no formula type in the installed set | always | VDR-TXA1-C001 VDR-TXA1-C317 | Calculation |
| TXA1-BR02 | A tax is selectable for sales, purchases or none; none is usable only inside a group | always | VDR-TXA1-C002 VDR-TXA1-C015 | Constraint |
| TXA1-BR03 | Taxes are applied in ascending sequence, ties by creation order; fixed first, then included, then excluded | always | VDR-TXA1-C004 VDR-TXA1-C033 VDR-TXA1-C020 | Calculation |
| TXA1-BR04 | Group members replace the group and are sorted by their own sequence at the group's position | tax group on a line | VDR-TXA1-C020 VDR-TXA1-C015 | Calculation |
| TXA1-BR05 | Same-type, same-inclusion, same-base-flag taxes are computed as one batch | always | VDR-TXA1-C021 | Calculation |
| TXA1-BR06 | A base-affecting tax adds its amount to the base of later taxes unless they opt out | include-in-base flag set | VDR-TXA1-C005 VDR-TXA1-C006 VDR-TXA1-C022 | Configuration |
| TXA1-BR07 | Fixed tax = quantity x amount with the sign of the unit price, not reduced by discount | fixed tax | VDR-TXA1-C023 VDR-TXA1-C084 VDR-TXA1-C248 | Calculation |
| TXA1-BR08 | Exclusive percentage tax = base x percent / 100 (base includes propagated extra base) | percentage tax, price-excluded | VDR-TXA1-C026 | Calculation |
| TXA1-BR09 | Inclusive percentage tax = base x percent / (100 + batch percent total); base = price minus batch tax | percentage tax, price-included | VDR-TXA1-C024 VDR-TXA1-C034 | Calculation |
| TXA1-BR10 | Division tax uses the divided base; inclusive division tax = base x percent / 100 | division tax | VDR-TXA1-C027 VDR-TXA1-C025 | Calculation |
| TXA1-BR11 | Line discount reduces the unit price before taxes | discount on line | VDR-TXA1-C047 | Calculation |
| TXA1-BR12 | Negative-factor taxes create a mirrored reverse-charge entry and are never price-included | distribution with negative factor | VDR-TXA1-C030 VDR-TXA1-C031 VDR-TXA1-C067 | Calculation |
| TXA1-BR13 | A line may force total-included or total-excluded reading of every tax | special mode set | VDR-TXA1-C041 VDR-TXA1-C086 VDR-TXA1-C087 | Configuration |
| TXA1-BR14 | Whether a price includes tax: tax override, else company default (tax excluded) | always | VDR-TXA1-C007 VDR-TXA1-C008 VDR-TXA1-C170 | Default |
| TXA1-BR15 | The company price-inclusion default cannot change after invoicing started | company has accounting | VDR-TXA1-C171 | Constraint |
| TXA1-BR16 | Expense claims are read as tax-included whatever the company default | hr_expense installed | VDR-TXA1-C244 VDR-TXA1-C246 | Calculation |
| TXA1-BR17 | Rounding method follows the company setting (default global); each step rounds in the precision of its currency | always | VDR-TXA1-C048 VDR-TXA1-C169 VDR-TXA1-C208 | Default |
| TXA1-BR18 | Global rounding rounds each tax total once and spreads the delta; included taxes round base plus tax and derive the base | round globally | VDR-TXA1-C053 VDR-TXA1-C054 VDR-TXA1-C055 VDR-TXA1-C052 | Calculation |
| TXA1-BR19 | Per-line rounding rounds tax amounts and raw base at calculation | round per line | VDR-TXA1-C029 VDR-TXA1-C051 | Calculation |
| TXA1-BR20 | Manual tax amounts are kept unless currency or document type changes or taxes-affecting lines change | draft document edited | VDR-TXA1-C114 VDR-TXA1-C116 VDR-TXA1-C044 VDR-TXA1-C127 | Calculation |
| TXA1-BR21 | Totals are grouped by tax group in group order with optional subtotal labels | always | VDR-TXA1-C072 VDR-TXA1-C071 VDR-TXA1-C073 | Calculation |
| TXA1-BR22 | Cash rounding adds a line or changes the largest tax; nothing happens for biggest-tax strategy without a tax | cash rounding set | VDR-TXA1-C075 VDR-TXA1-C211 VDR-TXA1-C212 | Calculation |
| TXA1-BR23 | Global discounts and down payments are split across taxes; fixed taxes are not discounted | discount or advance applied | VDR-TXA1-C099 VDR-TXA1-C100 VDR-TXA1-C226 VDR-TXA1-C227 VDR-TXA1-C084 | Calculation |
| TXA1-BR24 | Early-payment discount tax treatment follows the payment term mode | payment term with early discount | VDR-TXA1-C144 VDR-TXA1-C107 VDR-TXA1-C217 | Configuration |
| TXA1-BR25 | Each tax has mirrored invoice and credit-note distribution lines with one base line and totals of 100 percent | always | VDR-TXA1-C014 VDR-TXA1-C094 VDR-TXA1-C064 | Constraint |
| TXA1-BR26 | A distribution-line account cannot be receivable, payable or off-balance; missing account falls back to the base account | always | VDR-TXA1-C098 VDR-TXA1-C062 | Constraint |
| TXA1-BR27 | Tax tags attach from distribution lines, product tags and preceding base-affecting taxes; cash-basis tags attach at payment | always | VDR-TXA1-C063 VDR-TXA1-C065 VDR-TXA1-C066 VDR-TXA1-C069 VDR-TXA1-C070 | Calculation |
| TXA1-BR28 | Selectable tags are limited to no-country, fiscal-country and foreign-VAT-country tags | tax maintenance | VDR-TXA1-C097 | Constraint |
| TXA1-BR29 | Zero-amount tax items are not created; zero-rated and exempt sales keep only base items with tags | zero-amount tax | VDR-TXA1-C079 | Calculation |
| TXA1-BR30 | Tax items are merged by partner, currency, analytic, account, taxes, distribution line and group | always | VDR-TXA1-C060 VDR-TXA1-C081 | Calculation |
| TXA1-BR31 | Tax items inherit analytic split only for analytic-cost taxes or non-closing lines | analytic distribution present | VDR-TXA1-C061 | Calculation |
| TXA1-BR32 | Draft documents re-synchronise tax items; posted documents do not | draft document | VDR-TXA1-C114 VDR-TXA1-C082 | Calculation |
| TXA1-BR33 | A tax belongs to one tax group; default group is first of its country, else without country | tax created without group | VDR-TXA1-C013 VDR-TXA1-C200 | Default |
| TXA1-BR34 | Tax names are unique per usage, scope and country across the company tree | tax create or rename | VDR-TXA1-C010 | Constraint |
| TXA1-BR35 | A cash-basis tax needs a reconcilable transition account; the company switch cannot be disabled while one exists | on_payment tax | VDR-TXA1-C012 VDR-TXA1-C182 VDR-TXA1-C175 | Constraint |
| TXA1-BR36 | Customer lines default to product sales taxes else account sale taxes; vendor lines symmetric; then company filter and fiscal position mapping | line tax recompute | VDR-TXA1-C135 VDR-TXA1-C136 VDR-TXA1-C138 VDR-TXA1-C134 | Default |
| TXA1-BR37 | Order lines take product taxes only (no account taxes), mapped by the order's fiscal position | sale or purchase order line | VDR-TXA1-C218 VDR-TXA1-C220 VDR-TXA1-C230 | Default |
| TXA1-BR38 | The company default sale and purchase taxes seed new products; line-level defaults do not read them | product creation | VDR-TXA1-C172 VDR-TXA1-C145 VDR-TXA1-C146 VDR-TXA1-C139 | Default |
| TXA1-BR39 | Quick encoding falls back to journal-account taxes, then company default tax | quick encoding mode | VDR-TXA1-C291 VDR-TXA1-C130 | Default |
| TXA1-BR40 | Combo products carry no taxes | product type combo | VDR-TXA1-C149 VDR-TXA1-C218 | Default |
| TXA1-BR41 | Order taxes travel unchanged to invoice lines with engine data | invoice from order | VDR-TXA1-C225 VDR-TXA1-C224 | Calculation |
| TXA1-BR42 | Order-line taxes are limited to sale-type taxes of the order's tax country | sale order line | VDR-TXA1-C219 VDR-TXA1-C214 | Constraint |
| TXA1-BR43 | A document may not keep taxes of another country than its tax country | post or edit document | VDR-TXA1-C126 VDR-TXA1-C113 | Constraint |
| TXA1-BR44 | Fiscal position resolution order: partner, delivery address, manual position, country, automatic candidates with tests | document partner or address change | VDR-TXA1-C161 VDR-TXA1-C159 VDR-TXA1-C160 | Calculation |
| TXA1-BR45 | A fiscal position replaces taxes by listed replacements and swaps accounts by mapping; no position leaves taxes unchanged | position present | VDR-TXA1-C157 VDR-TXA1-C158 VDR-TXA1-C156 | Calculation |
| TXA1-BR46 | When mapped taxes are price-included the unit price is adapted symmetrically | fiscal position maps included taxes | VDR-TXA1-C037 VDR-TXA1-C154 VDR-TXA1-C092 | Calculation |
| TXA1-BR47 | Foreign tax IDs on positions need country, state within fiscal country, and are unique per country | foreign VAT position | VDR-TXA1-C164 VDR-TXA1-C166 | Constraint |
| TXA1-BR48 | Partner VAT check in the installed set is a stub; VAT presence means set and not a slash | always | VDR-TXA1-C167 VDR-TXA1-C168 | Risk |
| TXA1-BR49 | Vendor-bill lines may be partly deductible (0 to 100); the private share and its taxes go to the journal's private-share account | vendor bill line deductibility below 100 | VDR-TXA1-C123 VDR-TXA1-C124 VDR-TXA1-C119 VDR-TXA1-C118 VDR-TXA1-C125 | Configuration |
| TXA1-BR50 | Totals show non-deductible tax separately | private-share lines present | VDR-TXA1-C076 | Calculation |
| TXA1-BR51 | Receipt cost excludes taxes whose distribution lines have an account and includes taxes without account | purchase receipt valuation | VDR-TXA1-C237 VDR-TXA1-C236 VDR-TXA1-C088 | Calculation |
| TXA1-BR52 | Cost-of-goods entries are untaxed and exist only for real-time valuation products | customer invoice posting, real-time valuation | VDR-TXA1-C322 VDR-TXA1-C240 VDR-TXA1-C242 | Calculation |
| TXA1-BR53 | Foreign-amount base and tax are divided by the line rate to get company amounts; each currency is rounded separately | foreign-currency line | VDR-TXA1-C050 VDR-TXA1-C059 VDR-TXA1-C046 | Calculation |
| TXA1-BR54 | Invoice rate = rate at invoice date (today if empty), refreshable, positive, manual edits protected | invoice or receipt | VDR-TXA1-C201 VDR-TXA1-C202 VDR-TXA1-C203 VDR-TXA1-C204 VDR-TXA1-C128 | Calculation |
| TXA1-BR55 | Orders use their own order-date rate; the invoice created from an order recomputes its rate at invoice date | order to invoice | VDR-TXA1-C215 VDR-TXA1-C234 VDR-TXA1-C224 | Calculation |
| TXA1-BR56 | Rate lookup falls back to earliest rate then 1.0; no installed feed; no rate rows in this database | any conversion | VDR-TXA1-C205 VDR-TXA1-C278 VDR-TXA1-C209 | Risk |
| TXA1-BR57 | Rates and cash-basis switch live on the root company; branches share them | company tree | VDR-TXA1-C206 VDR-TXA1-C176 | Constraint |
| TXA1-BR58 | Foreign sale documents may show tax in company currency (company flag on by default) | foreign-currency sale document | VDR-TXA1-C112 VDR-TXA1-C173 | Configuration |
| TXA1-BR59 | A currency precision cannot be reduced once used in entries | currency maintenance | VDR-TXA1-C210 | Constraint |
| TXA1-BR60 | Taxable supply date has no logic; rate date is the invoice date | always | VDR-TXA1-C267 VDR-TXA1-C122 VDR-TXA1-C201 | Risk |
| TXA1-BR61 | A used tax cannot be deleted and its company cannot change; archiving is not guarded; sales-order-only use does not count | tax maintenance | VDR-TXA1-C093 VDR-TXA1-C016 VDR-TXA1-C326 VDR-TXA1-C302 VDR-TXA1-C300 VDR-TXA1-C301 | Constraint |
| TXA1-BR62 | Chart reload skips changed taxes unless forced; forced reload renames the old tax and creates a new one | chart template reload | VDR-TXA1-C256 VDR-TXA1-C257 | Calculation |
| TXA1-BR63 | Only the accounting administrator role creates, edits or deletes taxes, groups, distribution lines and fiscal positions | always | VDR-TXA1-C271 | Constraint |
| TXA1-BR64 | Tax visibility is limited to the user's allowed companies and their parents | always | VDR-TXA1-C272 VDR-TXA1-C091 | Constraint |
| TXA1-BR65 | Non-sale taxed documents are moved to the first open day under a tax lock; posted taxed lines are protected | tax lock date set | VDR-TXA1-C293 VDR-TXA1-C294 VDR-TXA1-C266 VDR-TXA1-C129 | Constraint |
| TXA1-BR66 | The Thai template recognises all 18 taxes at invoicing, uses only generic engine features and ships no fiscal position | Thai chart loaded | VDR-TXA1-C189 VDR-TXA1-C187 VDR-TXA1-C275 VDR-TXA1-C186 | Configuration |
| TXA1-BR67 | Zero and exempt Thai taxes have no template group and fall to the first withholding group | Thai chart loaded | VDR-TXA1-C200 VDR-TXA1-C192 VDR-TXA1-C195 | Risk |
| TXA1-BR68 | Sale withholding taxes are forced price-excluded; purchase withholding follows the company default | Thai chart loaded | VDR-TXA1-C198 VDR-TXA1-C324 | Risk |
| TXA1-BR69 | Withholding tax is selected manually per line; no payee-driven selection exists | Thai chart loaded | VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C187 | Risk |
| TXA1-BR70 | Without a category code the e-invoice exporter infers exempt for a domestic zero-amount tax | e-invoice export | VDR-TXA1-C297 VDR-TXA1-C299 | Risk |
| TXA1-BR71 | Legal notes of taxes and fiscal positions print on invoices; Thai taxes have none | invoice print | VDR-TXA1-C284 VDR-TXA1-C285 VDR-TXA1-C290 | Configuration |

## REGISTER: Source and Override Map

Format `module:file:line`. Overrides are restricted to the 356 installed modules (dump list); non-installed Community add-ons are listed only where marked NOT installed. A row with 'none' records a negative scan (method names and inheritance grepped across installed modules).

| Concept | Base definition (module:file:line) | Overrides in installed Community modules (module:file:line) | Effective-behaviour condition | Claim-IDs |
|---|---|---|---|---|
| Tax record, constraints and lifecycle | account:models/account_tax.py:71 (class), :232-:275 constraints, :5131 delete guard | account_edi_ubl_cii:models/account_tax.py:5 (adds category and exemption code fields); purchase:models/account_tax.py:17 and hr_expense:models/account_tax.py:17 (used-flag); sale: none (negative); NOT installed: account_tax_python:models/account_tax.py:16 (type selection_add), l10n_account_withholding_tax:models/account_tax.py:13 (flag) | Effective model = account + the three installed extensions | VDR-TXA1-C010 VDR-TXA1-C093 VDR-TXA1-C296 VDR-TXA1-C300 VDR-TXA1-C301 VDR-TXA1-C302 VDR-TXA1-C317 VDR-TXA1-C318 |
| Tax calculation core (_get_tax_details and helpers) | account:models/account_tax.py:1137, :895, :923, :976, :1082-:1135 | No installed override; NOT installed: account_tax_python:models/account_tax.py:116 (_eval_tax_amount_fixed_amount for formula type) | Effective = base only (formula add-on absent) | VDR-TXA1-C028 VDR-TXA1-C020 VDR-TXA1-C021 VDR-TXA1-C022 VDR-TXA1-C317 |
| Base-line and tax-line preparation hooks | account:models/account_tax.py:1591, :1692, :2297, :2315, :2347 | hr_expense:models/account_tax.py:24, :30, :36, :42 (carry the expense reference); no other installed override | Base + expense extension when hr_expense installed | VDR-TXA1-C039 VDR-TXA1-C045 VDR-TXA1-C243 VDR-TXA1-C303 |
| Per-document base-line producers | account:models/account_move.py:1591 (journal item), :1619, :1674, :1708 | sale:models/sale_order_line.py:827; purchase:models/purchase_order_line.py:135; hr_expense:models/hr_expense.py:1738; hr_expense:models/account_move.py:94 (override of the journal-item hook) | Each document type has its own producer; engine shared | VDR-TXA1-C105 VDR-TXA1-C222 VDR-TXA1-C231 VDR-TXA1-C244 VDR-TXA1-C304 |
| Rounding (_round_base_lines_tax_details) and totals (_get_tax_totals_summary) | account:models/account_tax.py:2185, :2727 | No installed override; callers: account:models/account_move.py:1836, sale:models/sale_order.py:801, purchase:models/purchase_order.py:255 | Effective = base only | VDR-TXA1-C057 VDR-TXA1-C071 VDR-TXA1-C111 VDR-TXA1-C216 VDR-TXA1-C232 |
| Tax journal item generation and sync | account:models/account_tax.py:3051 (_prepare_tax_lines); account:models/account_move.py:3287 (_sync_tax_lines) | No installed override of either; hr_expense extends the grouping keys (account_tax.py:36, :42) | Base + expense keys | VDR-TXA1-C079 VDR-TXA1-C114 VDR-TXA1-C303 |
| Non-deductible handling | account:models/account_move.py:1729, :3496; account:models/account_tax.py:1776, :2975 | None in installed modules; client mirror lacks it (account:static/src/helpers/account_tax.js:1152) | account only | VDR-TXA1-C109 VDR-TXA1-C119 VDR-TXA1-C049 VDR-TXA1-C076 VDR-TXA1-C077 VDR-TXA1-C269 |
| Default tax resolution on journal items | account:models/account_move_line.py:955, :964 | None in installed modules | account only | VDR-TXA1-C134 VDR-TXA1-C135 VDR-TXA1-C136 |
| Default tax resolution on sales order lines | sale:models/sale_order_line.py:545 | sale_loyalty:models/sale_order_line.py:35 (reward lines); delivery:models/sale_order.py:211 (delivery line created with taxes); sale_project_stock:models/stock_move.py:44 | sale + loyalty + delivery + project stock | VDR-TXA1-C218 VDR-TXA1-C249 VDR-TXA1-C250 VDR-TXA1-C312 |
| Default tax resolution on purchase order lines | purchase:models/purchase_order_line.py:153 | purchase_requisition:models/purchase.py:50, :85; sale_purchase:models/sale_order_line.py:129; purchase_stock:models/stock_rule.py:342 | purchase + agreements + service resale + replenishment | VDR-TXA1-C230 VDR-TXA1-C309 VDR-TXA1-C311 VDR-TXA1-C310 |
| Default tax on products | account:models/product.py:40, :47, :183 | None (company defaults come from account:models/company.py:126) | account only | VDR-TXA1-C145 VDR-TXA1-C146 VDR-TXA1-C150 VDR-TXA1-C172 |
| Fiscal position finder and mapping | account:models/partner.py:247, :154, :165 | None in installed modules (callers listed in the order modules) | account only | VDR-TXA1-C161 VDR-TXA1-C157 VDR-TXA1-C158 VDR-TXA1-C313 |
| Fiscal position on documents | account:models/account_move.py:1037 | sale:models/sale_order.py:412; purchase:models/purchase_order.py:453 | Each document type resolves its own position | VDR-TXA1-C103 VDR-TXA1-C213 VDR-TXA1-C229 |
| Product accounts (income, expense; stock, production) | account:models/product.py:68 | stock_account:models/product.py:130; mrp_account:models/product.py:10 | account + stock accounting + manufacturing accounting | VDR-TXA1-C148 VDR-TXA1-C308 VDR-TXA1-C307 |
| Company tax fields and settings | account:models/company.py:126, :129, :144, :153, :203, :220, :272; account:models/res_config_settings.py:59 | None in installed modules | account only | VDR-TXA1-C172 VDR-TXA1-C169 VDR-TXA1-C170 VDR-TXA1-C175 VDR-TXA1-C181 |
| VAT-number validation | account:models/partner.py:857 (stub) | NOT installed: base_vat:models/res_partner.py:107 | Stub effective (add-on absent) | VDR-TXA1-C167 VDR-TXA1-C319 |
| Currency conversion and rate lookup | base:models/res_currency.py:120, :273, :284 | account:models/res_currency.py:26 (precision guard); product:models/res_currency.py:18 (pricelist side effect); spreadsheet:models/res_currency.py:7 (not tax related); no rate feed | base + account guard | VDR-TXA1-C205 VDR-TXA1-C207 VDR-TXA1-C210 |
| Invoice currency rate | account:models/account_move.py:1134, :1151, :6095 | None in installed modules | account only | VDR-TXA1-C201 VDR-TXA1-C202 VDR-TXA1-C203 |
| Taxable supply date | account:models/account_move.py:396, :1108 (stub) | None in installed modules (Thai module does not implement it) | Stub effective | VDR-TXA1-C267 VDR-TXA1-C122 |
| Cash rounding | account:models/account_cash_rounding.py:20; account:models/account_tax.py:2917 | None in installed modules | account only | VDR-TXA1-C211 VDR-TXA1-C075 |
| Chart template loading of taxes | account:models/chart_template.py:333, :730 | l10n_th:models/template_th.py:10, :19 (Thai data); sale:models/chart_template.py:8; stock_account:models/account_chart_template.py:27 | account loader + Thai data + two property extensions | VDR-TXA1-C256 VDR-TXA1-C254 VDR-TXA1-C184 VDR-TXA1-C316 VDR-TXA1-C315 |
| Invoice document selection | account:models/account_move.py:7373 | l10n_th:models/account_move.py:7 | Thai fiscal-country companies | VDR-TXA1-C188 VDR-TXA1-C314 |
| Tax cost in stock valuation | purchase_stock:models/purchase_order_line.py:239 (account has no counterpart) | stock_account:models/account_move.py:111; purchase_stock:models/account_invoice.py:85; stock_account:models/account_move_line.py:37 | purchase_stock + stock_account | VDR-TXA1-C237 VDR-TXA1-C322 VDR-TXA1-C242 VDR-TXA1-C239 |
| Client-side calculation mirror | account:static/src/helpers/account_tax.js:244, :1152 | None | web client | VDR-TXA1-C268 VDR-TXA1-C269 VDR-TXA1-C038 |
| E-invoice tax classification | account_edi_ubl_cii:models/account_edi_common.py:405, :396 | account_edi_ubl_cii:models/account_tax.py:5 (fields) | e-invoicing installed | VDR-TXA1-C297 VDR-TXA1-C298 VDR-TXA1-C296 |

## REGISTER: Thai Tax Record Treatment Map

Maps every seeded Thai tax record (restored dump = `l10n_th` data) to the treatment it represents natively and how. No statutory correctness is asserted: every row is `STATUTORY CHECK PENDING (TXS)`. Dump ids are database ids (sequence 1, active, on_invoice, include-in-base false, base-affected true for all 18).

| DB id | Name | Template id | Usage | Percent | Treatment represented | Tax group | Base tags | Tax tag; account | Closing flag | Price-include override | Claim-IDs | Statutory link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7% | tax_input_vat | purchase | 7 | STANDARD-RATED (input) | VAT 7% | 6. Purchase amount that is entitled to deduction | 7. Input tax; 114200 | true | none | VDR-TXA1-C190 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 2 | 7% | tax_output_vat | sale | 7 | STANDARD-RATED (output) | VAT 7% | 1. Sales amount | 5. Output tax; 213200 | true | none | VDR-TXA1-C191 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 3 | 0% | tax_input_vat_0 | purchase | 0 | ZERO-RATED (input) | WHT 1% (fallback) | 6. Purchase amount that is entitled to deduction | 7. Input tax; 114200 (zero item dropped) | true | none | VDR-TXA1-C192 VDR-TXA1-C079 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 4 | 0% | tax_output_vat_0 | sale | 0 | ZERO-RATED (output) | WHT 1% (fallback) | 1. Sales amount and 2. Less sales subject to 0% tax rate | 5. Output tax; 213200 (zero item dropped) | true | none | VDR-TXA1-C193 VDR-TXA1-C079 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 5 | 0% EXEMPT | tax_input_vat_exempted | purchase | 0 | EXEMPT (input); Thai description text also mentions non-claimable input tax | WHT 1% (fallback) | 6. Purchase amount that is entitled to deduction | 7. Input tax; 114200 (zero item dropped) | true | none | VDR-TXA1-C194 VDR-TXA1-C079 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 6 | 0% EXEMPT | tax_output_vat_exempted | sale | 0 | EXEMPT (output) | WHT 1% (fallback) | 1. Sales amount and 3. Less exempted sales | 5. Output tax; 213200 (zero item dropped) | true | none | VDR-TXA1-C195 VDR-TXA1-C079 VDR-TXA1-C200 | STATUTORY CHECK PENDING (TXS) |
| 7 | 1% WH C T | tax_wht_co_1 | purchase | -1 | WITHHOLDING (company payee, rate 1) | WHT 1% | Income PND53 | PND53; 213302 | false | company default | VDR-TXA1-C196 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 8 | 2% WH C A | tax_wht_co_2 | purchase | -2 | WITHHOLDING (company payee, rate 2) | WHT 2% | Income PND53 | PND53; 213302 | false | company default | VDR-TXA1-C196 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 9 | 3% WH C S | tax_wht_co_3 | purchase | -3 | WITHHOLDING (company payee, rate 3) | WHT 3% | Income PND53 | PND53; 213302 | false | company default | VDR-TXA1-C196 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 10 | 5% WH C R | tax_wht_co_5 | purchase | -5 | WITHHOLDING (company payee, rate 5) | WHT 5% | Income PND53 | PND53; 213302 | false | company default | VDR-TXA1-C196 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 11 | 1% WH P T | tax_wht_pers_1 | purchase | -1 | WITHHOLDING (individual payee, rate 1) | WHT 1% | Income PND3 | PND3; 213301 | false | company default | VDR-TXA1-C197 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 12 | 2% WH P A | tax_wht_pers_2 | purchase | -2 | WITHHOLDING (individual payee, rate 2) | WHT 2% | Income PND3 | PND3; 213301 | false | company default | VDR-TXA1-C197 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 13 | 3% WH P S | tax_wht_pers_3 | purchase | -3 | WITHHOLDING (individual payee, rate 3) | WHT 3% | Income PND3 | PND3; 213301 | false | company default | VDR-TXA1-C197 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 14 | 5% WH P R | tax_wht_pers_5 | purchase | -5 | WITHHOLDING (individual payee, rate 5) | WHT 5% | Income PND3 | PND3; 213301 | false | company default | VDR-TXA1-C197 VDR-TXA1-C324 | STATUTORY CHECK PENDING (TXS) |
| 15 | 1% WH T | tax_wht_income_1 | sale | -1 | WITHHOLDING SUFFERED (sale, rate 1) | WHT 1% | none | none; 114300 | false | tax_excluded | VDR-TXA1-C198 | STATUTORY CHECK PENDING (TXS) |
| 16 | 2% WH A | tax_wht_income_2 | sale | -2 | WITHHOLDING SUFFERED (sale, rate 2) | WHT 2% | none | none; 114300 | false | tax_excluded | VDR-TXA1-C198 | STATUTORY CHECK PENDING (TXS) |
| 17 | 3% WH S | tax_wht_income_3 | sale | -3 | WITHHOLDING SUFFERED (sale, rate 3) | WHT 3% | none | none; 114300 | false | tax_excluded | VDR-TXA1-C198 | STATUTORY CHECK PENDING (TXS) |
| 18 | 5% WH R | tax_wht_income_5 | sale | -5 | WITHHOLDING SUFFERED (sale, rate 5) | WHT 5% | none | none; 114300 | false | tax_excluded | VDR-TXA1-C198 | STATUTORY CHECK PENDING (TXS) |

Treatment summary by native mechanism (all rows STATUTORY CHECK PENDING (TXS)):

| Treatment | Records (DB ids) | How represented natively | Claim-IDs |
|---|---|---|---|
| Standard-rated | 1, 2 | Percentage tax 7, VAT group, input/output VAT accounts, base and tax tags, closing flag on | VDR-TXA1-C190 VDR-TXA1-C191 VDR-TXA1-C200 |
| Zero-rated | 3, 4 | Percentage tax 0; zero tax item dropped by the engine; sale base also tagged zero-rated sales; no template group (falls to first withholding group) | VDR-TXA1-C192 VDR-TXA1-C193 VDR-TXA1-C079 VDR-TXA1-C200 |
| Exempt | 5, 6 | Percentage tax 0 named exempt; sale base also tagged exempted sales; purchase shares the ordinary purchase grid tag | VDR-TXA1-C194 VDR-TXA1-C195 VDR-TXA1-C079 |
| Non-deductible | none as a tax record | No Thai record; generic percentage deductibility on vendor-bill lines (private-share account, not set in DB) and cost capitalisation of account-less taxes (none under Thai set); Thai-language description of the purchase exempt record mentions non-claimable input tax (translation text only) | VDR-TXA1-C119 VDR-TXA1-C125 VDR-TXA1-C281 VDR-TXA1-C237 VDR-TXA1-C194 |
| Withholding (purchase) | 7-14 | Negative-percentage taxes -1,-2,-3,-5 per payee type, own group per rate, accounts by return form, recognised at posting, closing flag off, price-include follows company default | VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C324 |
| Withholding suffered (sale) | 15-18 | Negative-percentage sale taxes, price-excluded override, creditable asset account, no tags | VDR-TXA1-C198 |
| Reverse charge | none | Mechanism exists (negative-factor distribution); no Thai record uses it | VDR-TXA1-C030 VDR-TXA1-C067 |
| Cash-basis VAT | none | Mechanism exists; all 18 taxes on_invoice; suspense VAT accounts exist but are referenced by no tax | VDR-TXA1-C009 VDR-TXA1-C282 VDR-TXA1-C186 |

## 13. Native status summary (e)

| Status | Count of catalogue functions |
|---|---|
| NATIVE | 66 |
| PARTIAL | 12 |
| NATIVE GAP / EXTENSION REQUIRED | 5 |
| UNKNOWN | 2 |

Native-gap candidates (statutory need pending TXS validation for each; absence in Community source is not proof that no requirement exists):

- TXA1-F28 Tax closing flag per distribution line and month-end settlement of tax accounts - Candidate: closing entry moving input and output VAT to payable or receivable not present; statutory need pending TXS (also U24 CAP-U24-08). Search done: use_in_tax_closing; NOT PRESENT routine: search = every non-localization module for the flag (readers: account_tax.py and account_move_line_tax_details.py only) Claims VDR-TXA1-C095 VDR-TXA1-C323
- TXA1-F52 Prohibited or non-claimable input VAT as a distinct tax treatment with return-grid exclusion - Candidate; statutory need pending TXS. Search done: NOT PRESENT: search = installed tax records, deductibility fields, tag definitions; only a zero-rate exempt purchase tax and the percentage mechanism exist Claims VDR-TXA1-C194 VDR-TXA1-C119 VDR-TXA1-C283 VDR-TXA1-C336
- TXA1-F55 Choose withholding tax from payee type (company, individual, foreign) - Candidate; foreign payee form has an account but no tax; statutory need pending TXS. Search done: NOT PRESENT: search = fiscal positions (none shipped), partner fields in the Thai module (branch label only), tax selection logic Claims VDR-TXA1-C187 VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C157
- TXA1-F64 Automatic exchange-rate feed - Candidate; foreign-currency Thai transactions need a rate source; statutory rate basis pending TXS. Search done: NOT PRESENT: search = cron rows and installed modules for rate providers (none) Claims VDR-TXA1-C278 VDR-TXA1-C205 VDR-TXA1-C337
- TXA1-F65 Tax-point date for tax and rate (taxable supply date) - Candidate; field exists but has no logic; statutory need pending TXS (topic 5 owner U24/TXS). Search done: _compute_taxable_supply_date stub Claims VDR-TXA1-C267 VDR-TXA1-C122 VDR-TXA1-C201

## 14. Report items

- Claims: 338 (FACT 293, OBSERVATION 21, INFERENCE 16, UNKNOWN 8); neutral statements: 123; capabilities: 9; catalogue functions: 85; business rules: 71; override-map rows: 25; Thai tax records mapped: 18.
- Contradictions with prior evidence: none found against U13 and U24 (spot re-verified: tax engine order, rounding, repartition, zero-line drop, fiscal position finder, default taxes, Thai tax rows and accounts). Deltas, not contradictions: (a) U24 left RT whether zero tax lines persist; source drops zero items (U13 C047 already stated it; here VDR-TXA1-C079); (b) U13 stated product/account default taxes; this unit adds that order lines read product taxes only (VDR-TXA1-C220) and that quick encoding is the only path reading the company default tax (VDR-TXA1-C291); (c) U24 describes base_vat in its Thai scope while the dump does not install it (VDR-TXA1-C319), consistent with U23.
- Anomalies noted (not contradictions): company rounding value `round_globally` is labelled 'Round per Tax' (VDR-TXA1-C169); the accounting module imports a table from the VAT-validation module at Python level although that module is not installed (VDR-TXA1-C180); sales-order-only use does not mark a tax as used (VDR-TXA1-C302); Thai template sets the cash-basis company switch while no tax is cash-basis (VDR-TXA1-C186); zero-rated and exempt Thai taxes fall to a withholding tax group (VDR-TXA1-C200).
- RT / AWT list: VDR-TXA1-C331 (numeric VAT plus withholding and rounding), VDR-TXA1-C333 (zero-rate persistence and tags), VDR-TXA1-C334 (order vs invoice rate), VDR-TXA1-C324 (withholding with tax-included default), VDR-TXA1-C224 (invoice rate computed at its own date), VDR-TXA1-C299 (e-invoice classification of Thai zero-rated sales), VDR-TXA1-C338 (deleting a sales-only-used tax; template reload).
- DISCOVERED SUPPORTING MODULES (outside the named set, read only as far as needed): `base_vat` (Python-level import of a VAT format table in `account/models/company.py` and `partner.py`; NOT installed), `hr_expense` (engine hook overrides), `sale_loyalty`, `delivery`, `stock_delivery`, `purchase_requisition`, `sale_purchase`, `sale_project_stock`, `mrp_account` and `stock_account` (product accounts), `account_edi_ubl_cii` (tax category fields), `event_sale` family, `event_product` (display-only use of `compute_all`), `spreadsheet` (currency helper, not tax related); NOT installed Community add-ons read for the map only: `account_tax_python`, `l10n_account_withholding_tax`, `account_update_tax_tags`, `account_debit_note`. Modules absent from the dump and therefore not part of the effective behaviour: `website_sale`, `point_of_sale`, `currency_rate_live` (not present in the source tree).
- Not read / limits: `account_move_line_tax_details.py` beyond the grouping condition; line-by-line `_sync_dynamic_line`, payment/reconcile logic (U11/U12); `account.report` tax-report engine and Thai report XML (U24); EDI builders beyond tax category and validation hooks; JavaScript mirror beyond signatures; stock-valuation postings beyond tax touch points (U10); POS and ecommerce (not installed). Business rules marked Risk are INFERENCE or RT and need runtime confirmation.
- Re-verification: five claims re-read against source before finishing (see the final report of the run).

## 15. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-TXA1-C001 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:84 | amount_type = fields.Selection | FACT | account installed | — | Tax computation type is a required selection of group, fixed, percent, division (percentage tax included); the base module declares no formula/code type | N-TXA1-005 |
| VDR-TXA1-C002 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:81 | type_tax_use | FACT | always | — | Tax usage scope is required selection sale/purchase/none (none = usable only inside a group); default sale | N-TXA1-006 |
| VDR-TXA1-C003 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:83 | tax_scope | FACT | always | — | Optional tax scope service/goods on each tax | N-TXA1-007 |
| VDR-TXA1-C004 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:131 | sequence = fields.Integer(required=True | FACT | always | — | Each tax has a required sequence (default 1) that orders application of taxes | N-TXA1-008 |
| VDR-TXA1-C005 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:148 | include_base_amount | FACT | always | — | Flag 'Affect Base of Subsequent Taxes' (default False): a tax with this flag adds its amount to the base of taxes with a higher sequence that accept it | N-TXA1-011 |
| VDR-TXA1-C006 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:150 | is_base_affected | FACT | always | — | Flag 'Base Affected by Previous Taxes' (default True): allows earlier include-in-base taxes to alter this tax's base | N-TXA1-011 |
| VDR-TXA1-C007 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:142 | price_include_override | FACT | always | — | Per-tax override (tax_included or tax_excluded) of the company default for whether entered prices contain the tax | N-TXA1-068 |
| VDR-TXA1-C008 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:323 | _compute_price_include | FACT | always | — | Effective price-included flag = tax override equals included, or (company default is included and no override) | N-TXA1-068 |
| VDR-TXA1-C009 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility | FACT | always | — | Tax exigibility selection on_invoice (default) or on_payment (cash basis) | N-TXA1-036 |
| VDR-TXA1-C010 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:232 | _constrains_name | FACT | always | — | Tax names must be unique per usage type, scope and country across the whole company tree (child_of root company); type none excluded | N-TXA1-095 |
| VDR-TXA1-C011 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:264 | tax_group_id.country_id | FACT | always | — | A tax group with a country must have the same country as the tax using it | N-TXA1-095 |
| VDR-TXA1-C012 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:267 | _constrains_cash_basis_transition_account | FACT | always | — | An on_payment tax requires a reconcilable cash-basis transition account (skipped while a chart template loads) | N-TXA1-036 |
| VDR-TXA1-C013 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:304 | _compute_tax_group_id | FACT | always | — | Default tax group is searched by tax country and company, falling back to a company group without country | N-TXA1-035 |
| VDR-TXA1-C014 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:559 | _validate_repartition_lines | FACT | always | — | Repartition constraint: invoice and refund each exactly one base line, same line count, at least one tax line, mirrored type and percent, positive factors total 100, negative factors total -100 if present | N-TXA1-030 |
| VDR-TXA1-C015 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:596 | _check_children_scope | FACT | always | — | Group children: no recursion, scope must equal the group or be none/empty, nested groups forbidden | N-TXA1-035 |
| VDR-TXA1-C016 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:613 | _check_company_consistency | FACT | always | — | Changing a tax's company is refused when journal items already link to the tax | N-TXA1-095 |
| VDR-TXA1-C017 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:709 | onchange_amount | FACT | UI onchange | — | For percent/division taxes with non-zero amount and no label, the invoice label defaults to the formatted percentage | N-TXA1-017 |
| VDR-TXA1-C018 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:720 | onchange_price_include | FACT | UI onchange | — | Setting price-included in the form also sets include_base_amount true | N-TXA1-068 |
| VDR-TXA1-C019 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:788 | product.sudo() | FACT | always | — | Product fields needed by tax evaluation are read as superuser; the base sets of product and unit-of-measure fields are empty (lines 742 and 824), a hook for extensions | N-TXA1-018 |
| VDR-TXA1-C020 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:895 | _flatten_taxes_and_sort_them | FACT | always | — | Group taxes are replaced by their children; result sorted by sequence then id, parent sequence governing the group's position | N-TXA1-009 |
| VDR-TXA1-C021 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:923 | _batch_for_taxes_computation | FACT | always | — | Taxes are batched when same computation type, same price-included flag (unless special mode), same include-base flag and not mutually base-affecting | N-TXA1-010 |
| VDR-TXA1-C022 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:976 | _propagate_extra_taxes_base | FACT | always | — | Per-tax extra base is propagated to other taxes depending on price-included flag, include-base flag, is_base_affected and the special mode | N-TXA1-011 |
| VDR-TXA1-C023 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1093 | self.amount_type == 'fixed' | FACT | amount_type fixed | — | Fixed tax amount = sign of unit price x quantity x amount, independent of price | N-TXA1-012 |
| VDR-TXA1-C024 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1109 | self.amount_type == 'percent' | FACT | price-included percent | — | Price-included percent tax = raw base / (1 + sum of batch percents) x own percent; if batch total is -100% factor is zero | N-TXA1-070 |
| VDR-TXA1-C025 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1114 | self.amount_type == 'division' | FACT | price-included division | — | Price-included division tax = raw base x amount / 100 | N-TXA1-070 |
| VDR-TXA1-C026 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1129 | self.amount_type == 'percent' | FACT | price-excluded percent | — | Price-excluded percent tax = raw base (plus extra base) x amount / 100 | N-TXA1-013 |
| VDR-TXA1-C027 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1132 | self.amount_type == 'division' | FACT | price-excluded division | — | Price-excluded division tax = raw base x amount / 100 / (1 - sum of batch percents), multiplier 1 when batch total is 100% | N-TXA1-014 |
| VDR-TXA1-C028 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1142 | rounding_method='round_per_line' | FACT | always | — | _get_tax_details is the core calculation entry point; default rounding mode when called directly is round per line; optional special mode total_excluded or total_included | N-TXA1-099 |
| VDR-TXA1-C029 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1182 | round_per_line | FACT | rounding_method round_per_line | — | Under round per line each tax amount and the raw base are rounded to the currency precision before use | N-TXA1-020 |
| VDR-TXA1-C030 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1184 | has_negative_factor | FACT | tax has negative repartition factor | — | A tax whose invoice distribution has a negative tax factor produces a mirrored second tax entry (reverse-charge entry) with the opposite amount and is never price-included | N-TXA1-016 |
| VDR-TXA1-C031 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1202 | prepare_tax_extra_data | FACT | always | — | Price-included flag per tax data: forced False for negative-factor taxes; True or False when special mode total_included or total_excluded; else the tax's own flag | N-TXA1-016 |
| VDR-TXA1-C032 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1235 | raw_base = quantity * price_unit | FACT | always | — | Raw base = quantity x unit price, rounded first only for round-per-line | N-TXA1-001 |
| VDR-TXA1-C033 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1256 | eval_tax_amount(tax._eval_tax_amount_fixed_amount | FACT | always | — | Evaluation order: fixed taxes first (descending), then price-included taxes (descending), then price-excluded taxes (ascending) | N-TXA1-008 |
| VDR-TXA1-C034 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1286 | base -= total_tax_amount | FACT | price-included tax, no special mode | — | Base of a price-included tax = raw base plus extra base minus the batch's total tax amount | N-TXA1-070 |
| VDR-TXA1-C035 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1312 | total_excluded = taxes_data_list[0]['base'] | FACT | always | — | Line totals: total excluded = base of the first tax entry, total included = excluded + sum of tax amounts; no taxes means both equal the raw base | N-TXA1-001 |
| VDR-TXA1-C036 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1239 | evaluation_context | FACT | always | — | Evaluation context passed to every tax computation holds product values, unit-of-measure values, price unit, quantity, raw base and special mode | N-TXA1-018 |
| VDR-TXA1-C037 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1342 | _adapt_price_unit_to_another_taxes | FACT | fiscal position maps price-included taxes | — | Price unit is re-derived for replacement taxes only when all original taxes are price-included: strip original taxes, add new price-included tax amounts (symmetrical mapping) | N-TXA1-086 |
| VDR-TXA1-C038 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1151 | Mirror of the same method in account_tax.js | FACT | always | — | The engine methods are documented as mirrored in a JavaScript file; both implementations must stay consistent (client-side previews) | N-TXA1-004 |
| VDR-TXA1-C039 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1591 | _prepare_base_line_for_taxes_computation | FACT | always | — | Any business record (journal item, order line, dict) is converted to a generic base-line dictionary (product, uom, taxes, unit price, quantity, discount, currency, rate, sign, refund flag, partner, account, analytic) before calculation | N-TXA1-002 |
| VDR-TXA1-C040 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1642 | 'special_type' | FACT | always | — | A base line may carry a special type: early_payment, cash_rounding or non_deductible; these select custom behaviour in the engine | N-TXA1-015 |
| VDR-TXA1-C041 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1635 | 'special_mode' | FACT | always | — | A base line may force special mode total_included (all taxes price-included) or total_excluded (all price-excluded) | N-TXA1-001 |
| VDR-TXA1-C042 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1610 | currency = ( | FACT | always | — | Base-line currency falls back from line currency to company currency to company's currency record | N-TXA1-073 |
| VDR-TXA1-C043 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1676 | manual_total_excluded_currency | FACT | always | — | Base lines may carry forced total-excluded and per-tax manual amounts (used for down payments, combo products, global discounts); they are exported and re-imported with a currency/price/quantity consistency test | N-TXA1-024 |
| VDR-TXA1-C044 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1449 | extra_tax_data.get('manual_tax_amounts') | FACT | always | — | Stored manual tax amounts are re-imported only if currency, unit price, discount, quantity and the set of taxes are unchanged; amounts are rescaled by the change of rate | N-TXA1-024 |
| VDR-TXA1-C045 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1692 | _prepare_tax_line_for_taxes_computation | FACT | always | — | Existing tax journal items are converted to a generic tax-line dictionary (repartition line, group tax, taxes, tags, partner, account, analytic, amounts) so the same logic can serve expenses and bank reconciliation | N-TXA1-002 |
| VDR-TXA1-C046 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1737 | _add_tax_details_in_base_line | FACT | always | — | Per base line the engine applies the discount to unit price, runs the core tax calculation and stores raw (unrounded) totals and per-tax base/tax amounts in both document currency and company currency | N-TXA1-108 |
| VDR-TXA1-C047 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1763 | price_unit_after_discount | FACT | always | — | Line discount percent is applied to the unit price before taxes are computed | N-TXA1-027 |
| VDR-TXA1-C048 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1762 | rounding_method or company.tax_calculation_rounding_method | FACT | no explicit method passed | — | Rounding method defaults to the company setting | N-TXA1-020 |
| VDR-TXA1-C049 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1776 | special_type'] == 'non_deductible' | FACT | base line special type non_deductible | — | For non-deductible base lines the reverse-charge tax entries are dropped from the tax data and subtracted from total included | N-TXA1-060 |
| VDR-TXA1-C050 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1788 | / rate if rate else 0.0 | FACT | always | — | Company-currency raw amounts are document-currency amounts divided by the line rate (0 if rate is 0); rounded to company currency only under round-per-line | N-TXA1-105 |
| VDR-TXA1-C051 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1793 | rounding_method == 'round_per_line' | FACT | round per line | — | Round-per-line rounds company-currency totals, tax amounts and base amounts independently with the company currency | N-TXA1-020 |
| VDR-TXA1-C052 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1840 | _distribute_delta_amount_smoothly | FACT | always | — | A rounding delta is distributed in smallest currency units across target amounts in proportion to their factors, largest factor first, then remaining units one each to the biggest | N-TXA1-022 |
| VDR-TXA1-C053 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1897 | _round_tax_details_tax_amounts | FACT | round globally | — | Under global rounding tax amounts are summed per tax, currency, refund flag, reverse-charge flag and price-included flag; the total is rounded once and the delta versus the sum of rounded line amounts is spread over the line tax amounts | N-TXA1-021 |
| VDR-TXA1-C054 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1966 | (mode == 'mixed' and price_include) | FACT | round globally | — | Base rounding in mixed mode: for price-included taxes round base plus tax then derive base by subtraction; for price-excluded taxes round the base independently | N-TXA1-021 |
| VDR-TXA1-C055 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1995 | _round_tax_details_base_lines | FACT | round globally | — | Each line's untaxed total receives a stored delta so the document total of untaxed amounts equals the rounded total of raw amounts; mode chosen 'included' unless any non-zero tax on the line is price-excluded | N-TXA1-021 |
| VDR-TXA1-C056 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2106 | _round_tax_details_tax_amounts_from_tax_lines | FACT | existing tax lines passed in | — | When existing tax journal items are supplied, line tax amounts are re-aligned to those items per tax, currency and refund flag, so manually edited tax amounts are kept | N-TXA1-023 |
| VDR-TXA1-C057 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2185 | _round_base_lines_tax_details | FACT | always | — | Rounding entry point: raw amounts rounded per currency, manual amounts applied, total included computed, then global tax-amount, base-amount and tax-line alignment steps; raw unrounded amounts are kept for e-invoicing | N-TXA1-100 |
| VDR-TXA1-C058 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2265 | if base_line[manual_field] is not None | FACT | manual amounts set | — | Forced total-excluded and per-tax base and tax amounts override computed values in document currency and are converted to company currency by the line rate | N-TXA1-024 |
| VDR-TXA1-C059 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2249 | currency.round(tax_details[f'raw_{total_excluded_field}']) | FACT | always | — | Rounding is performed separately in the document currency and the company currency, never one derived from the other except for manual amounts | N-TXA1-073 |
| VDR-TXA1-C060 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2306 | 'partner_id': base_line['partner_id'].id | FACT | always | — | Tax journal items are grouped by partner, currency, analytic distribution, base account and the set of line taxes, then by repartition line and group tax | N-TXA1-032 |
| VDR-TXA1-C061 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2335 | 'analytic_distribution': ( | FACT | always | — | A tax journal item inherits the line's analytic distribution only if the tax is flagged 'include in analytic cost' or its repartition line is not used in tax closing | N-TXA1-034 |
| VDR-TXA1-C062 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2340 | 'account_id': tax_rep_data['account'].id | FACT | always | — | Tax journal item account is the repartition-line account, falling back to the base line's account when the distribution line has none | N-TXA1-030 |
| VDR-TXA1-C063 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2342 | 'tax_tag_ids': [Command.set(tax_rep_data['tax_tags'].ids)] | FACT | always | — | Tax journal items carry the repartition tags (only when tax is on_invoice or cash-basis tags requested) plus tags inherited from the product and from preceding include-base taxes | N-TXA1-031 |
| VDR-TXA1-C064 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2393 | repartition_lines_field = 'refund_repartition_line_ids' | FACT | line is refund | — | Refund lines use the refund distribution lines; invoice lines use the invoice distribution lines | N-TXA1-030 |
| VDR-TXA1-C065 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2405 | product.sudo().account_tag_ids | FACT | line has a product | — | Account tags stored on the product are added to the base line tags and to each tax journal item's tags | N-TXA1-031 |
| VDR-TXA1-C066 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2412 | not tax_data['is_reverse_charge'] | FACT | always | — | Base line tags come from the base distribution line of each tax that is on_invoice (or when cash-basis tags requested); reverse-charge entries add no base tags | N-TXA1-031 |
| VDR-TXA1-C067 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2417 | x.factor < 0.0 | FACT | reverse-charge entry | — | For a reverse-charge entry the negative-factor tax distribution lines are used with sign -1; normal entries use non-negative factors | N-TXA1-016 |
| VDR-TXA1-C068 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2436 | tax_amount_currency * tax_rep.factor * tax_rep_sign | FACT | always | — | Each distribution line gets tax amount x its factor, rounded in document and company currency; leftover rounding difference is spread over the distribution lines | N-TXA1-030 |
| VDR-TXA1-C069 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2486 | tax.include_base_amount | FACT | tax includes base for later taxes | — | A tax that affects the base of later taxes also inherits the base-distribution tags of those later taxes | N-TXA1-031 |
| VDR-TXA1-C070 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2484 | include_caba_tags or tax.tax_exigibility == 'on_invoice' | FACT | always | — | Tags on tax lines are attached at document level only for on_invoice taxes; cash-basis taxes get their tags at payment time (U12 hand-off) | N-TXA1-036 |
| VDR-TXA1-C071 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2727 | _get_tax_totals_summary | FACT | always | — | Document totals summary: untaxed base, tax amount and total in document and company currency, grouped by tax group and subtotal label, from already rounded base-line tax details | N-TXA1-025 |
| VDR-TXA1-C072 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2828 | sorted_total_per_tax_group | FACT | always | — | Tax groups are shown ordered by group sequence; a group's preceding-subtotal label starts a new subtotal, default label is Untaxed Amount | N-TXA1-025 |
| VDR-TXA1-C073 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2845 | set(involved_taxes.mapped('amount_type')) == {'fixed'} | FACT | always | — | Displayed base per tax group is blank for groups with only fixed taxes and adjusted for groups with only price-included division taxes | N-TXA1-025 |
| VDR-TXA1-C074 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2972 | same_tax_base | FACT | always | — | A same-tax-base flag tells the view whether all tax groups share the same base, so the base need not be repeated | N-TXA1-025 |
| VDR-TXA1-C075 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2917 | elif cash_rounding | FACT | cash rounding configured | — | Cash rounding in the totals adds a delta either as an extra untaxed amount (add invoice line strategy) or to the largest tax group (biggest tax strategy; not applied when there is no tax) | N-TXA1-026 |
| VDR-TXA1-C076 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2975 | taxed_non_deductible_lines | FACT | document has non-deductible base lines with taxes | — | Taxes on non-deductible lines are reported per tax group as a separate non-deductible tax amount and removed from the group's regular tax and base amounts and from the document tax total | N-TXA1-061 |
| VDR-TXA1-C077 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2974 | not implemented in the JS-part | FACT | always | — | The non-deductible handling in totals exists only in the server-side implementation, not in the mirrored client-side one | N-TXA1-061 |
| VDR-TXA1-C078 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3010 | _exclude_tax_groups_from_tax_totals_summary | INFERENCE | called by localizations | — | Helper folds selected tax groups into the base amount for presentation (docstring: used in some localizations); a grep over the 356 installed modules found no caller, so it is inactive in this installation | N-TXA1-025 |
| VDR-TXA1-C079 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3115 | Remove tax lines having a zero amount | FACT | always | — | Tax journal items whose amount is zero in both currencies are dropped unless the grouping key carries the keep-zero flag (which the base grouping key sets to False) | N-TXA1-033 |
| VDR-TXA1-C080 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3101 | 'amount_currency': sign * (tax_details['total_excluded_currency'] | FACT | always | — | Base journal items receive tax tags and their amounts = sign x (untaxed total + rounding delta), in both currencies | N-TXA1-032 |
| VDR-TXA1-C081 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3111 | tax_line['tax_base_amount'] += sign * tax_data['base_amount'] | FACT | always | — | Each tax journal item accumulates its base amount, document-currency amount and company-currency balance across base lines with equal grouping key | N-TXA1-032 |
| VDR-TXA1-C082 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3130 | for tax_line in tax_lines or [] | FACT | existing tax lines supplied | — | Existing tax items matching a new grouping key are updated, non-matching are deleted and new keys are created | N-TXA1-110 |
| VDR-TXA1-C083 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3110 | tax_line['name'] = base_line.get | FACT | always | — | Tax journal item description is the tax name unless a manual tax line name is supplied | N-TXA1-032 |
| VDR-TXA1-C084 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3159 | return self.amount_type not in ('fixed', 'code') | FACT | always | — | Fixed taxes are not affected by discounts (and the code type, which this study found only in a non-installed module) | N-TXA1-012 |
| VDR-TXA1-C085 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4975 | def compute_all | FACT | always | — | Legacy compute_all(price, currency, quantity, product, partner, is_refund, ...) is a thin wrapper that builds one base line and calls the new engine; result lists per distribution line the amount, base, account, analytic, tags, exigibility | N-TXA1-003 |
| VDR-TXA1-C086 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5029 | force_price_include | FACT | context key set | — | A context key forces all taxes to be treated as price-included or price-excluded for a single computation | N-TXA1-003 |
| VDR-TXA1-C087 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5031 | not handle_price_include | FACT | handle_price_include False | — | When price-include handling is switched off every tax is treated as price-excluded on the given amount | N-TXA1-003 |
| VDR-TXA1-C088 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5078 | if not rep_line.account_id | FACT | always | — | compute_all reports a total_void that adds tax amounts of distribution lines without an account | N-TXA1-003 |
| VDR-TXA1-C089 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5081 | round_base | FACT | always | — | compute_all rounds total excluded and included to the currency unless the round_base context is false; per-tax amounts stay raw | N-TXA1-003 |
| VDR-TXA1-C090 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5025 | _accessible_branches | FACT | always | — | compute_all selects the first accessible branch (or the tax company) to get rounding method and currency | N-TXA1-090 |
| VDR-TXA1-C091 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5093 | _filter_taxes_by_company | FACT | always | — | Taxes are filtered by company walking up from the document company to its parents until at least one tax matches | N-TXA1-090 |
| VDR-TXA1-C092 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5106 | _fix_tax_included_price | FACT | product default taxes differ from line taxes | — | When a product's price-included tax is not among the line's taxes, the included tax amount is stripped from the price (total excluded of those taxes) | N-TXA1-086 |
| VDR-TXA1-C093 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5131 | unlink_except_tax_used | FACT | always | — | A tax used on journal items or reconcile models cannot be deleted; archiving is the alternative | N-TXA1-107 |
| VDR-TXA1-C094 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5321 | factor_percent = fields.Float( | FACT | always | — | Distribution line carries a percentage factor (default 100, 12-digit precision), base-or-tax basis, document type, account, tax grid tags, sequence and a closing flag | N-TXA1-101 |
| VDR-TXA1-C095 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5355 | _compute_use_in_tax_closing | FACT | always | — | Closing flag defaults true only for tax-type distribution lines whose account exists and is not an income or expense account | N-TXA1-038 |
| VDR-TXA1-C096 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5373 | _get_aml_target_tax_account | FACT | always | — | Target account for a tax line is the distribution-line account, or the cash-basis transition account for an on_payment tax unless suppressed by context | N-TXA1-036 |
| VDR-TXA1-C097 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5351 | allowed_country_ids | FACT | always | — | Selectable tax grids on a distribution line are limited to tags without country, the company's fiscal country, or its foreign-VAT countries | N-TXA1-031 |
| VDR-TXA1-C098 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5333 | 'off_balance' | FACT | always | — | The selectable account of a distribution line (field domain) excludes receivable, payable and off-balance accounts | N-TXA1-030 |
| VDR-TXA1-C099 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3955 | _prepare_global_discount_lines | FACT | always | — | Engine supports global discount lines (percentage or fixed) whose tax amounts are dispatched across the discounted lines per tax, skipping non-discountable taxes | N-TXA1-027 |
| VDR-TXA1-C100 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4020 | _prepare_down_payment_lines | FACT | always | — | Engine supports down-payment lines (percentage or fixed) whose base and tax are dispatched across the original lines' taxes | N-TXA1-028 |
| VDR-TXA1-C101 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4245 | _dispatch_global_discount_lines | FACT | always | — | Existing global-discount lines in a document are dispatched across other lines under their taxes so tax totals stay exact | N-TXA1-027 |
| VDR-TXA1-C102 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4334 | _dispatch_return_of_merchandise_lines | FACT | always | — | A negative-quantity line exactly matching a positive line (return of merchandise) is dispatched onto it for tax computation | N-TXA1-027 |
| VDR-TXA1-C103 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1037 | _compute_fiscal_position_id | FACT | always | — | A document's fiscal position is recomputed when partner, delivery address, company or type change: purchase receipts use the company's receipt fiscal position, otherwise the generic fiscal-position finder is called with partner and delivery address | N-TXA1-115 |
| VDR-TXA1-C104 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1199 | line.display_type in ('tax', 'non_deductible_tax') | FACT | invoices and receipts | — | Document untaxed, tax and total amounts are summed from tax lines (including non-deductible tax and rounding lines linked to a tax) and from product, rounding and non-deductible product lines | N-TXA1-025 |
| VDR-TXA1-C105 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1591 | _prepare_product_base_line_for_taxes_computation | FACT | always | — | Each product line becomes a base line: invoices use unit price, quantity, discount and invoice currency rate with normal price-include handling; non-invoice entries treat the amount as price-excluded | N-TXA1-002 |
| VDR-TXA1-C106 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1586 | _get_product_base_line_currency_rate | FACT | always | — | The rate used for tax amounts on invoices is the document's stored invoice currency rate; on other entries it is derived from the line's own amount-in-currency over balance | N-TXA1-075 |
| VDR-TXA1-C107 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1619 | _prepare_epd_base_line_for_taxes_computation | FACT | payment term with early discount | — | Early-payment discount lines are base lines of special type early payment with price-excluded mode, so the discount reduces the tax amount without touching the untaxed amount (mixed mode) | N-TXA1-029 |
| VDR-TXA1-C108 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1674 | _prepare_cash_rounding_base_line_for_taxes_computation | FACT | cash rounding line present | — | A cash-rounding invoice line is converted to a base line of special type cash rounding in price-excluded mode | N-TXA1-026 |
| VDR-TXA1-C109 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1729 | _prepare_non_deductible_base_lines_for_taxes_computation_from_base_lines | FACT | vendor bill line with deductibility below 100 | — | Non-deductible base lines are anticipated for draft vendor-bill lines whose deductible percent is not 100: base = subtotal x (1 - deductible%), carrying the line's non-fixed taxes | N-TXA1-060 |
| VDR-TXA1-C110 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1778 | _get_rounded_base_and_tax_lines | FACT | always | — | Rounded base lines and tax lines of a document include product, early-payment, cash-rounding and non-deductible lines; existing tax amounts can be kept (round-from-tax-lines) or recomputed | N-TXA1-023 |
| VDR-TXA1-C111 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1836 | _compute_tax_totals | FACT | invoices and receipts | — | Document tax totals are computed from rounded base lines with the invoice's cash rounding setting; non-invoice entries have no tax totals | N-TXA1-025 |
| VDR-TXA1-C112 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1849 | display_in_company_currency | FACT | sale document in foreign currency with company flag | — | Tax totals are flagged to display tax amounts in company currency only for sale documents whose currency differs from the company currency and having tax groups, when the company flag is on | N-TXA1-074 |
| VDR-TXA1-C113 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1944 | _compute_tax_country_id | FACT | always | — | Document tax country = fiscal position's country if the position is a foreign-VAT position, otherwise the company's fiscal country | N-TXA1-088 |
| VDR-TXA1-C114 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3287 | _sync_tax_lines | FACT | draft documents | — | Tax and base lines are re-synchronised only for draft documents when base line amounts, taxes, partner, currency, type or rate change; decision whether to keep manual tax amounts depends on what changed | N-TXA1-032 |
| VDR-TXA1-C115 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3410 | 'reapply_currency_rate' | FACT | invoice rate changed | — | Changing only the invoice currency rate keeps foreign-currency tax amounts and re-derives company-currency balances from the new rate | N-TXA1-109 |
| VDR-TXA1-C116 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3375 | field_has_changed(moves_values_before, move, 'currency_id') | FACT | currency or move type change | — | Changing document currency or switching to refund discards manual tax amounts and recomputes all tax lines | N-TXA1-109 |
| VDR-TXA1-C117 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3417 | include_caba_tags=move.always_tax_exigible | INFERENCE | always | — | Tax tags for cash-basis taxes are requested at document level only when the entry is flagged always tax-exigible, which by lines 1013-1020 is true for a non-invoice entry without cash-basis lines | N-TXA1-036 |
| VDR-TXA1-C118 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3448 | 'display_type': 'non_deductible_tax' | FACT | non-deductible lines with taxes | — | A single non-deductible tax line is created per document with the sum of taxes on private-part base lines, booked on the purchase journal's private-share account or its default account | N-TXA1-060 |
| VDR-TXA1-C119 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3559 | 'display_type': 'non_deductible_product' | FACT | draft vendor bill with line deductibility below 100 | — | For each partly deductible vendor-bill line a non-deductible product line is created with the private share of the subtotal on the same account, plus one total line on the journal's private-share account | N-TXA1-104 |
| VDR-TXA1-C120 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5767 | non_deductible_lines := self.line_ids.filtered | FACT | posting a bill with private-part lines | — | At posting the private-part total and tax lines are renamed with the document number for audit | N-TXA1-113 |
| VDR-TXA1-C121 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5763 | group_partial_purchase_deductibility | FACT | posting a vendor bill with deductibility other than 100 | — | Posting such a bill automatically adds the posting user to the partial-purchase-deductibility group that reveals the per-line deductibility column | N-TXA1-062 |
| VDR-TXA1-C122 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1108 | _compute_taxable_supply_date | FACT | account installed | — | The taxable-supply-date compute in the accounting module is a no-op stub and its show flag is false; localization modules may implement it | N-TXA1-079 |
| VDR-TXA1-C123 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:422 | deductible_amount = fields.Float | FACT | always | — | Journal item has a deductibility percentage (default 100) | N-TXA1-060 |
| VDR-TXA1-C124 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1612 | _constrains_deductible_amount | FACT | always | — | Deductibility below 100 is allowed only on vendor documents and must be between 0 and 100 | N-TXA1-060 |
| VDR-TXA1-C125 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:137 | non_deductible_account_id | FACT | always | — | Journal field 'private share account' holds the account that registers the private part of mixed expenses (visible on purchase journals) | N-TXA1-063 |
| VDR-TXA1-C126 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2858 | _validate_taxes_country | FACT | always | — | A document may not keep taxes whose country differs from its tax country (company fiscal country or foreign-VAT position country); otherwise an error is raised | N-TXA1-088 |
| VDR-TXA1-C127 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2548 | _inverse_tax_totals | FACT | user edits tax totals widget | — | Editing the tax amount of a tax group in the totals widget rewrites the first tax line of that group by the difference, then recomputes document amounts | N-TXA1-023 |
| VDR-TXA1-C128 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2872 | _check_invoice_currency_rate | FACT | foreign-currency invoice | — | An invoice whose currency differs from the company currency must have a strictly positive currency rate | N-TXA1-075 |
| VDR-TXA1-C129 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5315 | _affect_tax_report | FACT | always | — | A document 'affects the tax report' if any line has taxes, is a tax line or carries tax-applicability tags; this drives the tax lock date message and checks | N-TXA1-098 |
| VDR-TXA1-C130 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4419 | _get_frequent_account_and_taxes | FACT | partner set on quick-encode | — | Quick-encode suggests the partner's most frequent account and tax combination from the last two years, filtered by income (customer) or expense (vendor) accounts | N-TXA1-043 |
| VDR-TXA1-C131 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:195 | tax_ids = fields.Many2many( | FACT | always | — | Journal item taxes are a stored, computed and editable many-to-many to taxes, tracked in the audit trail | N-TXA1-040 |
| VDR-TXA1-C132 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:243 | extra_tax_data = fields.Json() | FACT | always | — | Journal item stores technical engine data (manual amounts, computation key) in a JSON field | N-TXA1-024 |
| VDR-TXA1-C133 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:212 | tax_line_id | FACT | always | — | A tax journal item is identified by its originator tax (via repartition line), tax group and stored base amount | N-TXA1-032 |
| VDR-TXA1-C134 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:955 | _compute_tax_ids | FACT | product or account changes on a line | — | Line taxes are recomputed when product or unit of measure changes; existing taxes are kept when there is no product and no account-level tax | N-TXA1-102 |
| VDR-TXA1-C135 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:971 | filtered_taxes_id = self.product_id.sudo().taxes_id | FACT | sale document line | — | On sale documents line taxes = product sales taxes of the company tree, else sale-type taxes set on the line's account | N-TXA1-040 |
| VDR-TXA1-C136 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:977 | filtered_supplier_taxes_id | FACT | purchase document line | — | On purchase documents line taxes = product vendor taxes of the company tree, else purchase-type taxes on the account | N-TXA1-040 |
| VDR-TXA1-C137 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:985 | skip_computed_taxes | FACT | miscellaneous entry | — | On miscellaneous entries no taxes are defaulted unless a context asks for account default taxes | N-TXA1-040 |
| VDR-TXA1-C138 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:988 | _filter_taxes_by_company | FACT | always | — | Defaulted taxes are narrowed to the line's company hierarchy, then mapped by the document's fiscal position | N-TXA1-040 |
| VDR-TXA1-C139 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:967 | company_domain = self.env['account.tax']._check_company_domain | INFERENCE | always | — | The line-level default does not read the company's default sale or purchase tax fields; defaults come only from product and account (lines 971-979), so company defaults act through product creation (see product claims) | N-TXA1-040 |
| VDR-TXA1-C140 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:916 | _compute_totals | FACT | always | — | Line subtotal and total are computed through the engine on the single line (for draft preview) in document currency | N-TXA1-025 |
| VDR-TXA1-C141 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:935 | _compute_price_unit | FACT | product set on a line | — | Unit price defaults to the product's tax-included or excluded price helper for the document type, company, currency, date, fiscal position and unit | N-TXA1-071 |
| VDR-TXA1-C142 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:759 | line.move_id.is_invoice(include_receipts=True) | FACT | always | — | Line currency rate on invoices equals the document invoice currency rate; on other entries it is looked up at invoice or entry date | N-TXA1-075 |
| VDR-TXA1-C143 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:780 | line.currency_id.round(line.balance * line.currency_rate) | FACT | always | — | Amount in currency defaults to balance x rate rounded to the line currency | N-TXA1-073 |
| VDR-TXA1-C144 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:41 | early_pay_discount_computation | FACT | payment term with early discount | — | Early-payment discount tax treatment is selectable: reduce tax on early payment, never, or always (upon invoice) | N-TXA1-029 |
| VDR-TXA1-C145 | FUNCTION MAPPING REQUIRED | account/models/product.py:40 | taxes_id = fields.Many2many | FACT | account installed | — | Product template carries a sales tax set (domain: sale-type taxes) defaulting to the user's company default sale tax (or root company's) | N-TXA1-045 |
| VDR-TXA1-C146 | FUNCTION MAPPING REQUIRED | account/models/product.py:47 | supplier_taxes_id | FACT | account installed | — | Product template carries a purchase tax set (domain: purchase-type taxes) defaulting to the company default purchase tax (or root company's) | N-TXA1-045 |
| VDR-TXA1-C147 | FUNCTION MAPPING REQUIRED | account/models/product.py:61 | account_tag_ids = fields.Many2many | FACT | always | — | Product may carry account tags (applicability products) applied to the base and tax journal items created for it | N-TXA1-031 |
| VDR-TXA1-C148 | FUNCTION MAPPING REQUIRED | account/models/product.py:68 | _get_product_accounts | FACT | always | — | Product income and expense accounts come from the product, else the category hierarchy, else the company's default income/expense account; the document fiscal position then maps the account | N-TXA1-046 |
| VDR-TXA1-C149 | FUNCTION MAPPING REQUIRED | account/models/product.py:152 | _onchange_type | FACT | product type set to combo | — | Selecting product type combo clears both the sales and purchase taxes on the product | N-TXA1-045 |
| VDR-TXA1-C150 | FUNCTION MAPPING REQUIRED | account/models/product.py:183 | def create(self, vals_list) | FACT | product created without company | — | A product created without a company also receives the default taxes of the companies not in the creating user's scope, so it works in every company | N-TXA1-045 |
| VDR-TXA1-C151 | FUNCTION MAPPING REQUIRED | account/models/product.py:195 | _get_list_price | FACT | product has sales taxes | — | Public price to list price conversion strips or keeps tax depending on whether the product's tax is configured as price-included | N-TXA1-072 |
| VDR-TXA1-C152 | FUNCTION MAPPING REQUIRED | account/models/product.py:113 | _construct_tax_string | FACT | always | — | Product form shows computed 'incl. taxes' and 'excl. taxes' amounts from the engine on the list price | N-TXA1-072 |
| VDR-TXA1-C153 | FUNCTION MAPPING REQUIRED | account/models/product.py:223 | _get_tax_included_unit_price | FACT | always | — | Shared unit-price helper: sale uses list price, purchase uses standard cost; converts unit of measure, adapts price for the fiscal position's tax mapping, then converts currency at the document date without rounding | N-TXA1-071 |
| VDR-TXA1-C154 | FUNCTION MAPPING REQUIRED | account/models/product.py:290 | _adapt_price_unit_to_another_taxes | FACT | fiscal position maps product taxes | — | Unit price is adapted to mapped taxes via the engine's price-unit adaptation (strip original included taxes, add mapped included taxes) | N-TXA1-086 |
| VDR-TXA1-C155 | FUNCTION MAPPING REQUIRED | account/models/partner.py:43 | tax_ids = fields.Many2many( | FACT | always | — | Fiscal position holds a set of replacement taxes, an account mapping list, an auto-apply flag, a VAT-required flag, country, country group, states, zip range and an optional foreign tax ID | N-TXA1-084 |
| VDR-TXA1-C156 | FUNCTION MAPPING REQUIRED | account/models/partner.py:99 | _compute_tax_map | FACT | always | — | Tax map is built from replacement taxes' 'replaces' lists: each original tax maps to the list of replacement taxes belonging to the position | N-TXA1-083 |
| VDR-TXA1-C157 | FUNCTION MAPPING REQUIRED | account/models/partner.py:154 | def map_tax | FACT | always | — | map_tax returns the taxes unchanged without a position; with a position that has no taxes it drops taxes tied to any position; otherwise each tax is replaced by its mapped taxes, unmapped taxes kept | N-TXA1-083 |
| VDR-TXA1-C158 | FUNCTION MAPPING REQUIRED | account/models/partner.py:165 | def map_account | FACT | always | — | map_account swaps an account for its destination account in the position's account list, unchanged if not mapped | N-TXA1-083 |
| VDR-TXA1-C159 | FUNCTION MAPPING REQUIRED | account/models/partner.py:208 | _get_first_matching_fpos | FACT | auto positions exist | — | Among auto-apply positions the first match wins, company-specific before parent-company positions, then by sequence | N-TXA1-081 |
| VDR-TXA1-C160 | FUNCTION MAPPING REQUIRED | account/models/partner.py:215 | _get_fpos_validation_functions | FACT | always | — | A position matches the delivery partner when VAT requirement, zip range, state, country and country group tests all pass | N-TXA1-081 |
| VDR-TXA1-C161 | FUNCTION MAPPING REQUIRED | account/models/partner.py:247 | def _get_fiscal_position | FACT | always | — | Finder order: no partner gives none; delivery address defaults to partner (and for same-prefix EU VAT both); manual position on delivery or partner wins; no country gives none; else first matching auto position | N-TXA1-106 |
| VDR-TXA1-C162 | FUNCTION MAPPING REQUIRED | account/models/partner.py:555 | property_account_position_id | FACT | always | — | Partner has a company-dependent manual fiscal position field | N-TXA1-081 |
| VDR-TXA1-C163 | FUNCTION MAPPING REQUIRED | account/models/partner.py:113 | _check_zip | FACT | always | — | Zip range requires both bounds with 'to' not below 'from' | N-TXA1-084 |
| VDR-TXA1-C164 | FUNCTION MAPPING REQUIRED | account/models/partner.py:119 | _validate_foreign_vat_country | FACT | foreign tax ID set | — | A foreign tax ID needs a country, a state within the fiscal country, a country in the chosen group and is unique per country | N-TXA1-084 |
| VDR-TXA1-C165 | FUNCTION MAPPING REQUIRED | account/models/partner.py:328 | _account_src_dest_uniq | FACT | always | — | Account mapping is unique per position and source/destination pair | N-TXA1-084 |
| VDR-TXA1-C166 | FUNCTION MAPPING REQUIRED | account/models/partner.py:298 | action_create_foreign_taxes | FACT | user is administrator or accounting manager | — | Creating foreign taxes for a foreign-country position may install that country's localization module and instantiate its taxes (only accounting managers) | N-TXA1-084 |
| VDR-TXA1-C167 | FUNCTION MAPPING REQUIRED | account/models/partner.py:857 | def _run_vat_checks | FACT | account only (no VAT-validation module) | — | In the accounting module the VAT syntax check is a stub returning the number unchanged; real validation requires an extension module | N-TXA1-089 |
| VDR-TXA1-C168 | FUNCTION MAPPING REQUIRED | account/models/partner.py:875 | _get_vat_required_valid | FACT | always | — | A partner counts as having a VAT number when the field is set and not equal to a slash | N-TXA1-081 |
| VDR-TXA1-C169 | FUNCTION MAPPING REQUIRED | account/models/company.py:129 | tax_calculation_rounding_method | FACT | always | — | Company setting 'tax calculation rounding method' with values round_globally (labelled 'Round per Tax') and round_per_line; default round_globally | N-TXA1-020 |
| VDR-TXA1-C170 | FUNCTION MAPPING REQUIRED | account/models/company.py:272 | account_price_include | FACT | always | — | Company default for whether prices include tax: tax_included or tax_excluded, required, default tax_excluded | N-TXA1-068 |
| VDR-TXA1-C171 | FUNCTION MAPPING REQUIRED | account/models/company.py:325 | _check_set_account_price_include | FACT | company has existing accounting | — | The company price-include default cannot be changed once the company has started invoicing | N-TXA1-069 |
| VDR-TXA1-C172 | FUNCTION MAPPING REQUIRED | account/models/company.py:126 | account_sale_tax_id | FACT | always | — | Company has a default sale tax and a default purchase tax (used as default on new products); also a default purchase-receipt fiscal position | N-TXA1-042 |
| VDR-TXA1-C173 | FUNCTION MAPPING REQUIRED | account/models/company.py:153 | display_invoice_tax_company_currency | FACT | always | — | Company flag 'taxes in company currency' defaults to on and controls showing tax amounts in company currency on foreign-currency sale documents | N-TXA1-074 |
| VDR-TXA1-C174 | FUNCTION MAPPING REQUIRED | account/models/company.py:203 | account_fiscal_country_id | FACT | always | — | Company fiscal country (stored, editable) defaults to the company's country and decides which country's taxes, tags and reports apply | N-TXA1-091 |
| VDR-TXA1-C175 | FUNCTION MAPPING REQUIRED | account/models/company.py:220 | tax_exigibility = fields.Boolean | FACT | always | — | Company switch 'use cash basis' (with cash-basis journal and base-tax-received account) unlocks the on_payment option on taxes | N-TXA1-037 |
| VDR-TXA1-C176 | FUNCTION MAPPING REQUIRED | account/models/company.py:316 | 'tax_exigibility' | FACT | always | — | The cash-basis switch and fiscal-year fields are delegated to the root company of a company tree | N-TXA1-090 |
| VDR-TXA1-C177 | FUNCTION MAPPING REQUIRED | account/models/company.py:352 | _compute_domestic_fiscal_position_id | FACT | always | — | Company's domestic fiscal position is computed from its positions matching the company country (or its country group), lowest sequence first | N-TXA1-085 |
| VDR-TXA1-C178 | FUNCTION MAPPING REQUIRED | account/models/company.py:144 | anglo_saxon_accounting | FACT | always | — | Company flag for anglo-saxon accounting (used by stock-valuation postings; off in this installation) | N-TXA1-067 |
| VDR-TXA1-C179 | FUNCTION MAPPING REQUIRED | account/models/company.py:133 | currency_exchange_journal_id | FACT | always | — | Company defines exchange-difference journal and gain and loss accounts for foreign-currency settlements | N-TXA1-077 |
| VDR-TXA1-C180 | FUNCTION MAPPING REQUIRED | account/models/company.py:14 | from odoo.addons.base_vat.models.res_partner import _ref_vat | FACT | always | — | The accounting module imports a VAT-format table from the VAT-validation module at Python level (module not listed as installed in this database; only a placeholder helper) | N-TXA1-089 |
| VDR-TXA1-C181 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:59 | tax_calculation_rounding_method | FACT | always | — | Settings screen exposes default taxes, price-include default, rounding method, cash basis and taxes-in-company-currency, all stored on the company | N-TXA1-091 |
| VDR-TXA1-C182 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:269 | _onchange_tax_exigibility | FACT | always | — | The cash-basis setting cannot be switched off while any tax is on_payment | N-TXA1-037 |
| VDR-TXA1-C183 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:19 | 'auto_install': ['account'] | FACT | l10n_th present | — | Thai localization depends on the EMV-QR module and accounting and auto-installs with accounting; its data are tax-report definitions and an invoice report view, plus the chart template functions | N-TXA1-112 |
| VDR-TXA1-C184 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:10 | @template('th') | FACT | Thai chart selected | — | The Thai template function supplies code digits 6, default receivable, payable, stock valuation and down-payment accounts | N-TXA1-049 |
| VDR-TXA1-C185 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:33 | 'account_sale_tax_id': 'tax_output_vat' | OBSERVATION | Thai chart loaded | — | Company defaults set by the Thai template: default sale tax = standard output VAT, default purchase tax = standard input VAT, fiscal country Thailand, cash-basis switch set to the string 'True' | N-TXA1-049 |
| VDR-TXA1-C186 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | FACT | Thai chart loaded | — | The template turns the company cash-basis switch on (string 'True'); no Thai tax uses on_payment | N-TXA1-037 |
| VDR-TXA1-C187 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:19 | @template('th', 'res.company') | INFERENCE | Thai chart loaded | — | The Thai template defines company, tax, tax-group and account data only; no fiscal position, journal or reconcile-model template function or file exists in the module (module has 5 model files and 4 template csv files) | N-TXA1-049 |
| VDR-TXA1-C188 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:9 | account_fiscal_country_id.code == 'TH' | FACT | company fiscal country Thailand | — | The only accounting override in the Thai module: choose the Thai invoice document layout for invoices of Thai-fiscal-country companies | N-TXA1-057 |
| VDR-TXA1-C189 | FUNCTION MAPPING REQUIRED | l10n_th/models/__init__.py:2 | from . import template_th | INFERENCE | Thai module installed | — | The Thai module has no override of the tax model, tax engine, fiscal position finder, move tax computation or product tax resolution (its models are template, partner branch-name label, move report choice, report action check, bank QR) | N-TXA1-103 |
| VDR-TXA1-C190 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:2 | "tax_input_vat" | OBSERVATION | Thai chart loaded | — | Standard input VAT: purchase tax, percent 7, group VAT 7%, invoice base tagged as purchase amount line 6 and tax tagged line 7, posted to input VAT account 114200, closing flag true | N-TXA1-050 |
| VDR-TXA1-C191 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:6 | "tax_output_vat" | OBSERVATION | Thai chart loaded | — | Standard output VAT: sale tax, percent 7, group VAT 7%, base tagged line 1 (sales amount), tax tagged line 5 posted to output VAT account 213200, closing flag true | N-TXA1-050 |
| VDR-TXA1-C192 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:10 | "tax_input_vat_0" | OBSERVATION | Thai chart loaded | — | Zero-rate input VAT: purchase tax percent 0, no group specified in template (defaults to first Thai tax group), base tagged line 6, tax line to account 114200 | N-TXA1-051 |
| VDR-TXA1-C193 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:14 | "tax_output_vat_0" | OBSERVATION | Thai chart loaded | — | Zero-rate output VAT: sale tax percent 0, base tagged both line 1 and line 2 (sales subject to 0%), tax line to account 213200 (zero amount lines are dropped by the engine) | N-TXA1-051 |
| VDR-TXA1-C194 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:18 | "tax_input_vat_exempted" | OBSERVATION | Thai chart loaded | — | Exempt input VAT: purchase tax percent 0 named '0% EXEMPT', base tagged line 6 (same grid as normal input VAT), tax to 114200; its Thai translation of the description also names non-deductible input tax (translation text only) | N-TXA1-052 |
| VDR-TXA1-C195 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:22 | "tax_output_vat_exempted" | OBSERVATION | Thai chart loaded | — | Exempt output VAT: sale tax percent 0 named '0% EXEMPT', base tagged line 1 and line 3 (exempted sales), tax to 213200 | N-TXA1-052 |
| VDR-TXA1-C196 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | "tax_wht_co_1" | OBSERVATION | Thai chart loaded | — | Purchase-side withholding for company payees: four negative-percent taxes (-1, -2, -3, -5), own group per rate, base tag Income PND53, tax tag PND53, account 213302, closing flag false (rows 26-41) | N-TXA1-053 |
| VDR-TXA1-C197 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:42 | "tax_wht_pers_1" | OBSERVATION | Thai chart loaded | — | Purchase-side withholding for individual payees: four negative-percent taxes (-1, -2, -3, -5), base tag Income PND3, tax tag PND3, account 213301, closing flag false (rows 42-57) | N-TXA1-053 |
| VDR-TXA1-C198 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:58 | "tax_wht_income_1" | OBSERVATION | Thai chart loaded | — | Sale-side withholding suffered: four negative-percent sale taxes, price-include override tax_excluded, no tags, account 114300 (creditable asset), closing flag false (rows 58-73) | N-TXA1-053 |
| VDR-TXA1-C199 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:2 | "tax_group_1" | OBSERVATION | Thai chart loaded | — | Five Thai tax groups: WHT 1%, 2%, 3%, 5% (payable account 213500, receivable account 114401) and VAT 7% (payable 213400, receivable 114400) | N-TXA1-054 |
| VDR-TXA1-C200 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:6 | "tax_group_vat_7" | OBSERVATION | Thai chart loaded | — | The VAT group carries payable 213400 and receivable 114400; zero-rate and exempt taxes (no group in template) fall under the first WHT group via the default group search | N-TXA1-054 |
| VDR-TXA1-C201 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1130 | _get_invoice_currency_rate_date | FACT | always | — | Invoice currency rate date = invoice date, else today; expected rate = conversion rate from company currency to document currency at that date | N-TXA1-075 |
| VDR-TXA1-C202 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1151 | _compute_invoice_currency_rate | FACT | invoice or receipt | — | Stored invoice currency rate is set to the expected rate for invoices and receipts and recomputed when currency, company or invoice date changes; it can be refreshed on demand | N-TXA1-114 |
| VDR-TXA1-C203 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6095 | def refresh_invoice_currency_rate | FACT | user action | — | A refresh action resets the invoice currency rate to the expected rate | N-TXA1-075 |
| VDR-TXA1-C204 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5642 | if not invoice.invoice_date | FACT | posting a sale invoice without invoice date | — | Posting a sale invoice with no invoice date sets it to today and recomputes the rate unless the user edited the rate manually; a vendor bill without date is refused | N-TXA1-075 |
| VDR-TXA1-C205 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | FACT | always | — | Rate lookup uses the latest rate on or before the date, else the earliest rate, else 1.0 when no rate exists for the currency | N-TXA1-076 |
| VDR-TXA1-C206 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:278 | company = (company or self.env.company).root_id | FACT | always | — | Conversion rates are resolved against the root company, so branches share the root company's rates | N-TXA1-090 |
| VDR-TXA1-C207 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:284 | def _convert | FACT | always | — | Conversion multiplies by the conversion rate and rounds to the target currency unless rounding is disabled | N-TXA1-076 |
| VDR-TXA1-C208 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:216 | def round | FACT | always | — | Currency rounding uses the currency's rounding factor (float round), compare and zero tests use the same factor | N-TXA1-078 |
| VDR-TXA1-C209 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:155 | currency.rate = (currency_rates.get(currency.id) or 1.0) | FACT | always | — | Current rate shown for a currency is its rate divided by the base currency rate, defaulting to 1.0 | N-TXA1-076 |
| VDR-TXA1-C210 | FUNCTION MAPPING REQUIRED | account/models/res_currency.py:30 | rounding_val > record.rounding | FACT | always | — | A currency's precision cannot be reduced once used in accounting entries | N-TXA1-078 |
| VDR-TXA1-C211 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:20 | strategy = fields.Selection | FACT | always | — | Cash rounding rule has precision, strategy (add a rounding line or modify the largest tax amount), rounding direction (up, down, nearest), profit and loss accounts (per company) | N-TXA1-026 |
| VDR-TXA1-C212 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:46 | validate_rounding | FACT | always | — | Cash rounding precision must be strictly positive | N-TXA1-026 |
| VDR-TXA1-C213 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:412 | _compute_fiscal_position_id | FACT | sale module installed | — | Sales order fiscal position is recomputed (partner, delivery address, company) via the generic finder; a changed position on an order with lines sets an 'update taxes' prompt | N-TXA1-082 |
| VDR-TXA1-C214 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:768 | _compute_tax_country_id | FACT | sale module installed | — | Sales order tax country = foreign-VAT position's country, else the company fiscal country | N-TXA1-088 |
| VDR-TXA1-C215 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:460 | _compute_currency_rate | FACT | sale module installed | — | Sales order currency rate = conversion rate from company currency to order currency at the order date | N-TXA1-075 |
| VDR-TXA1-C216 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:514 | _compute_amounts | FACT | sale module installed | — | Sales order untaxed, tax and total come from the shared engine and totals summary over order lines plus early-payment base lines | N-TXA1-025 |
| VDR-TXA1-C217 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:531 | _add_base_lines_for_early_payment_discount | FACT | payment term with early discount in mixed mode | — | For mixed-mode early discount the order's taxes are computed on the discounted untaxed amount through paired early-payment base lines | N-TXA1-029 |
| VDR-TXA1-C218 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:545 | _compute_tax_ids | FACT | sale module installed | — | Order line taxes = product sales taxes of the line's company, mapped by the order's fiscal position; none for combo products or lines without product or taxes | N-TXA1-041 |
| VDR-TXA1-C219 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:169 | domain="[('type_tax_use', '=', 'sale'), ('country_id', '=', tax_country_id)]" | FACT | sale module installed | — | Selectable taxes on an order line are limited to sale-type taxes of the order's tax country | N-TXA1-041 |
| VDR-TXA1-C220 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:557 | line.product_id.taxes_id._filter_taxes_by_company(company) | INFERENCE | sale module installed | — | Order line default taxes do not use the account's default taxes: the only source in the method (lines 545-571) is the product's sales taxes | N-TXA1-041 |
| VDR-TXA1-C221 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:622 | _reset_price_unit | FACT | sale module installed | — | Order line unit price is derived from the pricelist display price, adapted to the fiscal position's mapped taxes through the shared product helper | N-TXA1-071 |
| VDR-TXA1-C222 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:827 | _prepare_base_line_for_taxes_computation | FACT | sale module installed | — | Order line becomes a base line with the order's partner, currency and order-date rate; global-discount and down-payment lines get special types | N-TXA1-002 |
| VDR-TXA1-C223 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:855 | _compute_amount | FACT | sale module installed | — | Order line subtotal, total and tax are computed from the engine in order currency | N-TXA1-025 |
| VDR-TXA1-C224 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1439 | 'fiscal_position_id': (self.fiscal_position_id or | INFERENCE | invoice created from order | RT | The invoice receives the order's fiscal position (or finds one for the invoice partner) and currency but no currency rate in the values (lines 1431-1445), so by FX_RATECOMP its rate is computed at invoice date rather than copied from the order | N-TXA1-075 |
| VDR-TXA1-C225 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1553 | 'tax_ids': [Command.set(self.tax_ids.ids)] | FACT | invoice created from order | — | Invoice lines copy the order line's taxes and engine extra data unchanged | N-TXA1-047 |
| VDR-TXA1-C226 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_order_discount.py:147 | _prepare_global_discount_lines | FACT | global discount applied | — | A global (order-level) discount is turned into discount lines per tax set through the engine so tax is reduced proportionally | N-TXA1-027 |
| VDR-TXA1-C227 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:160 | _prepare_down_payment_lines | FACT | down payment invoice | — | Down payment lines are generated through the engine per tax from the order's base lines | N-TXA1-028 |
| VDR-TXA1-C228 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:95 | so_dpl.tax_ids = so_dpl.invoice_lines.tax_ids | FACT | posting a down payment invoice | — | After posting, order down payment lines take the taxes of their invoice lines | N-TXA1-111 |
| VDR-TXA1-C229 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:453 | _get_fiscal_position(self.partner_id) | FACT | purchase module installed | — | Purchase order fiscal position is set on vendor change through the generic finder | N-TXA1-082 |
| VDR-TXA1-C230 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:153 | _compute_tax_id | INFERENCE | purchase module installed | — | Purchase line taxes = product vendor taxes of the line's company mapped by the order's fiscal position; the method (lines 153-159) reads no account taxes | N-TXA1-041 |
| VDR-TXA1-C231 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:135 | _prepare_base_line_for_taxes_computation | FACT | purchase module installed | — | Purchase line becomes a base line using order currency and order-date rate | N-TXA1-002 |
| VDR-TXA1-C232 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:123 | _compute_amount | FACT | purchase module installed | — | Purchase line subtotal, total and tax come from the engine on the line's base line | N-TXA1-025 |
| VDR-TXA1-C233 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:222 | order.amount_total / order.currency_rate | FACT | purchase module installed | — | Purchase order also shows its total converted to company currency (total / order rate) in the totals summary when currencies differ | N-TXA1-074 |
| VDR-TXA1-C234 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:212 | _compute_currency_rate | FACT | purchase module installed | — | Purchase order currency rate = conversion rate company to order currency at order date | N-TXA1-075 |
| VDR-TXA1-C235 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:273 | _compute_tax_country_id | FACT | purchase module installed | — | Purchase order tax country follows foreign-VAT position else company fiscal country | N-TXA1-088 |
| VDR-TXA1-C236 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:507 | _get_gross_price_unit | FACT | purchase module installed | — | Gross unit price helper strips taxes via compute_all total_void (tax-excluded base plus taxes on distribution lines with no account) | N-TXA1-064 |
| VDR-TXA1-C237 | GRV-F04 | purchase_stock/models/purchase_order_line.py:239 | _get_stock_move_price_unit | FACT | purchase_stock installed | — | Stock-move unit price from a purchase line = discounted price with taxes removed through total_void (so taxes whose distribution lines have no account become part of inventory cost), unit converted, then converted to company currency at order date | N-TXA1-064 |
| VDR-TXA1-C238 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order_line.py:316 | _prepare_account_move_line | FACT | purchase_stock installed | — | Vendor-bill line prepared from a purchase line carries an explicit company-currency balance = unrounded total excluded converted without rounding | N-TXA1-065 |
| VDR-TXA1-C239 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move_line.py:37 | _get_gross_unit_price | FACT | stock_account installed | — | Valuation unit price from an invoice line uses unit price x (1 - discount) unless a price-included tax is present, then subtotal / quantity | N-TXA1-066 |
| VDR-TXA1-C240 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move.py:141 | 'tax_ids': [] | FACT | stock_account installed | — | Automatic stock-valuation (COGS) journal items created by the stock accounting module carry no taxes | N-TXA1-067 |
| VDR-TXA1-C241 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move_line.py:20 | fiscal_position = line.move_id.fiscal_position_id | FACT | stock_account installed | — | Valuation accounts for invoice lines are the product accounts mapped by the document's fiscal position | N-TXA1-046 |
| VDR-TXA1-C242 | FUNCTION MAPPING REQUIRED | purchase_stock/models/account_invoice.py:85 | 'tax_ids': [] | FACT | purchase_stock installed with price difference | — | Price-difference journal items created at bill posting carry no taxes | N-TXA1-067 |
| VDR-TXA1-C243 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:24 | _prepare_base_line_for_taxes_computation | FACT | hr_expense installed | — | Expense module extends the tax engine hooks to carry the expense reference through base lines, tax lines and grouping keys, and marks expense-linked taxes as used | N-TXA1-048 |
| VDR-TXA1-C244 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1742 | 'special_mode': 'total_included' | FACT | hr_expense installed | — | Expense amounts are taxed in total-included mode (entered amount is the tax-inclusive total) irrespective of the company price-include setting | N-TXA1-048 |
| VDR-TXA1-C245 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:575 | supplier_taxes_id.filtered_domain | FACT | hr_expense installed | — | Expense taxes default from the product's vendor taxes of the expense company | N-TXA1-048 |
| VDR-TXA1-C246 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:97 | payment_mode == 'own_account' | FACT | hr_expense installed | — | Expense journal items for own-account expenses are forced to total-included mode in the product base line | N-TXA1-048 |
| VDR-TXA1-C247 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:265 | taxes = self.fiscal_position_id.map_tax | FACT | sale_loyalty installed | — | Reward product lines take the product's sales taxes of the company, mapped by the order's fiscal position | N-TXA1-027 |
| VDR-TXA1-C248 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:312 | t.amount_type != 'fixed' | FACT | sale_loyalty installed | — | Discountable amount excludes fixed-type taxes (not discounted) | N-TXA1-012 |
| VDR-TXA1-C249 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:35 | _compute_tax_ids | FACT | sale_loyalty installed | — | Reward lines keep line taxes, filtered by company and mapped by fiscal position, instead of reading product taxes | N-TXA1-027 |
| VDR-TXA1-C250 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order.py:211 | taxes = carrier.product_id.taxes_id | FACT | delivery installed | — | Delivery charge line takes the carrier product's sales taxes of the company, mapped by the order's fiscal position | N-TXA1-041 |
| VDR-TXA1-C251 | FUNCTION MAPPING REQUIRED | delivery/models/delivery_carrier.py:325 | _get_tax_included_unit_price | FACT | delivery installed | — | Carrier-quoted shipping price is adapted to the fiscal position's mapped taxes using the shared unit-price helper | N-TXA1-086 |
| VDR-TXA1-C252 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:209 | dp_account = self.company_id.downpayment_account_id | FACT | down payment invoice | — | The down payment account is the company's down payment account, mapped through the order's fiscal position | N-TXA1-028 |
| VDR-TXA1-C253 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_order_discount.py:164 | 'discount': self.discount_percentage | FACT | per-line discount chosen | — | A per-line discount choice only writes a discount percent on every order line (no discount line is created) | N-TXA1-027 |
| VDR-TXA1-C254 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:730 | Set default Purchase and Sale taxes on the company | FACT | chart template loaded | — | After a chart loads, if the company has no default sale or purchase tax the first matching tax of the company is assigned; products having taxes in another company also receive the new company's default taxes | N-TXA1-042 |
| VDR-TXA1-C255 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:763 | Display caba fields if there are caba taxes | FACT | chart template loaded | — | Loading a chart sets the company cash-basis switch only when a cash-basis tax exists | N-TXA1-037 |
| VDR-TXA1-C256 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:333 | def tax_template_changed | FACT | chart reload | — | On template reload a tax is considered changed when type, amount (4 decimals) or number of distribution lines differ; the old tax is then renamed with an [old] prefix and a new one is created | N-TXA1-096 |
| VDR-TXA1-C257 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:377 | if xmlid not in xmlid2tax or tax_template_changed | FACT | chart reload | — | Unless creation is forced, changed or missing taxes are skipped on reload (not updated), so existing taxes are not silently modified | N-TXA1-096 |
| VDR-TXA1-C258 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:46 | preserve_existing_tags_on_taxes | FACT | module upgrade | — | Helper marks existing tax tags as non-updatable on module upgrade; the Thai module calls it from its post-init hook | N-TXA1-096 |
| VDR-TXA1-C259 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:372 | tax_receivable_account_id | FACT | chart reload | — | Existing tax groups keep user-set payable and receivable accounts on reload | N-TXA1-096 |
| VDR-TXA1-C260 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:92 | tax_ids = fields.Many2many('account.tax' | FACT | always | — | Ledger account has a 'default taxes' set used for journal items booked on that account when no product tax applies; off-balance accounts may not have taxes | N-TXA1-044 |
| VDR-TXA1-C261 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:193 | An Off-Balance account can not have taxes | FACT | always | — | Constraint: off-balance account cannot carry default taxes | N-TXA1-044 |
| VDR-TXA1-C262 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1204 | _compute_is_refund | FACT | always | — | Refund flag (choosing refund versus invoice distribution) is true for credit notes; for miscellaneous entries it follows the tax line's distribution type or, for untaxed lines, the debit/credit direction relative to the tax type (reversed entries invert it) | N-TXA1-030 |
| VDR-TXA1-C263 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1522 | _affect_tax_report | FACT | always | — | A journal item affects the tax report if it has taxes, is a tax line or has tax-applicability tags | N-TXA1-098 |
| VDR-TXA1-C264 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:534 | _create_tax_cash_basis_moves | FACT | on_payment taxes reconciled | — | Cash-basis entries are created on partial reconciliation in the company's cash-basis journal; not exercised by the Thai tax set (all on_invoice) | N-TXA1-036 |
| VDR-TXA1-C265 | FUNCTION MAPPING REQUIRED | account/models/account_move_line_tax_details.py:12 | _get_query_tax_details_from_domain | FACT | always | — | A shared SQL helper maps base journal items to their tax journal items (expanding group taxes into children) for tax reporting | N-TXA1-039 |
| VDR-TXA1-C266 | PCO-F01 | account/models/account_move.py:861 | _compute_date | FACT | invoice or receipt | — | Accounting date of a non-sale invoice moves into the first open period when the tax lock date applies and taxes are involved (has-tax flag is the tax-report-impact test); sale documents keep their accounting date source; the date source helper returns invoice date, else the entry date (lines 858-859) | N-TXA1-098 |
| VDR-TXA1-C267 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:396 | taxable_supply_date = fields.Date( | FACT | always | — | The document has an optional 'taxable supply date' field (stored, editable) whose compute is an empty stub in accounting (see MOV_SUPPLY) and which the accounting-date and currency-rate computes list as a dependency | N-TXA1-079 |
| VDR-TXA1-C268 | FUNCTION MAPPING REQUIRED | account/static/src/helpers/account_tax.js:244 | get_tax_details( | FACT | always | — | Client-side helper library re-implements the tax-detail function (this line), base-line preparation (line 635), per-line details (697), rounding (1051) and totals summary (1152) for previews | N-TXA1-004 |
| VDR-TXA1-C269 | FUNCTION MAPPING REQUIRED | account/static/src/helpers/account_tax.js:1152 | get_tax_totals_summary | INFERENCE | always | — | Client-side totals summary exists at this line; by the server comment at account_tax.py line 2974 the non-deductible part is not implemented client-side | N-TXA1-004 |
| VDR-TXA1-C270 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:554 | move_date = max(partial_values['settlement_date'] | FACT | on_payment taxes reconciled | — | A cash-basis entry is dated on the settlement date but never earlier than the day after the user's fiscal lock date | N-TXA1-036 |
| VDR-TXA1-C271 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:77 | access_account_tax_manager | FACT | account installed | — | Tax records: read for all internal users and accounting roles, create/edit/delete only for the accounting administrator role; the same pattern holds for distribution lines, tax groups (lines 82-89) and fiscal positions (lines 21-24) | N-TXA1-097 |
| VDR-TXA1-C272 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:170 | tax_comp_rule | FACT | account installed | — | Company rules limit taxes and tax groups to the user's allowed companies and their parents; distribution lines also allow records without company; fiscal positions follow the same parent-of rule | N-TXA1-090 |
| VDR-TXA1-C273 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:90 | group_partial_purchase_deductibility | FACT | account installed | — | A dedicated group reveals the partial-deductibility column on vendor bill lines | N-TXA1-062 |
| VDR-TXA1-C274 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:3 | access_account_cash_rounding_uinvoice | FACT | account installed | — | Cash rounding rules are editable by the invoicing role and readable by the read-only accounting role | N-TXA1-097 |
| VDR-TXA1-C275 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:2 | "tax_input_vat" | OBSERVATION | restored DB | — | DB has 18 taxes matching the template (6 VAT, 8 purchase withholding, 4 sale withholding): all percent type, sequence 1, on_invoice, active, base-affected true, none with include-base, analytic or cash-basis transition account; 72 distribution lines (36 invoice, 36 refund) of which 36 are tax lines: 12 flagged for closing (the VAT ones), 24 not (the withholding ones) | N-TXA1-050 |
| VDR-TXA1-C276 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | OBSERVATION | restored DB | — | DB company: chart th, round_globally, tax_excluded, cash-basis switch true, taxes-in-company-currency true, anglo-saxon false, default sale tax = standard output VAT, default purchase tax = standard input VAT, fiscal country Thailand, no domestic fiscal position, no purchase-receipt fiscal position, no tax lock date | N-TXA1-092 |
| VDR-TXA1-C277 | FUNCTION MAPPING REQUIRED | account/models/partner.py:247 | def _get_fiscal_position | OBSERVATION | restored DB | — | DB has zero fiscal positions and zero fiscal position account mappings, zero account default taxes, zero cash-rounding rules; fiscal position detection and tax mapping are therefore not exercised in this installation | N-TXA1-087 |
| VDR-TXA1-C278 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | OBSERVATION | restored DB | — | DB has two active currencies (company currency THB with 2 decimals and rounding 0.01, plus USD) and zero currency rate rows, so any foreign-currency conversion falls back to rate 1.0 until a rate is entered; no cron or module in the installed set fetches rates | N-TXA1-076 |
| VDR-TXA1-C279 | FUNCTION MAPPING REQUIRED | account/models/product.py:40 | taxes_id = fields.Many2many | OBSERVATION | restored DB | — | DB has 16 seeded service-type product templates: 14 carry the default sale tax (standard output VAT), 16 carry the default purchase tax (standard input VAT); none carries account tags | N-TXA1-093 |
| VDR-TXA1-C280 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:41 | early_pay_discount_computation | OBSERVATION | restored DB | — | DB has 10 payment terms, all with early-payment tax reduction mode 'included' (on early payment); one has an early discount enabled | N-TXA1-093 |
| VDR-TXA1-C281 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:137 | non_deductible_account_id | OBSERVATION | restored DB | — | DB purchase journal has no private-share account set; the partial-deductibility group exists; journals: sale, purchase, general, exchange, cash-basis, bank, stock | N-TXA1-063 |
| VDR-TXA1-C282 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:16 | "l10n_th_account_114100" | OBSERVATION | restored DB | — | Tax-related ledger accounts exist: undue input VAT 114100 and undue output VAT 213100 (not referenced by any tax), input VAT 114200, creditable withholding 114300, VAT receivable 114400, withholding receivable 114401, output VAT 213200, withheld PND3 213301, PND53 213302, PND54 213303 (not referenced by any tax), VAT payable 213400, withholding payable 213500, customer advances 212400 | N-TXA1-055 |
| VDR-TXA1-C283 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:2 | Purchase amount that is entitled | OBSERVATION | restored DB | — | DB holds 13 Thai tax-grid tags (sales amount, zero-rated sales, exempt sales, output tax, purchase amount, input tax, excess carried forward, income PND53, PND53, surcharge 53, income PND3, PND3, surcharge 3); the three surcharge/excess tags are on no tax | N-TXA1-056 |
| VDR-TXA1-C284 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2363 | _compute_taxes_legal_notes | FACT | always | — | Legal notes entered on each tax used by a document are concatenated into a document field printed on the invoice; fiscal position notes print too; the Thai template declares no legal notes | N-TXA1-059 |
| VDR-TXA1-C285 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:432 | taxes_legal_notes | FACT | always | — | Invoice layout prints the taxes legal notes block and the fiscal position note when non-empty | N-TXA1-059 |
| VDR-TXA1-C286 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:243 | tax.tax_label | FACT | always | — | Invoice lines show the tax labels (invoice label else name) of each line's taxes | N-TXA1-059 |
| VDR-TXA1-C287 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:248 | o.company_price_include == 'tax_excluded' | FACT | always | — | Invoice line amount column shows the untaxed subtotal when the company default is tax-excluded and the taxed total when tax-included | N-TXA1-072 |
| VDR-TXA1-C288 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:373 | account.document_tax_totals | FACT | always | — | Invoice layout prints tax totals per tax group via the totals summary, plus a company-currency tax block when the document flag is set | N-TXA1-059 |
| VDR-TXA1-C289 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2218 | _compute_amount_total_words | FACT | company flag on | — | Total in words is produced by the currency's amount-to-text helper (comma removed), controlled by a company flag | N-TXA1-059 |
| VDR-TXA1-C290 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:1 | "invoice_label" | INFERENCE | Thai chart loaded | — | The Thai tax csv header has no legal-notes column, so Thai taxes carry no printed legal notes; invoice label column is present but empty for all rows | N-TXA1-059 |
| VDR-TXA1-C291 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4482 | if self.is_sale_document(include_receipts=True) | FACT | quick-encoding mode on, no frequent history | — | Quick-encoding fallback taxes: the journal default account's taxes of the right type, else the company default sale or purchase tax, then mapped by the fiscal position | N-TXA1-043 |
| VDR-TXA1-C292 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4513 | force_price_include=True | FACT | quick-encoding mode on | — | Quick-encoding derives the untaxed unit price from the typed total by running the engine in forced price-included mode (a special formula applies for one percentage tax with a mixed early-payment discount) | N-TXA1-070 |
| VDR-TXA1-C293 | PCO-F01 | account/models/account_move.py:5703 | affects_tax_report = move._affect_tax_report() | FACT | posting a move | — | At posting, if the tax lock date (or other lock) is violated by a taxed move, the accounting date is advanced to the first open day via the accounting-date helper | N-TXA1-098 |
| VDR-TXA1-C294 | PCO-F01 | account/models/account_move_line.py:1526 | _check_tax_lock_date | FACT | posted move modified | — | Changing a posted taxed line on or before the tax lock date (or hard lock) is refused with a message about an already issued tax statement | N-TXA1-098 |
| VDR-TXA1-C295 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1552 | _check_caba_non_caba_shared_tags | FACT | always | — | A journal item may not mix cash-basis and invoice-basis taxes that share the same tags | N-TXA1-036 |
| VDR-TXA1-C296 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:7 | ubl_cii_tax_category_code | FACT | account_edi_ubl_cii installed | — | The e-invoicing module adds a tax category code (standard, zero-rated, exempt, reverse charge, export, outside scope and others) and an exemption reason code to each tax | N-TXA1-058 |
| VDR-TXA1-C297 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:431 | if supplier.country_id == customer.country_id | FACT | tax without a category code | — | Without a category code the exporter infers: domestic zero-amount tax gives exempt, domestic reverse-charge gives AE, domestic other gives standard; cross-border uses region rules else standard for non-zero and exempt for zero | N-TXA1-058 |
| VDR-TXA1-C298 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:396 | def _validate_taxes | FACT | electronic export | — | Electronic export re-validates the distribution structure of every tax on the invoice lines and raises a named error | N-TXA1-058 |
| VDR-TXA1-C299 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:7 | ubl_cii_tax_category_code | INFERENCE | restored DB | RT | DB: none of the 18 Thai taxes has a category code set; the e-invoicing module's model files include no Thai-specific builder; so by lines 431-434 of the common helper a Thai 0% sale tax would be inferred as exempt if exported (no Thai format exists in the installed set) | N-TXA1-058 |
| VDR-TXA1-C300 | FUNCTION MAPPING REQUIRED | purchase/models/account_tax.py:17 | def _compute_is_used | FACT | purchase installed | — | Purchase module marks a tax as used when it appears on purchase order lines, extending the delete guard | N-TXA1-094 |
| VDR-TXA1-C301 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:17 | def _compute_is_used | FACT | hr_expense installed | — | Expense module marks a tax as used when it appears on expenses | N-TXA1-094 |
| VDR-TXA1-C302 | FUNCTION MAPPING REQUIRED | sale/models/__init__.py:3 | from . import account_move | INFERENCE | sale installed | — | No sale-module file extends the tax model (its model files are listed in the package index: no tax file), so a tax used only on sales order lines is not reported as used by the delete guard (grep over installed modules found overrides of the used-flag only in purchase and hr_expense) | N-TXA1-094 |
| VDR-TXA1-C303 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:36 | def _prepare_base_line_grouping_key | FACT | hr_expense installed | — | Only the expense module overrides the tax engine's base-line, tax-line, base grouping-key and tax-repartition grouping-key hooks among installed modules (scan of every installed module for tax-engine method names found no other override) | N-TXA1-048 |
| VDR-TXA1-C304 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:94 | def _prepare_product_base_line_for_taxes_computation | FACT | hr_expense installed | — | Only the expense module overrides the journal-entry product base-line hook among installed modules | N-TXA1-048 |
| VDR-TXA1-C305 | FUNCTION MAPPING REQUIRED | stock_delivery/models/stock_move.py:79 | _add_tax_details_in_base_line | FACT | stock_delivery installed | — | Delivery stock moves reuse the sale line's base line and engine to compute the delivered quantity's tax-included value (raw total included) for display | N-TXA1-047 |
| VDR-TXA1-C306 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:352 | base_line = line._prepare_base_line_for_taxes_computation() | FACT | sale_loyalty installed | — | Loyalty reuses engine aggregation by tax to split discounts across tax sets | N-TXA1-027 |
| VDR-TXA1-C307 | FUNCTION MAPPING REQUIRED | mrp_account/models/product.py:10 | def _get_product_accounts | FACT | mrp_account installed | — | Manufacturing accounting extends product accounts with the production cost account | N-TXA1-046 |
| VDR-TXA1-C308 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:130 | def _get_product_accounts | FACT | stock_account installed | — | Stock accounting extends product accounts with the stock valuation account (category, else company) | N-TXA1-046 |
| VDR-TXA1-C309 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:50 | _get_fiscal_position(partner) | FACT | purchase_requisition installed | — | Purchase agreements set the order's fiscal position from the vendor and map vendor taxes through it | N-TXA1-082 |
| VDR-TXA1-C310 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:342 | _get_fiscal_position(partner) | FACT | purchase_stock installed | — | Replenishment-created purchase orders get a fiscal position from the vendor and a price adapted by the tax-included price fixer | N-TXA1-082 |
| VDR-TXA1-C311 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:129 | _get_fiscal_position(partner_supplier) | FACT | sale_purchase installed | — | Purchase orders created from service sales get the supplier's fiscal position and mapped vendor taxes | N-TXA1-082 |
| VDR-TXA1-C312 | FUNCTION MAPPING REQUIRED | sale_project_stock/models/stock_move.py:44 | fpos = order.fiscal_position_id | FACT | sale_project_stock installed | — | Project stock moves create sale lines with the product's sale taxes mapped by the order's fiscal position | N-TXA1-041 |
| VDR-TXA1-C313 | FUNCTION MAPPING REQUIRED | account/models/partner.py:247 | def _get_fiscal_position | INFERENCE | installed set | — | No installed module overrides the fiscal-position finder, its validation list or tax/account mapping (scan found no override of those method names outside the accounting module) | N-TXA1-081 |
| VDR-TXA1-C314 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:7 | def _get_name_invoice_report | FACT | Thai module installed | — | Thai module overrides the invoice document name hook | N-TXA1-057 |
| VDR-TXA1-C315 | FUNCTION MAPPING REQUIRED | stock_account/models/account_chart_template.py:27 | _get_stock_account_account | FACT | stock_account installed | — | Stock accounting extends the chart template loader for stock accounts (not tax related) | N-TXA1-096 |
| VDR-TXA1-C316 | FUNCTION MAPPING REQUIRED | sale/models/chart_template.py:8 | def _get_property_accounts | FACT | sale installed | — | Sale extends the chart loader with the down-payment account property | N-TXA1-096 |
| VDR-TXA1-C317 | FUNCTION MAPPING REQUIRED | account_tax_python/models/account_tax.py:16 | selection_add=[('code', "Custom Formula")] | FACT | account_tax_python NOT installed | — | Formula tax add-on adds computation type 'code' and a safe-evaluated formula, overriding the fixed-amount evaluation hook (line 116); source only, not installed in this DB | N-TXA1-019 |
| VDR-TXA1-C318 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_tax.py:71 | def _add_tax_details_in_base_line | FACT | l10n_account_withholding_tax NOT installed | — | Payment-time withholding add-on filters on-payment withholding taxes out of document tax computation (filter function) and adds a flag on the tax; source only, not installed (see U23) | N-TXA1-019 |
| VDR-TXA1-C319 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:107 | def _run_vat_checks | FACT | base_vat NOT installed | — | VAT-validation add-on overrides the accounting stub to validate VAT syntax per country and optionally via VIES; source only, not installed | N-TXA1-019 |
| VDR-TXA1-C320 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:7 | account.update.tax.tags.wizard | FACT | account_update_tax_tags NOT installed | — | A wizard add-on to re-apply tax tags to existing journal items exists in source; not installed | N-TXA1-019 |
| VDR-TXA1-C321 | FUNCTION MAPPING REQUIRED | account_debit_note/models/account_move.py:33 | def action_debit_note | FACT | account_debit_note NOT installed | — | Debit note add-on adds a debit-note action on invoices; source only, not installed (see U23/U24) | N-TXA1-019 |
| VDR-TXA1-C322 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move.py:111 | line.product_id.valuation != 'real_time' | FACT | stock_account installed | — | Valuation (COGS) journal items for customer invoices are generated only for storable products whose valuation is real-time; they use stock valuation and expense accounts mapped by fiscal position and are created without taxes, so VAT never enters cost of goods sold | N-TXA1-067 |
| VDR-TXA1-C323 | FUNCTION MAPPING REQUIRED | account/models/account_move_line_tax_details.py:147 | tax_rep.use_in_tax_closing IS TRUE | INFERENCE | installed set | — | Outside the engine, the only reader of the distribution-line closing flag found in installed modules is the reporting tax-details query (analytic condition, line 147); no installed module posts a tax closing entry from the flag (grep over non-localization modules found only these two files) | N-TXA1-038 |
| VDR-TXA1-C324 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:956 | (special_mode or tax.price_include == batch[0].price_include) | INFERENCE | company default switched to tax included | RT | Purchase withholding rows of the Thai template carry no price-include override (csv rows 26-57) whereas sale withholding rows are forced tax_excluded (row 58); if the company default were set to tax included, a purchase VAT and a purchase withholding on one line would share a batch (same type, price flag, include-base flag, lines 954-962) and the negative percentage would shrink the extracted base (line 1110); numeric effect not executed | N-TXA1-080 |
| VDR-TXA1-C325 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:488 | _compute_invoice_repartition_line_ids | FACT | tax created without distribution lines | — | A tax created without distribution lines receives default invoice and credit-note lines (one base and one tax line each, no account, no tags, 100 percent) | N-TXA1-094 |
| VDR-TXA1-C326 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:669 | def write(self, vals) | INFERENCE | always | — | The tax write method only sanitises values (lines 628-655, 669-670); no constraint or guard concerning the active flag was found in the tax model, so archiving a used tax is not blocked by the model | N-TXA1-094 |
| VDR-TXA1-C327 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:468 | def _message_log | FACT | always | — | Chatter logging of tracked tax fields and formatted distribution changes happens only when the tax is already used | N-TXA1-094 |
| VDR-TXA1-C328 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:462 | ondelete="restrict" | FACT | always | — | A fiscal position referenced by a document cannot be deleted (restrict); help text says positions adapt taxes and accounts and default from the customer | N-TXA1-084 |
| VDR-TXA1-C329 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2679 | _onchange_fpos_id_show_update_fpos | FACT | document with lines | — | Changing the fiscal position on a document that has lines raises an update-lines prompt | N-TXA1-111 |
| VDR-TXA1-C330 | FUNCTION MAPPING REQUIRED | account/models/partner.py:35 | active = fields.Boolean(default=True, | FACT | always | — | Fiscal positions can be archived through the active flag without deletion | N-TXA1-084 |
| VDR-TXA1-C331 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: numeric results of combining a 7 percent VAT with a withholding tax on one line, and of rounding deltas over several lines in THB, were not executed; resolve by a runtime test with representative documents (compare U13 C088) | N-TXA1-116 |
| VDR-TXA1-C332 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Thai company | — | UNKNOWN - STATUTORY SOURCE REQUIRED: whether Thai statutory practice for rounding tax amounts matches round-globally or round-per-line is not established by Community evidence; pending TXS | N-TXA1-117 |
| VDR-TXA1-C333 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | zero-rated or exempt sale | RT | UNKNOWN - EVIDENCE INSUFFICIENT: runtime confirmation that a zero-rated sale leaves exactly base items carrying both grid tags (source drops the zero tax item), and whether the three unused tags matter to any report formula, was not executed | N-TXA1-118 |
| VDR-TXA1-C334 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | foreign-currency order invoiced later | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether order-date and invoice-date rates produce different tax amounts between the order and its invoice was not executed; resolve by a runtime test with a rate entered | N-TXA1-119 |
| VDR-TXA1-C335 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Thai company | — | UNKNOWN - STATUTORY SOURCE REQUIRED: statutory classification, rate, grid and account of each seeded Thai tax record are unverified; pending TXS | N-TXA1-120 |
| VDR-TXA1-C336 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Thai company | — | UNKNOWN - STATUTORY SOURCE REQUIRED: whether a prohibited input-tax treatment can be represented by the percentage deductibility mechanism (the return grid would still count the base as claimable) is unknown; pending TXS | N-TXA1-121 |
| VDR-TXA1-C337 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Thai company | — | UNKNOWN - STATUTORY SOURCE REQUIRED: statutory source and date of exchange rates for tax on foreign-currency transactions are not established; pending TXS | N-TXA1-122 |
| VDR-TXA1-C338 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | tax used only on sales order lines | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether such a tax can be deleted in practice (foreign key behaviour) and how the Thai template reload behaves against modified taxes were not executed | N-TXA1-123 |
