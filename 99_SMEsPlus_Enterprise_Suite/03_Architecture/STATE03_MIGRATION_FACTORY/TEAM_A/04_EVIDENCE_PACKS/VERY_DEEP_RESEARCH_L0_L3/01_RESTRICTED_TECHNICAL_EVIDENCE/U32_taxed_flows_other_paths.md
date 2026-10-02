# U32 — taxed_flows_other_paths — Restricted Technical Evidence

**RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**

- Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** (no V-level, no Complete, no coverage percentage, no Gate PASS)
- Unit: U32 `taxed_flows_other_paths` — Thai Tax Core lane, Odoo-behaviour sub-lane: source-level completion for the other paths through which taxes enter entries, which TXA1 and TXA2 listed as not read. Statutory facts are owned by TXS; statutory links below are links to existing TXS rows only, never an assertion of law.
- Topics: (1) generic tax engine and calculation, (3) standard-rated, zero-rated, exempt, non-deductible treatment, (4) document types, (6) price-included, rounding, currency, (7) tax journal entries, reconciliation, reversal, (8) company, partner, product, fiscal configuration, (9) VAT and withholding data and reporting requirements, (12) cross-module triggers
- Modules read (Community only): account (bank statement line and statement, reconcile model, partial reconcile, payment register wizard, automatic-entry and accrual wizards, tax engine hooks, fiscal-position finder), hr_expense, sale_expense, sale_expense_margin, stock_landed_costs, mrp_landed_costs, mrp_subcontracting_landed_costs, mrp_account, mrp_subcontracting_purchase, purchase_mrp (report), purchase_stock (price-difference lines, replenishment), account_edi_ubl_cii (shared and generic builders, tax model, partner format selection, import), account_edi, delivery, sale_loyalty, sale_loyalty_delivery, loyalty, sale_margin, sale_product_matrix, purchase_product_matrix, product_matrix, sale (down payment, early-payment lines, reinvoice values), purchase (bill-to-order wizard, fiscal position paths), purchase_requisition, l10n_th (tax template header), and, uninstalled and read at source only: account_tax_python, l10n_account_withholding_tax, account_update_tax_tags, account_debit_note, base_vat
- Source revision: `19.0.post20260921` (`odoo/addons`) · Date: 2026-10-02 · Charter: `thaitax_common.txt` (overrides `wave3_common.txt` where different) and `WORKER_SPEC_L2_L3.md`
- Not used: Extra, Custom, OEEL-1, OPL-1 or Enterprise code; no Odoo started; source evidence is not runtime proof (flag `RT`). Foreign country format files (BIS 3, CII, XRechnung, NLCIUS, A-NZ, SG, PINT, E-FFF) are future optional country-pack material and were not studied.
- Claim ids `VDR-U32-C###`; neutral ids `N-U32-###` in `02_NEUTRAL_KNOWLEDGE/U32_taxed_flows_other_paths_NEUTRAL.md`. Database: restored dump queried for configuration only (module state, counts, flags, seeded configuration names); no business data exists (1 company, periodic valuation, standard cost, anglo-saxon flag off).

## 0. Scope, method, limits and re-verification of prior evidence

Method: for each of the seven assigned areas the base code and every override in installed Community modules were read at the lines cited in the claims; the tax-bearing hand-off was traced to the line values that reach the tax engine or the journal; the restored database was queried for configuration only. Where a module contains no tax logic the search is recorded as `NO TAX HANDLING FOUND` with its scope (section 5). Prior evidence was used as a map and re-verified only at the lines relied on:

| Prior evidence relied on | Result of re-verification | Where used |
|---|---|---|
| TXA2 honest limits (bank-statement reconcile models, landed costs, manufacturing and subcontracting, e-invoicing format code not read) | CLOSED for the Community-installed modules named above; foreign format classes remain not read (VDR-U32-C125) | CAP-U32-01, -03, -04 |
| U12-C258, U12-C259 (reconcile-model engine outside Community), U12-C222, U12-C229, U12-C240, U12-C160 | CONFIRMED at source; this unit adds the tax angle: preset taxes have no Community consumer (VDR-U32-C003, VDR-U32-C004, VDR-U32-C006) | CAP-U32-01 |
| U12 early-payment discount (C075, C267..C294) and TXA1-C107, C144, C280 | CONFIRMED; this unit verifies tax-base redistribution with several taxes (VDR-U32-C169, VDR-U32-C170, VDR-U32-C179) | CAP-U32-07 |
| U16-C005..C012, C121..C123, C134, C137, C182, C435 (expense tax flow) | CONFIRMED (VDR-U32-C032, VDR-U32-C036, VDR-U32-C037, VDR-U32-C039, VDR-U32-C041, VDR-U32-C053); this unit adds company-paid rate and plug lines, SQL base-to-tax mapping, reinvoice price source | CAP-U32-02 |
| U05-C019 (loyalty discount products created without taxes) | NARROWED by the dump: the seeded reward discount product carries the 7% sale tax (VDR-U32-C146); code claim VDR-U32-C141 holds for products created while the order-loyalty module is installed | CAP-U32-05 |
| U05-C104..C109, C113, C114, C125 (down payment) | CONFIRMED; tax-inclusive target and per-tax rounding added (VDR-U32-C159, VDR-U32-C160, VDR-U32-C161) | CAP-U32-06 |
| U06-C177, C182, C183 and TXA1-C230 (purchase line taxes) | CONFIRMED; refinement: tax routine is onchange and explicit-call driven, not a stored compute (VDR-U32-C190, VDR-U32-C191) | CAP-U32-08 |
| U25-C187, C189, C203, C204, C211 (fiscal position, no position in dump) | CONFIRMED (VDR-U32-C199) | CAP-U32-08 |
| U23-C009, C025, C058, C059, C075, C078, C113, C129, C139..C165, C174, C177, C179, C185 (uninstalled add-ons) | CONFIRMED; only depth added (VDR-U32-C204, VDR-U32-C209, VDR-U32-C211, VDR-U32-C212, VDR-U32-C214) | CAP-U32-09 |
| TXA1-C039..C047, C099, C101, C216, C217, C226, C248, C306 (engine, discounts, loyalty splitting) | CONFIRMED where relied on (VDR-U32-C136, VDR-U32-C139, VDR-U32-C156) | CAP-U32-05, -06 |

Honest limits: no execution; tax numeric results, rounding equality and several RT items are listed in section 3. Format-specific e-invoice builders were read only down to class headers. Statutory requirements are not derived from any behaviour described here.

## 1. DISCOVERED SUPPORTING MODULES (read only as far as needed)

`account_payment` (payment register wizard write-off and early-payment values), `purchase_stock` (price-difference lines, replenishment fiscal position), `purchase_requisition` (requisition and alternative orders), `purchase_mrp` (manufacturing overview cost report), `sale_expense` and `sale_expense_margin` (reinvoice and margin), `sale_loyalty_delivery` (free shipping reward), `loyalty` (rule and seeded data), `delivery` (carrier line), `mrp_landed_costs`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`, `mrp_account`, `account_edi_proxy_client` and `account_peppol_advanced_fields` (state only), `account_fleet` (not read), `l10n_th` (tax template header and tax rows only). Search-only (no tax reference found): `mrp`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `sale_mrp`, `sale_mrp_margin`, `product_matrix`, `sale_product_matrix`, `purchase_product_matrix`.

## 2. Contradictions with earlier units and packets

1. **U05-C019 (reward discount products are created without taxes)** — CONTRA (narrowing, dump-specific): VDR-U32-C146. The base loyalty module creates the reward discount product with no tax override; the order-loyalty override that strips taxes applies only to products created after it is installed (VDR-U32-C141); the seeded gift-card reward product was created earlier and carries the 7% sale tax in the dump, while the order-loyalty data file strips only the trigger products (VDR-U32-C142). Effect: gift-card sale is untaxed and its redemption line is taxed (VDR-U32-C140) in this configuration (RT).
2. No contradiction with U12-C258/C259 (confirmed, VDR-U32-C003), U16-C182 (confirmed, VDR-U32-C053, VDR-U32-C054), U06-C182/C183 (refined, not contradicted, VDR-U32-C190, VDR-U32-C191), TXA1-C248/C306 (confirmed, VDR-U32-C136, VDR-U32-C139), TXA2 section 0 limits (closed for Community modules).
3. Source-internal observations (not contradictions): the base UBL builder file carries 30 deprecation markers and the older UBL 2.0 builder leaves the withholding total empty while the BIS 3 class calls the new builder (VDR-U32-C110); reward lines are fiscal-position-mapped twice (VDR-U32-C143); the reconcile-model line-values helper has no caller (VDR-U32-C006).

## 3. Runtime/AWT (RT) list (summary; each item also flagged in a claim or capability)

| RT id | Item | Claims |
|---|---|---|
| RT-01 | Reconciliation tool outside the studied code adding taxed lines to bank entries; cash-basis tax matched from a bank line | VDR-U32-C006, VDR-U32-C024 |
| RT-02 | Parent-company taxes on the expense mail-gateway path; foreign-currency expense numeric tax; company-paid entry as read by the input-tax ledger; supplier identity on employee-paid receipts | VDR-U32-C027, VDR-U32-C044, VDR-U32-C059 |
| RT-03 | Landed cost and subcontracting bills with non-deductible tax or withholding; entries under perpetual valuation | VDR-U32-C083 |
| RT-04 | Export of a Thai document (7%, zero-rated, exempt, withholding) through a manually chosen European format; which tax-total generation runs per format | VDR-U32-C094, VDR-U32-C100, VDR-U32-C110, VDR-U32-C114, VDR-U32-C127 |
| RT-05 | Gift-card redemption, stacked rewards and double fiscal-position mapping of reward lines; programmatic purchase lines without taxes | VDR-U32-C143, VDR-U32-C155, VDR-U32-C191, VDR-U32-C154 |
| RT-06 | Advance combined with global discount, early-payment discount or withholding | VDR-U32-C166 |
| RT-07 | Order versus invoice versus payment-time early-payment tax equality with several taxes, instalments and foreign currency | VDR-U32-C175, VDR-U32-C184 |
| RT-08 | Foreign customers and vendors with a configured fiscal position; finder with numeric Thai tax ids | VDR-U32-C198, VDR-U32-C202 |
| RT-09 | Installing the uninstalled add-ons: formula tax with price-included flag, withholding base and grid tags, debit note rate and date | VDR-U32-C207, VDR-U32-C213, VDR-U32-C217, VDR-U32-C218, VDR-U32-C219 |
| RT-10 | Tax-report effect of cut-off reclassification of taxed base lines; accrual of price-included lines | VDR-U32-C225 |

## 4. Native-gap candidates (for the controller; vocabulary NATIVE · PARTIAL · NATIVE GAP / EXTENSION REQUIRED · UNKNOWN)

| Gap candidate | Native status | Claims | Statutory link (existing TXS rows, link only) |
|---|---|---|---|
| Thai electronic tax invoice and receipt file format and reporting (no export format bound to Thailand; European code lists only) | NATIVE GAP / EXTENSION REQUIRED | VDR-U32-C111, VDR-U32-C112, VDR-U32-C113, VDR-U32-C085, VDR-U32-C125, VDR-U32-C127 | S14-01..S14-09, S06-02 |
| Distinguishing Thai zero-rated from exempt supply in an exported document (needs a code on each tax; list has no Thai reasons) | PARTIAL | VDR-U32-C088, VDR-U32-C094, VDR-U32-C096 | S03-01, S03-03 |
| Applying reconcile-model taxes to bank-statement entries (preset taxes stored, no Community engine) | NATIVE GAP / EXTENSION REQUIRED | VDR-U32-C001, VDR-U32-C003, VDR-U32-C006 | n/a (requirement not derived) |
| Thai tax on bank-originated entries (fees, interest) through classification of the statement line | NATIVE GAP / EXTENSION REQUIRED | VDR-U32-C007, VDR-U32-C012, VDR-U32-C024 | n/a (requirement not derived) |
| Purchase-order early supplier discount tax builder (none found) | UNKNOWN | VDR-U32-C176 | S05-05 |
| Fiscal positions for foreign customers and vendors on Thai flows (engine native; no seeded position; manual tax choice) | PARTIAL | VDR-U32-C199, VDR-U32-C198, VDR-U32-C202 | S03-01, S10-01 |
| Withholding on expense lines and company-paid expenses (not traced) | UNKNOWN | VDR-U32-C041, VDR-U32-C059 | S13-02 |
| Landed cost, manufacturing and subcontracting tax handling (NO TAX HANDLING FOUND; requirement not derived from absence) | UNKNOWN | VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081 | n/a |
| Gift-card sale and redemption tax asymmetry in the seeded configuration | PARTIAL | VDR-U32-C140, VDR-U32-C142, VDR-U32-C146 | n/a |

## 5. Search records (NO TAX HANDLING FOUND where applicable)

| Scope searched | Method | Result | Claims |
|---|---|---|---|
| stock_landed_costs, mrp_landed_costs, mrp_subcontracting_landed_costs, mrp, mrp_account, mrp_subcontracting, mrp_subcontracting_account, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping, sale_mrp, sale_mrp_margin | case-insensitive search for tax and fiscal in python, xml and csv files | **NO TAX HANDLING FOUND** | VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081 |
| purchase_mrp | same | report-level compute_all of purchase line taxes only (cost shown without recoverable tax); no posting | VDR-U32-C077 |
| product_matrix, sale_product_matrix, purchase_product_matrix, sale_mrp_margin | same, plus js | **NO TAX HANDLING FOUND** (lines created from defaults; tax from standard line rules) | VDR-U32-C147, VDR-U32-C148, VDR-U32-C151 |
| sale_margin, sale_expense_margin | same | untaxed amounts used for margin only | VDR-U32-C149, VDR-U32-C150, VDR-U32-C058 |
| account bank statement and statement-line models | same | no tax reference in either file; statement entries untaxed | VDR-U32-C007, VDR-U32-C008 |
| hr_expense python and wizard files | grep for fiscal | no fiscal-position reference | VDR-U32-C196 |

## 6. How Thai taxes map in an exported document (format level, inference; foreign formats not studied)

| Thai tax (template row) | Default category when no code is set | Percent exported | Placement | Claims |
|---|---|---|---|---|
| Output VAT 7% (`tax_output_vat`) | S (standard) | 7 | tax total and line category | VDR-U32-C091, VDR-U32-C098, VDR-U32-C100 |
| Output VAT 0% (`tax_output_vat_0`, zero-rated) | E (exempt), also for a non-EEA customer | 0 | tax total, category E with default exempt text | VDR-U32-C090, VDR-U32-C093, VDR-U32-C094, VDR-U32-C095 |
| Output VAT 0% exempt (`tax_output_vat_exempted`) | E | 0 | same as above, not distinguishable from zero-rated | VDR-U32-C090, VDR-U32-C094 |
| Sales withholding taxes (negative percent, e.g. `tax_wht_income_3`) | withholding flag | negative rate | withholding total with reversed sign, outside line categories, netted from inclusive total | VDR-U32-C099, VDR-U32-C100, VDR-U32-C101, VDR-U32-C102, VDR-U32-C103 |
| Input VAT 7% and purchase withholding taxes | not exported (vendor bills are exported only for self-billing journals) | n/a | n/a | VDR-U32-C115 |

Statutory links (link only): S06-02 (tax invoice content), S14-02, S14-05 (e-tax invoice form), S13-02, S13-03 (withholding certificate), S03-01, S03-03 (zero-rated and exempt). Nothing here derives a statutory requirement from the behaviour.

## 7. Native status per function (summary; full rows in the Function Catalog register)

| Native status | Count | Cat-IDs |
|---|---|---|
| NATIVE | 16 | U32-F04, U32-F06, U32-F07, U32-F10, U32-F12, U32-F18, U32-F19, U32-F20, U32-F23, U32-F24, U32-F26, U32-F27, U32-F28, U32-F30, U32-F39, U32-F40 |
| PARTIAL | 19 | U32-F01, U32-F05, U32-F08, U32-F09, U32-F11, U32-F14, U32-F15, U32-F16, U32-F21, U32-F22, U32-F25, U32-F31, U32-F32, U32-F33, U32-F34, U32-F35, U32-F36, U32-F37, U32-F38 |
| NATIVE GAP / EXTENSION REQUIRED | 3 | U32-F02, U32-F03, U32-F17 |
| UNKNOWN | 2 | U32-F13, U32-F29 |

## CAP-U32-01 Bank statement lines and reconcile models that can add taxed lines

**Function-ID(s):** FUNCTION MAPPING REQUIRED (PCO-F01 only for the cash-basis date claim)

### D1 Business purpose and process semantics
Business purpose: record bank movements and later classify them; decide whether the Community product itself ever adds taxed lines to a bank entry. Finding: a statement line creates an untaxed liquidity plus suspense entry (VDR-U32-C007, VDR-U32-C008, VDR-U32-C011); the reconcile model stores taxes on its lines but no Community code applies a model (VDR-U32-C001, VDR-U32-C003, VDR-U32-C006); taxed content can reach a bank entry only through manual edit, an external reconciliation tool, a cash-basis settlement or the early-payment helper (VDR-U32-C017, VDR-U32-C018, VDR-U32-C020, VDR-U32-C021).

### D2 Architecture, data and object relationships
Objects: account.bank.statement.line (inherits account.move, always entry type), account.bank.statement, account.reconcile.model and account.reconcile.model.line (tax_ids, amount types, trigger), account.move.line.reconcile_model_id, account.partial.reconcile (cash-basis collection), account.payment.register wizard (write-off line). Relations: model line to taxes through account_reconcile_model_line_account_tax_rel (VDR-U32-C001, VDR-U32-C004).

### D3 Source, technical and workflow logic
Control and data flow. Statement line create -> two line value sets -> entry posted (VDR-U32-C007, VDR-U32-C009). Edit of amount, currency or partner -> synchronisation rewrites to liquidity plus suspense and deletes other lines (VDR-U32-C012, VDR-U32-C013, VDR-U32-C014). Reconcile -> partials -> cash-basis entries if a cash-basis tax is on the document (VDR-U32-C017, VDR-U32-C018).
State diagram (A -> B [trigger]):
- statement line created -> entry posted [create, automatic post] (VDR-U32-C009)
- entry posted -> entry rewritten untaxed [amount, currency, partner or label edit] (VDR-U32-C012)
- posted entry with tax lines -> unchanged tax [no draft sync for posted moves] (VDR-U32-C010)
- matched to document -> cash-basis entry created [partial reconcile, cash-basis taxes only] (VDR-U32-C017)
- reconciliation undone -> statement line back to default lines [only if locks pass] (VDR-U32-C023)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Create statement line -> untaxed bank entry posted (VDR-U32-C007, VDR-U32-C009); tax classification happens outside the studied code (VDR-U32-C003). |
| 2 Reversal / cancel / negative path | Undo reconciliation restores default lines when fiscal and tax lock checks pass (VDR-U32-C023); cash-basis entries follow partial removal (TXA2 relied on). |
| 3 Multi-company / data scope | Reconcile models have a company; record rule and ACL per U12-C263/C266; preset taxes are company-checked (VDR-U32-C001). |
| 4 Side effects & cross-module triggers | Partial reconcile triggers cash-basis entries (VDR-U32-C017, VDR-U32-C018); early-discount helper shared with the payment wizard (VDR-U32-C020, VDR-U32-C021). |
| 5 Configuration & optionality | Presets optional; no tax-included flag (VDR-U32-C002); trigger manual or automated has no consumer here (VDR-U32-C003). |
| 6 Validation & constraints | One liquidity line, at most one suspense line; other lines rewritten on edits (VDR-U32-C012, VDR-U32-C014); regex and amount checks on presets (U12-C249). |
| 7 Roles & permissions | ACL and rules per U12-C262..C266; this unit adds the tax is-used guard on presets (VDR-U32-C004, VDR-U32-C005). |
| 8 Scheduled / automated behavior | None found; the account cron list has no statement or preset job (U12-C261). |
| 9 Exception & failure behavior | Missing suspense account stops creation (U12-C223); invalid entry shape raises a user error (VDR-U32-C014); cash-basis journal missing raises error at partial (source line 276-279, not claimed separately). |
| 10 Accounting, stock, audit, security & compliance implications | Bank entries carry no tax tags by default; foreign-currency conversion has no tax (VDR-U32-C015, VDR-U32-C016); a Thai tax on bank fees or interest would need an external classifier (native gap candidate). |

### DB reconciliation (configuration only)
Restored DB: 2 reconcile models, 0 preset-line tax relations, 0 statements, 0 statement lines; all 18 taxes on invoice (VDR-U32-C022, VDR-U32-C019).

### Unknown / Runtime list
- RT: reconciliation tool outside the studied code and cash-basis match from a bank line (VDR-U32-C024)
- RT: reconcile-model line values helper has no caller (VDR-U32-C006)

## CAP-U32-02 Employee expense taxes (computation, receipts, company-paid entries, re-invoicing)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: record employee spending with input tax and reimburse the employee or book a company-paid expense; optionally re-invoice the customer. U16 covered the flow; this capability fixes the tax computation and tax-line effects. Tax is extracted from the typed total (price-included for every tax) (VDR-U32-C025, VDR-U32-C028, VDR-U32-C032), receipts and company-paid entries carry tax lines per expense (VDR-U32-C033, VDR-U32-C038, VDR-U32-C039, VDR-U32-C040), and a re-invoice uses product customer taxes, not expense taxes (VDR-U32-C053, VDR-U32-C054).

### D2 Architecture, data and object relationships
Objects: hr.expense (tax_ids via expense_tax, tax_amount, untaxed_amount, currency rate), account.move (in_receipt, expense_ids), account.move.line (expense_id), account.tax overrides (expense grouping keys), hr.expense.split wizard, sale.order.line (reinvoice values), sale_expense_margin cost.

### D3 Source, technical and workflow logic
Control and data flow. Expense fields recompute with the shared engine (VDR-U32-C028, VDR-U32-C029, VDR-U32-C030, VDR-U32-C031) -> post -> employee-paid: purchase receipt with total-included base lines (VDR-U32-C033, VDR-U32-C035, VDR-U32-C036, VDR-U32-C037); company-paid: entry from engine tax lines, base plugged to total (VDR-U32-C040, VDR-U32-C042, VDR-U32-C043, VDR-U32-C044) -> optional reinvoice sale line (VDR-U32-C053, VDR-U32-C055, VDR-U32-C056).
State diagram (A -> B [trigger]):
- expense draft -> receipt posted [post, employee paid] (VDR-U32-C033, VDR-U32-C047)
- expense draft -> entry posted with payment [post, company paid] (VDR-U32-C040, VDR-U32-C044)
- receipt posted -> expense detached [cancel or reversal] (VDR-U32-C046)
- expense -> two split expenses [split wizard] (VDR-U32-C048, VDR-U32-C049)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Typed total -> tax and untaxed split (VDR-U32-C028) -> receipt line with expense taxes (VDR-U32-C035) -> posted with today as invoice date (VDR-U32-C047). |
| 2 Reversal / cancel / negative path | Cancel or reversal clears expense link (VDR-U32-C046); reversal is the credit-note reversal (TXA2 relied on). |
| 3 Multi-company / data scope | Taxes limited to company domain (VDR-U32-C026); mail path uses exact company (VDR-U32-C027); expense journal per company (VDR-U32-C047, VDR-U32-C052). |
| 4 Side effects & cross-module triggers | Reinvoice creates sale lines with mapped customer taxes (VDR-U32-C053, VDR-U32-C054); margin uses untaxed cost (VDR-U32-C058); tax lines grouped per expense (VDR-U32-C038, VDR-U32-C039). |
| 5 Configuration & optionality | Expense policy per product; default taxes from product (VDR-U32-C026, VDR-U32-C050, VDR-U32-C051); cash-basis tags only for company-paid (VDR-U32-C041). |
| 6 Validation & constraints | One company-paid expense per entry (VDR-U32-C045); split halves add up (VDR-U32-C049); editing taxes needs editable state (U16-C078). |
| 7 Roles & permissions | 14 ACL rows and 12 record rules seeded by hr_expense in the dump (VDR-U32-C052); roles per U16. |
| 8 Scheduled / automated behavior | hr_expense seeds 1 cron (U16); none touches tax (VDR-U32-C052). |
| 9 Exception & failure behavior | Missing payment method line on company-paid expense raises user error (source line 1636, not claimed separately); reinvoice to draft or locked order is refused (sale line 103-119, not claimed separately). |
| 10 Accounting, stock, audit, security & compliance implications | Input tax recorded at acceptance; supplier identity on employee-paid receipts is RT (VDR-U32-C044); reinvoiced tax may differ from recovered tax (VDR-U32-C054). |

### DB reconciliation (configuration only)
Restored DB: 7 expense products with 7% sale and purchase tax, expense journal set, 0 expenses (VDR-U32-C051, VDR-U32-C052).

### Unknown / Runtime list
- RT: foreign-currency expense numeric tax and company-paid entry reading by tax ledger (VDR-U32-C059, VDR-U32-C044)
- RT: parent-company taxes on mail path (VDR-U32-C027)
- Not read in detail: expense approval, mail alias, post wizard (U16 owns).

## CAP-U32-03 Landed costs, manufacturing and subcontracting entries and their tax interaction

**Function-ID(s):** GRV-F05 (landed cost allocation), MFG-F03 (manual WIP posting) for the claims that carry them; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: decide whether landed costs, manufacturing and subcontracting entries compute or post taxes and how vendor-bill taxes interact. Result: NO TAX HANDLING FOUND in these modules (VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081); a landed cost uses the bill line before tax (VDR-U32-C060) and posts an untaxed entry only for real-time valued products (VDR-U32-C063, VDR-U32-C064, VDR-U32-C066).

### D2 Architecture, data and object relationships
Objects: stock.landed.cost (cost lines, valuation adjustment lines, vendor_bill_id), account.move.line.is_landed_costs_line, mrp.account.wip.accounting wizard, mrp_landed_costs and mrp_subcontracting_landed_costs targets, purchase_stock price-difference lines, purchase_mrp report.

### D3 Source, technical and workflow logic
Control and data flow. Vendor bill with flagged lines -> create landed cost (VDR-U32-C060, VDR-U32-C061, VDR-U32-C062) -> compute split -> validate -> entry (real-time) or value update (periodic) (VDR-U32-C063, VDR-U32-C066, VDR-U32-C067) -> posted (VDR-U32-C070).
State diagram (A -> B [trigger]):
- draft -> posted [validate] (VDR-U32-C070)
- draft -> cancelled [cancel] (VDR-U32-C069)
- posted -> neutralised [negative landed cost] (VDR-U32-C069)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Bill line before tax -> cost line -> allocation -> entry debit stock valuation, credit cost account (VDR-U32-C060, VDR-U32-C065). |
| 2 Reversal / cancel / negative path | Validated cost cannot be cancelled; negative cost reverses (VDR-U32-C069). |
| 3 Multi-company / data scope | Company on the cost and journal; ACL and rule counts in the dump (VDR-U32-C082). |
| 4 Side effects & cross-module triggers | Targets: transfers, manufacturing orders, subcontracted moves (VDR-U32-C071, VDR-U32-C072); value update of moves (VDR-U32-C067). |
| 5 Configuration & optionality | Real-time valuation only (VDR-U32-C066); FIFO or average only (VDR-U32-C068). |
| 6 Validation & constraints | Sum of allocation must match cost lines (source lines 256-270, not claimed separately); standard cost raises error (VDR-U32-C068). |
| 7 Roles & permissions | ACL and rule counts (VDR-U32-C082). |
| 8 Scheduled / automated behavior | None found. |
| 9 Exception & failure behavior | Missing expense account raises error (source line 356, not claimed separately); standard cost refusal (VDR-U32-C068). |
| 10 Accounting, stock, audit, security & compliance implications | No tax line in any of these entries (VDR-U32-C063, VDR-U32-C064, VDR-U32-C073); bill taxes remain on the bill (VDR-U32-C065); price-difference lines carry no tax (VDR-U32-C076). |

### DB reconciliation (configuration only)
Restored DB: landed-cost, manufacturing and subcontracting modules installed; 0 landed costs; periodic valuation and standard cost (VDR-U32-C082, VDR-U32-C066, VDR-U32-C068).

### Unknown / Runtime list
- RT: landed cost and subcontracting bills with non-deductible tax or withholding; perpetual valuation entries (VDR-U32-C083)
- Not read: manufacturing order lifecycle, work orders, BOM costing (U14, U15 own).

## CAP-U32-04 Electronic-invoice tax hooks (category, exemption, how Thai taxes map, amount checks, import)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: describe at format level how taxes are classified and totalled in an exported electronic invoice and how imported taxes are matched; foreign country formats are future optional country-pack material and were not studied. Result: the shared code carries a European category and reason vocabulary (VDR-U32-C084, VDR-U32-C085), predicts codes when absent (VDR-U32-C089, VDR-U32-C090, VDR-U32-C091, VDR-U32-C092, VDR-U32-C093), treats negative-rate percent taxes as withholding (VDR-U32-C099, VDR-U32-C102, VDR-U32-C103), reconciles totals with a rounding amount (VDR-U32-C104, VDR-U32-C105), and offers no Thai format (VDR-U32-C111, VDR-U32-C112, VDR-U32-C113).

### D2 Architecture, data and object relationships
Objects: account.tax (ubl_cii_tax_category_code, ubl_cii_tax_exemption_reason_code), account.edi.common (category prediction, constraints, import), account.edi.ubl (tax grouping keys, tax total nodes, monetary totals, constraint hook), res.partner (format selection by country), account.move (need-XML test), account.move.send (build hook), legacy account.edi framework (post, reset, cancel hooks, tax details helper).

### D3 Source, technical and workflow logic
Control and data flow. Send -> need-XML test (VDR-U32-C115) -> builder -> validate taxes (VDR-U32-C106, VDR-U32-C107) -> grouping keys per tax (VDR-U32-C097, VDR-U32-C098, VDR-U32-C099) -> tax and withholding totals (VDR-U32-C102) -> legal monetary totals with rounding amount (VDR-U32-C103, VDR-U32-C104, VDR-U32-C105) -> constraints -> attach or report errors (VDR-U32-C108, VDR-U32-C116). Import -> tax search plan (VDR-U32-C119, VDR-U32-C120, VDR-U32-C121) -> unmatched logged (VDR-U32-C122) -> tax-total fix within tolerance (VDR-U32-C123, VDR-U32-C124).
State diagram (A -> B [trigger]):
- posted sales document -> XML attached [send, format selected] (VDR-U32-C115, VDR-U32-C116)
- export errors -> sent without XML [error continue] (VDR-U32-C116)
- imported file -> draft bill with matched taxes [import] (VDR-U32-C119, VDR-U32-C122)
- draft bill -> tax amounts aligned to file [all taxes matched, delta within 0.03] (VDR-U32-C123)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Domestic customer with a formatted partner: taxes classified, totals built, rounding amount zero or small (VDR-U32-C089, VDR-U32-C102, VDR-U32-C104). |
| 2 Reversal / cancel / negative path | Credit notes use the same builders; legacy framework cancel hooks mark documents for cancellation (TXA2 relied on, VDR-U32-C117). |
| 3 Multi-company / data scope | Supplier and customer countries and the company drive the codes (VDR-U32-C090, VDR-U32-C092, VDR-U32-C098); import tax search is company-scoped (VDR-U32-C121). |
| 4 Side effects & cross-module triggers | Send flow attaches XML and PDF; import writes chatter logs (VDR-U32-C116, VDR-U32-C122). |
| 5 Configuration & optionality | Category and reason codes per tax are optional (VDR-U32-C084, VDR-U32-C086); partner format selection (VDR-U32-C111, VDR-U32-C114); no Thai code on any Thai tax (VDR-U32-C088). |
| 6 Validation & constraints | Tax on each line (VDR-U32-C109); tax structure check (VDR-U32-C106, VDR-U32-C107); reason required for AE, E, G, O, K (VDR-U32-C086). |
| 7 Roles & permissions | Not studied beyond legacy framework ACL count (VDR-U32-C117). |
| 8 Scheduled / automated behavior | Legacy framework cron exists, no format registered in the dump (VDR-U32-C117). |
| 9 Exception & failure behavior | Export errors do not block sending (VDR-U32-C116); unmatched import taxes only logged (VDR-U32-C122). |
| 10 Accounting, stock, audit, security & compliance implications | No entry is created by export; withholding handling in totals (VDR-U32-C099, VDR-U32-C103); zero-rated versus exempt cannot be distinguished by default (VDR-U32-C094); Thai e-tax invoice format absent (native gap candidate). |

### DB reconciliation (configuration only)
Restored DB: 0 EDI formats, 0 EDI documents, all 18 Thai taxes without codes; module auto-install flag; Peppol module not installed (VDR-U32-C088, VDR-U32-C117, VDR-U32-C126).

### Unknown / Runtime list
- RT: export of a Thai document with 7%, zero, exempt and withholding taxes (VDR-U32-C127)
- RT: which tax-total generation runs per format (VDR-U32-C110)
- UNKNOWN: format-specific builders (VDR-U32-C125)

## CAP-U32-05 Discount, loyalty reward, delivery, product-matrix and margin lines: tax effects

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: record tax correctly on lines that are not plain products: delivery charges, loyalty rewards (free product, discount, free shipping, gift card), matrix-created lines, and margin views. U05 covered the flow; this capability covers tax effects and fills in purchase-side bill and down-payment hand-offs. Result: delivery and reward lines set their taxes explicitly from product taxes mapped by the order position (VDR-U32-C128, VDR-U32-C129, VDR-U32-C132, VDR-U32-C135, VDR-U32-C136); discounts split per tax set (VDR-U32-C136, VDR-U32-C137, VDR-U32-C138, VDR-U32-C139); matrix and margin modules have no tax logic (VDR-U32-C147, VDR-U32-C148, VDR-U32-C151).

### D2 Architecture, data and object relationships
Objects: sale.order.line (delivery flag, reward flag, tax_ids), delivery carrier, sale.order (reward values, discountable amounts), loyalty.rule (minimum amount tax mode), loyalty.reward discount product, product matrix grids, sale_margin fields, purchase bill-to-order wizard and down-payment section.

### D3 Source, technical and workflow logic
Control and data flow. Choose carrier -> rate adapted to tax mapping (VDR-U32-C130) -> delivery line with explicit taxes (VDR-U32-C128, VDR-U32-C129). Claim reward -> discountable amounts per tax set (VDR-U32-C138, VDR-U32-C139) -> reward lines per tax set (VDR-U32-C136, VDR-U32-C137) -> reward line tax compute maps again (VDR-U32-C143). Gift card: sale untaxed (VDR-U32-C142), redemption takes product taxes (VDR-U32-C140).
State diagram (A -> B [trigger]):
- order -> delivery line added [carrier selected] (VDR-U32-C128)
- order -> reward lines added [reward claimed] (VDR-U32-C136)
- reward lines -> recomputed taxes [line tax compute] (VDR-U32-C143)
- vendor bill lines -> purchase order lines or down-payment lines [wizard] (VDR-U32-C152, VDR-U32-C153)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Delivery line with mapped product tax; discount reward per tax set; free shipping line mirrors delivery tax (VDR-U32-C128, VDR-U32-C132, VDR-U32-C136). |
| 2 Reversal / cancel / negative path | Reward lines are removed with the reward; negative reward prices reduce tax per set (VDR-U32-C136, VDR-U32-C137). |
| 3 Multi-company / data scope | Taxes filtered by order company (VDR-U32-C128, VDR-U32-C135). |
| 4 Side effects & cross-module triggers | Thresholds on tax-inclusive totals (VDR-U32-C131, VDR-U32-C145); margin uses untaxed amounts (VDR-U32-C149, VDR-U32-C150). |
| 5 Configuration & optionality | Minimum amount tax mode (VDR-U32-C144); product taxes on reward and gift-card products (VDR-U32-C141, VDR-U32-C142, VDR-U32-C146). |
| 6 Validation & constraints | Discount capped at order total (VDR-U32-C137); fixed taxes not discounted (VDR-U32-C139). |
| 7 Roles & permissions | Seeded ACL counts (VDR-U32-C134, VDR-U32-C146). |
| 8 Scheduled / automated behavior | None found. |
| 9 Exception & failure behavior | Nothing to discount raises error (source line 577, not claimed separately). |
| 10 Accounting, stock, audit, security & compliance implications | Gift-card sale untaxed and redemption taxed asymmetry in the dump (VDR-U32-C140, VDR-U32-C142, VDR-U32-C146); double mapping RT (VDR-U32-C143). |

### DB reconciliation (configuration only)
Restored DB: one gift-card program and reward; reward discount product with 7% sale tax; gift-card product without sale tax; delivery products with 7% (VDR-U32-C146, VDR-U32-C134).

### Unknown / Runtime list
- RT: numeric gift-card redemption and stacked rewards (VDR-U32-C155)
- RT: second fiscal-position mapping on reward lines (VDR-U32-C143)
- Not read: loyalty point accrual and program eligibility logic beyond tax touch points.

## CAP-U32-06 Down-payment lines: tax effects

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: invoice an advance with tax proportional to the order and neutralise it on the final invoice; U05 covered the flow. Tax effect: the advance is a percentage or fixed tax-inclusive share of the order, split per tax set with exact per-tax rounding (VDR-U32-C158, VDR-U32-C159, VDR-U32-C160, VDR-U32-C161, VDR-U32-C162).

### D2 Architecture, data and object relationships
Objects: AccountTax down-payment preparation and reduction helpers, sale.advance.payment.inv wizard, sale.order.line (is_downpayment, extra_tax_data), final invoice lines with reversed tax data.

### D3 Source, technical and workflow logic
Control and data flow. Wizard -> base lines from order (VDR-U32-C158) -> dispatch non-discountable taxes (VDR-U32-C156, VDR-U32-C157) -> reduce to target (VDR-U32-C159, VDR-U32-C160, VDR-U32-C161) -> smooth deltas (VDR-U32-C162) -> fix manual amounts (VDR-U32-C163) -> order lines and invoice -> final invoice reverses (VDR-U32-C164).
State diagram (A -> B [trigger]):
- order confirmed -> advance lines and invoice draft [wizard] (VDR-U32-C158)
- advance posted -> advance deducted [final invoice, quantity -1] (VDR-U32-C164)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Percentage advance -> per tax set lines -> posted -> deducted on final invoice (VDR-U32-C159, VDR-U32-C164). |
| 2 Reversal / cancel / negative path | Final invoice reverses stored tax data (VDR-U32-C164); advance invoice deletion removes advance lines (U05-C094). |
| 3 Multi-company / data scope | Company account mapping by fiscal position (U05-C113); not set in dump (VDR-U32-C165). |
| 4 Side effects & cross-module triggers | Order lines created with manual tax data (VDR-U32-C163). |
| 5 Configuration & optionality | Percentage or fixed (VDR-U32-C159, VDR-U32-C160). |
| 6 Validation & constraints | Positive amount only (U05-C101). |
| 7 Roles & permissions | Per U05. |
| 8 Scheduled / automated behavior | Auto invoicing after payment per U05-C015. |
| 9 Exception & failure behavior | Zero total yields zero percentage (source line 3737, within VDR-U32-C160). |
| 10 Accounting, stock, audit, security & compliance implications | Tax of an advance stated at advance time and reversed at the same amounts (VDR-U32-C164); fixed and formula taxes folded into base (VDR-U32-C157). |

### DB reconciliation (configuration only)
Restored DB: company down-payment account not set (VDR-U32-C165).

### Unknown / Runtime list
- RT: advance with global discount, early-payment discount or withholding (VDR-U32-C166)

## CAP-U32-07 Early-payment discount tax-base redistribution with several taxes

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: verify how an early-payment discount redistributes the tax base when several taxes apply. U12 covered the discount amounts. Result: mixed mode groups by tax set at invoicing (VDR-U32-C169, VDR-U32-C170, VDR-U32-C171, VDR-U32-C172); included mode recomputes each tax at payment per distribution line (VDR-U32-C177, VDR-U32-C178, VDR-U32-C179, VDR-U32-C180, VDR-U32-C181); order and invoice builders differ (VDR-U32-C174, VDR-U32-C175).

### D2 Architecture, data and object relationships
Objects: payment term discount fields, account.move.line epd key and needed values, account.move early-payment base lines and counterpart helper, sale.order early-payment base lines, payment register wizard.

### D3 Source, technical and workflow logic
Control and data flow. Mixed: invoice lines -> groups by account, analytics and tax set -> discount per group -> spread over lines -> epd pair lines -> tax engine on reduced base (VDR-U32-C169, VDR-U32-C170, VDR-U32-C171, VDR-U32-C172, VDR-U32-C173). Included: payment -> helper recomputes taxes on remaining share -> base and tax adjustment lines on payment entry (VDR-U32-C177, VDR-U32-C178, VDR-U32-C179, VDR-U32-C180, VDR-U32-C181, VDR-U32-C182).
State diagram (A -> B [trigger]):
- invoice saved (mixed) -> discount pair lines [payment term] (VDR-U32-C167, VDR-U32-C171)
- payment within discount window (included) -> adjustment lines [register payment] (VDR-U32-C177, VDR-U32-C179)
- exchange difference -> exchange lines [payment foreign currency] (VDR-U32-C183)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Included mode at payment adjusts base and each tax (VDR-U32-C177, VDR-U32-C179). |
| 2 Reversal / cancel / negative path | Unreconcile removes adjustment lines with the payment (U12 relied on). |
| 3 Multi-company / data scope | Loss and gain accounts per company (VDR-U32-C182). |
| 4 Side effects & cross-module triggers | Shared helper with payment wizard (VDR-U32-C020, VDR-U32-C021). |
| 5 Configuration & optionality | Modes included, excluded, mixed; DB all included (VDR-U32-C167). |
| 6 Validation & constraints | Fixed taxes removed (VDR-U32-C168, VDR-U32-C178). |
| 7 Roles & permissions | Per U12. |
| 8 Scheduled / automated behavior | None. |
| 9 Exception & failure behavior | Rounding remainder to biggest base line (VDR-U32-C181); exchange lines (VDR-U32-C183). |
| 10 Accounting, stock, audit, security & compliance implications | Tax reduced per distribution line with reversed tags (VDR-U32-C179); order versus invoice rounding RT (VDR-U32-C175); purchase order builder unknown (VDR-U32-C176). |

### DB reconciliation (configuration only)
Restored DB: both early-payment accounts set; all payment terms included mode (TXA1-C280) (VDR-U32-C182, VDR-U32-C167).

### Unknown / Runtime list
- RT: numeric equality for several taxes, lines, instalments, foreign currency (VDR-U32-C184, VDR-U32-C175)
- UNKNOWN: purchase order builder (VDR-U32-C176)

## CAP-U32-08 Fiscal-position and partner-driven tax mapping at order, purchase, bill and expense hand-offs

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: show where the fiscal position is evaluated for each hand-off and what a foreign customer or vendor receives. TXA1 and U25 own the finder; this capability traces each caller. Result: sales order computes it, purchase order sets it by onchange, bills compute it, expenses use none (VDR-U32-C185, VDR-U32-C189, VDR-U32-C195, VDR-U32-C196); the dump has no position so taxes stay product defaults (VDR-U32-C199).

### D2 Architecture, data and object relationships
Objects: account.fiscal.position finder, sale.order, sale.order.line, purchase.order, purchase.order.line, account.move, account.move.line, hr.expense, stock rule, requisition, e-invoice import, partner VAT validation hook.

### D3 Source, technical and workflow logic
Control and data flow. Sale: stored compute -> lines mapped -> update-taxes action (VDR-U32-C185, VDR-U32-C186, VDR-U32-C187) -> invoice (VDR-U32-C188). Purchase: onchange -> lines by explicit routine (VDR-U32-C189, VDR-U32-C190, VDR-U32-C191) -> bill (VDR-U32-C192); replenishment and requisition evaluate themselves (VDR-U32-C193, VDR-U32-C194). Bill: compute from partner and delivery partner (VDR-U32-C195); line taxes mapped (VDR-U32-C197). Expense: none (VDR-U32-C196).
State diagram (A -> B [trigger]):
- partner or address changed -> position recomputed [sale, bill] (VDR-U32-C185, VDR-U32-C195)
- position changed on order with lines -> update prompt [sale] (VDR-U32-C185, VDR-U32-C186)
- vendor chosen -> position set [purchase onchange] (VDR-U32-C189)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | No position in the dump: taxes are product defaults (VDR-U32-C199). |
| 2 Reversal / cancel / negative path | Credit notes copy the document position (TXA2 relied on). |
| 3 Multi-company / data scope | Finder runs with the document company (VDR-U32-C185, VDR-U32-C193, VDR-U32-C195). |
| 4 Side effects & cross-module triggers | Position drives tax and account mapping (VDR-U32-C187, VDR-U32-C197); import tax search (VDR-U32-C201). |
| 5 Configuration & optionality | Manual partner position wins (U25-C187); receipt default position (VDR-U32-C195). |
| 6 Validation & constraints | VAT-required validation hook (VDR-U32-C200); European prefix logic (VDR-U32-C198). |
| 7 Roles & permissions | Per TXA1 and U25. |
| 8 Scheduled / automated behavior | None. |
| 9 Exception & failure behavior | No country on partner gives no position (U25-C189). |
| 10 Accounting, stock, audit, security & compliance implications | Foreign customer or vendor needs manual tax choice in the dump (VDR-U32-C199); expenses have no partner-driven mapping (VDR-U32-C196). |

### DB reconciliation (configuration only)
Restored DB: 0 fiscal positions, no default receipt position (VDR-U32-C199).

### Unknown / Runtime list
- RT: configured positions for foreign customers and vendors (VDR-U32-C202)
- RT: finder with numeric Thai tax ids (VDR-U32-C198)

## CAP-U32-09 Optional tax add-ons not installed: calculation and entry-effect depth (formula tax, withholding on payment, tag update, debit note, VAT validation)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: add tax-calculation and entry-effect depth for the add-ons that TXC counted but did not read in depth, without repeating U23. All five are uninstalled in the dump. U23 claims relied on: C009, C025, C058, C059, C075, C078, C113, C129, C139..C165, C177, C179, C185.

### D2 Architecture, data and object relationships
Objects: account_tax_python (code amount type), l10n_account_withholding_tax (withholding lines, engine flag), account_update_tax_tags (SQL re-tagging), account_debit_note (copy wizard), base_vat (finder hook).

### D3 Source, technical and workflow logic
Control and data flow. Formula tax joins the engine in the fixed pass (VDR-U32-C203, VDR-U32-C204, VDR-U32-C205, VDR-U32-C206); withholding add-on filters taxes out of document batching and re-enters them with the flag (VDR-U32-C209, VDR-U32-C210, VDR-U32-C211, VDR-U32-C212, VDR-U32-C213); tag tool re-tags by repartition line (VDR-U32-C214, VDR-U32-C215); debit note copies (VDR-U32-C216, VDR-U32-C217, VDR-U32-C218); VAT hook (VDR-U32-C200).
State diagram (A -> B [trigger]):
- document computed -> formula tax amount added [fixed pass] (VDR-U32-C204)
- invoice posted -> payment with withholding lines -> withholding entry items [register payment] (VDR-U32-C210, VDR-U32-C211, VDR-U32-C212)
- tax lines -> re-tagged [tool run] (VDR-U32-C214)
- posted invoice -> draft debit note [wizard] (VDR-U32-C216)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Formula in fixed pass (VDR-U32-C204); withholding on payment entry reproduces typed values (VDR-U32-C211). |
| 2 Reversal / cancel / negative path | Tag tool irreversible (U23-C174); debit note is a new document (VDR-U32-C216). |
| 3 Multi-company / data scope | Withholding lines company-checked (U23-C049); tag tool per company (VDR-U32-C214). |
| 4 Side effects & cross-module triggers | Excise-type export treatment of formula taxes (VDR-U32-C208). |
| 5 Configuration & optionality | All uninstalled; flags and columns absent in the dump (U23). |
| 6 Validation & constraints | Formula checks (U23-C142..C152); price-included flag not constrained (VDR-U32-C207). |
| 7 Roles & permissions | Per U23. |
| 8 Scheduled / automated behavior | None except base_vat cron (U23-C125). |
| 9 Exception & failure behavior | Division by zero yields 0 (U23-C155). |
| 10 Accounting, stock, audit, security & compliance implications | Withholding tax lines carry tags and accounts (VDR-U32-C212); tag tool changes tags only (VDR-U32-C215). |

### DB reconciliation (configuration only)
Restored DB: all five uninstalled; no columns or models (U23-C060, C098, C165, C190).

### Unknown / Runtime list
- RT: numeric effects after installation (VDR-U32-C219, VDR-U32-C207)

## CAP-U32-10 Other entry generators that carry no tax: cut-off, accrual and price-difference lines

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Business purpose: complete the sweep of paths that create entries without tax. Cut-off and reclassification, accrual and price-difference lines were checked for tax content (VDR-U32-C220, VDR-U32-C221, VDR-U32-C222, VDR-U32-C224).

### D2 Architecture, data and object relationships
Objects: account.automatic.entry.wizard, account.accrued.orders.wizard, purchase_stock bill price-difference lines.

### D3 Source, technical and workflow logic
Control and data flow. Wizard runs with computed taxes suppressed (VDR-U32-C220) -> lines without tax data (VDR-U32-C221); accrual uses untaxed values (VDR-U32-C222) and fiscal-position account (VDR-U32-C223); price-difference lines empty tax set (VDR-U32-C224).
State diagram (A -> B [trigger]):
- selected lines -> transfer entry [wizard action] (VDR-U32-C220, VDR-U32-C221)
- orders -> accrual entry and reversal [wizard] (VDR-U32-C222)

### Ten-dimension table

| # / Dimension | Finding (claims) |
|---|---|
| 1 Happy path | Entries created without tax (VDR-U32-C221, VDR-U32-C222). |
| 2 Reversal / cancel / negative path | Cut-off entries are built as opposite lines on the source account and the accrual account (VDR-U32-C221); accrual reversal behaviour was not read. |
| 3 Multi-company / data scope | Accrual company on the order (VDR-U32-C223). |
| 4 Side effects & cross-module triggers | Account mapping by fiscal position (VDR-U32-C223). |
| 5 Configuration & optionality | Wizards optional. |
| 6 Validation & constraints | Not read in depth (lock-safe date helper only seen by name). |
| 7 Roles & permissions | Per U11. |
| 8 Scheduled / automated behavior | None. |
| 9 Exception & failure behavior | Not read in depth. |
| 10 Accounting, stock, audit, security & compliance implications | No tax tags on these lines (VDR-U32-C221, VDR-U32-C224); tax report unaffected by reclassification (RT, VDR-U32-C225). |

### DB reconciliation (configuration only)
Configuration only; no data.

### Unknown / Runtime list
- RT: tax report effect of reclassifying taxed base lines (VDR-U32-C225)

## REGISTER: Function Catalog

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Entry points / triggers | Claim-IDs | Statutory link (statutory-register id or n/a) | Native status |
|---|---|---|---|---|---|---|---|
| U32-F01 | Create an untaxed entry from a bank statement line (liquidity plus suspense) | 1, 7 | FUNCTION MAPPING REQUIRED | statement line create or import; post at creation | VDR-U32-C007, VDR-U32-C008, VDR-U32-C009, VDR-U32-C011, VDR-U32-C015 | n/a (requirement not derived) | PARTIAL |
| U32-F02 | Store taxes on reconciliation presets (configuration only) | 1 | FUNCTION MAPPING REQUIRED | reconcile model form | VDR-U32-C001, VDR-U32-C002, VDR-U32-C003, VDR-U32-C004, VDR-U32-C005, VDR-U32-C022 | n/a (requirement not derived) | NATIVE GAP / EXTENSION REQUIRED |
| U32-F03 | Add tax to a bank-originated entry through classification (bank fees, interest, other) | 1, 7 | FUNCTION MAPPING REQUIRED | manual edit of posted bank entry; external reconciliation tool | VDR-U32-C006, VDR-U32-C010, VDR-U32-C012, VDR-U32-C013, VDR-U32-C014, VDR-U32-C024 | n/a (requirement not derived) | NATIVE GAP / EXTENSION REQUIRED |
| U32-F04 | Create cash-basis tax entries when a bank line settles a document | 1, 5, 7 | PCO-F01 (date claim only) | partial reconcile of document and bank line | VDR-U32-C017, VDR-U32-C018, VDR-U32-C019 | S05-01, S05-02 (link only) | NATIVE |
| U32-F05 | Convert foreign-currency bank lines (date or bank-given rate), without tax | 1, 6 | FUNCTION MAPPING REQUIRED | statement line create and edit | VDR-U32-C015, VDR-U32-C016 | S12-01, S12-03 (link only) | PARTIAL |
| U32-F06 | Register a payment with a write-off (untaxed) or with an early-payment discount (taxed) | 1, 7 | FUNCTION MAPPING REQUIRED | payment register wizard | VDR-U32-C020, VDR-U32-C021 | S05-05 (link only) | NATIVE |
| U32-F07 | Compute expense tax as tax-included and split untaxed amount | 1, 2, 6 | FUNCTION MAPPING REQUIRED | expense form fields and inverses | VDR-U32-C025, VDR-U32-C026, VDR-U32-C028, VDR-U32-C029, VDR-U32-C030, VDR-U32-C031, VDR-U32-C032, VDR-U32-C050 | S04-02 (link only) | NATIVE |
| U32-F08 | Post employee-paid expenses as purchase receipts with tax lines per expense | 2, 7, 12 | FUNCTION MAPPING REQUIRED | expense post action | VDR-U32-C033, VDR-U32-C034, VDR-U32-C035, VDR-U32-C036, VDR-U32-C037, VDR-U32-C038, VDR-U32-C039, VDR-U32-C047 | S04-02, S06-01 (link only) | PARTIAL |
| U32-F09 | Post a company-paid expense as an entry with engine tax lines | 2, 7 | FUNCTION MAPPING REQUIRED | expense post action (company paid) | VDR-U32-C040, VDR-U32-C041, VDR-U32-C042, VDR-U32-C043, VDR-U32-C044, VDR-U32-C045 | S04-02 (link only) | PARTIAL |
| U32-F10 | Split an expense and cancel or reverse its receipt | 2, 7 | FUNCTION MAPPING REQUIRED | split wizard; receipt cancel and reversal | VDR-U32-C046, VDR-U32-C048, VDR-U32-C049 | n/a | NATIVE |
| U32-F11 | Re-invoice an expense with product customer taxes and a price from list or cost | 2, 8, 12 | FUNCTION MAPPING REQUIRED | expense line with order; reinvoice routine | VDR-U32-C053, VDR-U32-C054, VDR-U32-C055, VDR-U32-C056, VDR-U32-C057, VDR-U32-C058 | n/a | PARTIAL |
| U32-F12 | Allocate landed costs from untaxed bill lines and post an untaxed entry (real-time valuation) | 12 | GRV-F05 | bill button; landed cost validate | VDR-U32-C060, VDR-U32-C061, VDR-U32-C062, VDR-U32-C063, VDR-U32-C064, VDR-U32-C065, VDR-U32-C066, VDR-U32-C067, VDR-U32-C068, VDR-U32-C069, VDR-U32-C070, VDR-U32-C082 | n/a | NATIVE |
| U32-F13 | Tax handling in manufacturing, subcontracting and manufacturing WIP documents (NO TAX HANDLING FOUND) | 12 | MFG-F03 (WIP entry claims) | WIP wizard; subcontract purchase and receipt | VDR-U32-C071, VDR-U32-C072, VDR-U32-C073, VDR-U32-C074, VDR-U32-C075, VDR-U32-C076, VDR-U32-C077, VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081 | n/a (requirement not derived) | UNKNOWN |
| U32-F14 | Classify taxes for e-invoicing (category and exemption reason) | 3, 4, 9 | FUNCTION MAPPING REQUIRED | tax form; export prediction | VDR-U32-C084, VDR-U32-C085, VDR-U32-C086, VDR-U32-C087, VDR-U32-C088, VDR-U32-C089, VDR-U32-C090, VDR-U32-C091, VDR-U32-C092, VDR-U32-C093, VDR-U32-C094, VDR-U32-C095, VDR-U32-C096 | S03-01, S03-03, S14-05 (link only) | PARTIAL |
| U32-F15 | Build tax and withholding totals and monetary totals of an exported document | 4, 6 | FUNCTION MAPPING REQUIRED | send flow; export builder | VDR-U32-C097, VDR-U32-C098, VDR-U32-C099, VDR-U32-C100, VDR-U32-C101, VDR-U32-C102, VDR-U32-C103, VDR-U32-C104, VDR-U32-C105, VDR-U32-C110 | S13-02, S14-05 (link only) | PARTIAL |
| U32-F16 | Validate taxes and tax presence before export; report constraint messages | 4, 6 | FUNCTION MAPPING REQUIRED | export builder start; constraint hook | VDR-U32-C106, VDR-U32-C107, VDR-U32-C108, VDR-U32-C109, VDR-U32-C115, VDR-U32-C116 | S14-04 (link only) | PARTIAL |
| U32-F17 | Thai electronic tax invoice file format and revenue-authority reporting | 4, 9 | FUNCTION MAPPING REQUIRED | partner format selection; none bound to Thailand | VDR-U32-C111, VDR-U32-C112, VDR-U32-C113, VDR-U32-C114, VDR-U32-C125, VDR-U32-C127 | S14-01, S14-05, S14-07 (link only) | NATIVE GAP / EXTENSION REQUIRED |
| U32-F18 | Match imported e-invoice taxes and align tax totals | 1, 7, 12 | FUNCTION MAPPING REQUIRED | import of UBL or CII file | VDR-U32-C119, VDR-U32-C120, VDR-U32-C121, VDR-U32-C122, VDR-U32-C123, VDR-U32-C124 | n/a | NATIVE |
| U32-F19 | Tax a delivery charge line (explicit taxes, provider price adapted) | 2, 12 | FUNCTION MAPPING REQUIRED | carrier selection on order | VDR-U32-C128, VDR-U32-C129, VDR-U32-C130, VDR-U32-C134 | n/a | NATIVE |
| U32-F20 | Split a loyalty discount per tax set and cap it | 1, 3, 6 | FUNCTION MAPPING REQUIRED | reward claim on order | VDR-U32-C136, VDR-U32-C137, VDR-U32-C138, VDR-U32-C139 | S05-05 (link only) | NATIVE |
| U32-F21 | Tax free-product and free-shipping reward lines | 1, 12 | FUNCTION MAPPING REQUIRED | reward claim on order | VDR-U32-C132, VDR-U32-C135, VDR-U32-C133 | n/a | PARTIAL |
| U32-F22 | Sell and redeem gift cards with tax | 1, 3 | FUNCTION MAPPING REQUIRED | gift-card product sale; reward claim | VDR-U32-C140, VDR-U32-C141, VDR-U32-C142, VDR-U32-C146 | n/a | PARTIAL |
| U32-F23 | Compare loyalty and shipping thresholds on tax-inclusive or tax-exclusive amounts | 12 | FUNCTION MAPPING REQUIRED | reward eligibility; carrier rate | VDR-U32-C131, VDR-U32-C144, VDR-U32-C145 | n/a | NATIVE |
| U32-F24 | Matrix-created lines and margin views stay tax-neutral | 12 | FUNCTION MAPPING REQUIRED | matrix entry; margin fields | VDR-U32-C147, VDR-U32-C148, VDR-U32-C149, VDR-U32-C150, VDR-U32-C151 | n/a | NATIVE |
| U32-F25 | Convert vendor-bill lines into purchase lines or down-payment lines | 12 | FUNCTION MAPPING REQUIRED | bill-to-purchase-order wizard | VDR-U32-C152, VDR-U32-C153, VDR-U32-C154 | n/a | PARTIAL |
| U32-F26 | Compute and invoice an advance with per-tax rounding; reverse on final invoice | 1, 3, 12 | FUNCTION MAPPING REQUIRED | advance wizard; final invoice | VDR-U32-C156, VDR-U32-C157, VDR-U32-C158, VDR-U32-C159, VDR-U32-C160, VDR-U32-C161, VDR-U32-C162, VDR-U32-C163, VDR-U32-C164, VDR-U32-C165 | S05-01, S05-02 (link only) | NATIVE |
| U32-F27 | Reduce tax at invoicing through an early-payment discount (mixed mode) | 1, 6 | FUNCTION MAPPING REQUIRED | payment term; invoice save; order totals | VDR-U32-C167, VDR-U32-C168, VDR-U32-C169, VDR-U32-C170, VDR-U32-C171, VDR-U32-C172, VDR-U32-C173, VDR-U32-C174, VDR-U32-C175 | S05-05 (link only) | NATIVE |
| U32-F28 | Adjust base and each tax at payment through an early-payment discount (included mode) | 1, 6, 7 | FUNCTION MAPPING REQUIRED | register payment | VDR-U32-C177, VDR-U32-C178, VDR-U32-C179, VDR-U32-C180, VDR-U32-C181, VDR-U32-C182, VDR-U32-C183 | S05-05 (link only) | NATIVE |
| U32-F29 | Early supplier discount on purchase orders | 1 | FUNCTION MAPPING REQUIRED | none found | VDR-U32-C176, VDR-U32-C184 | S05-05 (link only) | UNKNOWN |
| U32-F30 | Evaluate the fiscal position for sales hand-offs | 8, 12 | FUNCTION MAPPING REQUIRED | order partner change; update taxes; invoice creation | VDR-U32-C185, VDR-U32-C186, VDR-U32-C187, VDR-U32-C188 | n/a | NATIVE |
| U32-F31 | Evaluate the fiscal position for purchase hand-offs | 8, 12 | FUNCTION MAPPING REQUIRED | vendor onchange; replenishment; requisition; bill creation | VDR-U32-C189, VDR-U32-C190, VDR-U32-C191, VDR-U32-C192, VDR-U32-C193, VDR-U32-C194 | n/a | PARTIAL |
| U32-F32 | Evaluate the fiscal position for bills, receipts and expenses | 8 | FUNCTION MAPPING REQUIRED | bill compute; line default taxes; expense | VDR-U32-C195, VDR-U32-C196, VDR-U32-C197 | n/a | PARTIAL |
| U32-F33 | Tax mapping for foreign customers and vendors on Thai flows | 3, 8 | FUNCTION MAPPING REQUIRED | fiscal position setup (none seeded) | VDR-U32-C198, VDR-U32-C199, VDR-U32-C201, VDR-U32-C202 | S03-01, S10-01 (link only) | PARTIAL |
| U32-F34 | Partner tax-number validation influence on fiscal position (optional add-on) | 8, 9 | FUNCTION MAPPING REQUIRED | finder hook | VDR-U32-C200 | n/a | PARTIAL |
| U32-F35 | Formula-defined tax calculation (optional, uninstalled) | 1 | FUNCTION MAPPING REQUIRED | tax form; engine fixed pass | VDR-U32-C203, VDR-U32-C204, VDR-U32-C205, VDR-U32-C206, VDR-U32-C207, VDR-U32-C208 | n/a | PARTIAL |
| U32-F36 | Withholding on payment calculation and entry items (optional, uninstalled) | 1, 9 | FUNCTION MAPPING REQUIRED | register payment; payment form | VDR-U32-C209, VDR-U32-C210, VDR-U32-C211, VDR-U32-C212, VDR-U32-C213 | S13-02, S13-03 (link only) | PARTIAL |
| U32-F37 | Re-tag existing tax items (optional, uninstalled) | 7, 9 | FUNCTION MAPPING REQUIRED | settings tool in developer mode | VDR-U32-C214, VDR-U32-C215 | n/a | PARTIAL |
| U32-F38 | Issue a debit note (optional, uninstalled) and its tax effect | 4 | FUNCTION MAPPING REQUIRED | button on posted invoice | VDR-U32-C216, VDR-U32-C217, VDR-U32-C218 | S07-01 (link only) | PARTIAL |
| U32-F39 | Cut-off and reclassification entries without tax | 7 | FUNCTION MAPPING REQUIRED | automatic entry wizard | VDR-U32-C220, VDR-U32-C221, VDR-U32-C225 | n/a | NATIVE |
| U32-F40 | Accrual entries from orders without tax; price-difference lines without tax | 7, 12 | FUNCTION MAPPING REQUIRED | accrual wizard; bill posting under automated valuation | VDR-U32-C222, VDR-U32-C223, VDR-U32-C224, VDR-U32-C076 | n/a | NATIVE |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Claim-IDs | Class |
|---|---|---|---|---|
| U32-BR-01 | A bank statement line creates an untaxed entry of bank item plus suspense item and the entry is posted at creation. | always | VDR-U32-C007, VDR-U32-C008, VDR-U32-C009, VDR-U32-C011 | FACT |
| U32-BR-02 | Tax lines are synchronised only for draft entries, so a posted bank entry is not re-taxed by edits. | bank entry posted | VDR-U32-C010 | FACT |
| U32-BR-03 | Editing amount, currency, partner or label of a bank line deletes all items other than bank and suspense. | statement line edit | VDR-U32-C012, VDR-U32-C013, VDR-U32-C014 | FACT |
| U32-BR-04 | Reconcile-model taxes are stored configuration with no Community consumer and they make a tax non-deletable. | reconcile model with taxes | VDR-U32-C001, VDR-U32-C003, VDR-U32-C004, VDR-U32-C005 | INFERENCE |
| U32-BR-05 | A payment write-off is untaxed; an early-payment write-off comes from the tax-aware helper. | register payment | VDR-U32-C021, VDR-U32-C020 | FACT |
| U32-BR-06 | Cash-basis entries arise from every partial match, bank lines included, dated at settlement but after the fiscal lock. | cash-basis tax on document | VDR-U32-C017, VDR-U32-C018 | INFERENCE |
| U32-BR-07 | Every tax on an expense behaves as price-included; the typed total is split into untaxed and tax amounts. | expense | VDR-U32-C025, VDR-U32-C028, VDR-U32-C032, VDR-U32-C036, VDR-U32-C037 | FACT |
| U32-BR-08 | Expense tax lines are generated per expense, never merged across expenses of one receipt. | receipt with several expenses | VDR-U32-C038, VDR-U32-C039 | FACT |
| U32-BR-09 | Foreign-currency expense tax is recomputed in company currency on the converted total; receipts are in company currency. | foreign-currency expense | VDR-U32-C029, VDR-U32-C030, VDR-U32-C031, VDR-U32-C034 | FACT |
| U32-BR-10 | Company-paid expense: one entry per expense, base item absorbs rounding so the entry equals the expense total. | company-paid expense | VDR-U32-C040, VDR-U32-C042, VDR-U32-C043, VDR-U32-C045 | FACT |
| U32-BR-11 | A re-invoiced expense is billed with product customer taxes mapped by the order position, not with expense taxes. | reinvoice policy sales price or cost | VDR-U32-C053, VDR-U32-C054, VDR-U32-C055, VDR-U32-C056, VDR-U32-C057 | FACT |
| U32-BR-12 | A landed cost uses the bill line before tax and posts an untaxed entry, only for real-time valued products and FIFO or average costing. | landed cost | VDR-U32-C060, VDR-U32-C063, VDR-U32-C064, VDR-U32-C066, VDR-U32-C068 | FACT |
| U32-BR-13 | Manufacturing, subcontracting and manufacturing WIP documents contain no tax logic (NO TAX HANDLING FOUND). | always | VDR-U32-C073, VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081 | INFERENCE |
| U32-BR-14 | Price-difference lines on a vendor bill carry no tax. | automated valuation | VDR-U32-C076, VDR-U32-C224 | FACT |
| U32-BR-15 | E-invoice category defaults: same-country zero tax is E, negative factor AE, other S; export or intra-community codes need an EEA party. | no code on tax | VDR-U32-C089, VDR-U32-C090, VDR-U32-C091, VDR-U32-C092, VDR-U32-C093 | FACT |
| U32-BR-16 | Percent taxes with negative amount are withholding in an export and are netted from the inclusive total. | export of document with such taxes | VDR-U32-C099, VDR-U32-C101, VDR-U32-C102, VDR-U32-C103 | FACT |
| U32-BR-17 | Each invoice line other than sections, notes and combo products needs at least one tax before export. | export | VDR-U32-C109 | FACT |
| U32-BR-18 | No export format is bound to Thailand. | always | VDR-U32-C111, VDR-U32-C112, VDR-U32-C113 | FACT |
| U32-BR-19 | Imported taxes are matched by type, use, amount and optional name, country and code; unmatched ones are logged. | e-invoice import | VDR-U32-C119, VDR-U32-C120, VDR-U32-C121, VDR-U32-C122 | FACT |
| U32-BR-20 | Imported tax totals within 0.03 of the computed tax overwrite the tax lines when every tax was matched. | e-invoice import | VDR-U32-C123, VDR-U32-C124 | FACT |
| U32-BR-21 | Delivery lines carry the carrier product taxes mapped by the order position, set explicitly on the line. | delivery line | VDR-U32-C128, VDR-U32-C129, VDR-U32-C130 | FACT |
| U32-BR-22 | A loyalty discount creates one negative line per non-fixed tax set, capped at the order total. | discount reward | VDR-U32-C136, VDR-U32-C137, VDR-U32-C138, VDR-U32-C139 | FACT |
| U32-BR-23 | Gift cards are sold untaxed by default and redeemed with the reward product taxes as tax-included. | gift-card program | VDR-U32-C140, VDR-U32-C141, VDR-U32-C142 | FACT |
| U32-BR-24 | Thresholds compare tax-inclusive totals unless the loyalty rule says tax-excluded. | free shipping, loyalty rule | VDR-U32-C131, VDR-U32-C144, VDR-U32-C145 | FACT |
| U32-BR-25 | An advance is a tax-inclusive share of the order, with per-tax rounded shares, reversed with stored tax data on the final invoice. | down payment | VDR-U32-C159, VDR-U32-C160, VDR-U32-C161, VDR-U32-C163, VDR-U32-C164 | FACT |
| U32-BR-26 | Mixed early-payment discount groups by account, analytics and the whole tax set and reduces the tax on that set; fixed and formula taxes are excluded. | payment term mixed | VDR-U32-C168, VDR-U32-C169, VDR-U32-C170, VDR-U32-C171 | FACT |
| U32-BR-27 | Included early-payment discount recomputes each tax at payment per distribution line, with reversed tags and a remainder on the biggest base line. | payment term included | VDR-U32-C177, VDR-U32-C178, VDR-U32-C179, VDR-U32-C180, VDR-U32-C181 | FACT |
| U32-BR-28 | Sales order fiscal position is a stored compute; purchase order position is set by onchange; bills compute it; expenses use none. | always | VDR-U32-C185, VDR-U32-C189, VDR-U32-C195, VDR-U32-C196 | FACT |
| U32-BR-29 | Purchase line taxes come from explicit routines, so lines created by code keep no tax unless set. | programmatic purchase line | VDR-U32-C190, VDR-U32-C191 | INFERENCE |
| U32-BR-30 | A formula tax is evaluated in the fixed pass and is excluded from discounts, advances and early-payment splits. | account_tax_python installed | VDR-U32-C203, VDR-U32-C204, VDR-U32-C206, VDR-U32-C156 | FACT |
| U32-BR-31 | Withholding on payment taxes are filtered out of document computation and re-enter through the payment lines with manual amounts. | l10n_account_withholding_tax installed | VDR-U32-C209, VDR-U32-C210, VDR-U32-C211 | FACT |
| U32-BR-32 | Cut-off and reclassification lines carry no tax, tag or distribution line. | automatic entry wizard | VDR-U32-C220, VDR-U32-C221 | FACT |

## REGISTER: Source and Override Map

| Concept | Base definition (module:file:line) | Overrides in installed Community modules (module:file:line) | Effective-behaviour condition | Claim-IDs |
|---|---|---|---|---|
| Expense tax base line | account:models/account_tax.py (engine prepare-base-line hook, see TXA1-C039) | hr_expense:models/hr_expense.py:1738; hr_expense:models/account_tax.py:24; hr_expense:models/account_move.py:94; hr_expense:models/account_move_line.py:36 | hr_expense installed (dump: yes) | VDR-U32-C032, VDR-U32-C036, VDR-U32-C037, VDR-U32-C039 |
| Base-to-tax line SQL mapping | account:models/account_move_line_tax_details.py:23 | hr_expense:models/account_move_line.py:41 | hr_expense installed | VDR-U32-C038 |
| Tax amount evaluation (fixed pass) | account:models/account_tax.py:1082 | account_tax_python:models/account_tax.py:116 | account_tax_python installed (dump: no) | VDR-U32-C203, VDR-U32-C204 |
| Tax filter before batching | account:models/account_tax.py:939 | l10n_account_withholding_tax:models/account_tax.py:71 | withholding add-on installed (dump: no) | VDR-U32-C209 |
| Discount eligibility of taxes | account:models/account_tax.py:3150 | none installed; code type (uninstalled add-on) is excluded by the base test | always | VDR-U32-C156, VDR-U32-C206 |
| Sale line taxes | sale:models/sale_order_line.py:544 | sale_loyalty:models/sale_order_line.py:35 (reward lines); delivery:models/sale_order.py:230 (explicit delivery taxes) | loyalty and delivery installed (dump: yes) | VDR-U32-C187, VDR-U32-C129, VDR-U32-C143 |
| Reward line values | sale_loyalty:models/sale_order.py:536 | sale_loyalty_delivery:models/sale_order.py:32 | free shipping reward | VDR-U32-C132, VDR-U32-C136 |
| Down-payment tax lines | account:models/account_tax.py:4020 | sale:wizard/sale_make_invoice_advance.py:138 | sale installed | VDR-U32-C158, VDR-U32-C159, VDR-U32-C163 |
| Fiscal position finder | account:models/partner.py:247 | base_vat:models/res_partner.py:962 (hook; uninstalled) | base_vat installed (dump: no) | VDR-U32-C198, VDR-U32-C200 |
| Fiscal position on documents | account:models/account_move.py:1037 | sale:models/sale_order.py:412; sale:models/sale_order.py:1439; purchase:models/purchase_order.py:445; purchase:models/purchase_order.py:938 | always | VDR-U32-C185, VDR-U32-C188, VDR-U32-C189, VDR-U32-C192, VDR-U32-C195 |
| Reinvoice sale line values | sale:models/account_move_line.py:175 | sale_expense:models/account_move_line.py:35 | sale_expense installed | VDR-U32-C053, VDR-U32-C054, VDR-U32-C055, VDR-U32-C057 |
| Landed cost from bill | stock_landed_costs:models/account_move.py:21 | mrp_landed_costs:models/stock_landed_cost.py (target only); mrp_subcontracting_landed_costs:models/stock_landed_cost.py (target only) | installed in dump | VDR-U32-C060, VDR-U32-C071, VDR-U32-C072 |
| Statement line entry creation | account:models/account_bank_statement_line.py:367 | account_payment:models/account_bank_statement_line.py:9 (U12-C260, no super) | always | VDR-U32-C007, VDR-U32-C009 |
| E-invoice tax category prediction | account_edi_ubl_cii:models/account_edi_common.py:405 | none in installed Community modules (foreign format classes not read) | always | VDR-U32-C089, VDR-U32-C090, VDR-U32-C091, VDR-U32-C092, VDR-U32-C093 |
| E-invoice tax totals | account_edi_ubl_cii:models/account_edi_ubl.py:2178 | account_edi_ubl_cii:models/account_edi_xml_ubl_bis3.py:128; legacy builder account_edi_ubl_cii:models/account_edi_xml_ubl_20.py:712 | format chosen per partner | VDR-U32-C102, VDR-U32-C110 |
| Early-payment lines | account:models/account_move_line.py:1077 | sale:models/sale_order.py:531 (order-level analogue) | mixed mode | VDR-U32-C167, VDR-U32-C169, VDR-U32-C174 |
| EDI post-time loop | account:models/account_move.py (post routine, TXA2) | account_edi:models/account_move.py:233 | journals with formats (dump: none) | VDR-U32-C117 |

## REGISTER: State and Reversal

| Document/entity | State or event | Trigger | Reversal / cancel / correction path | Blocked when | Claim-IDs |
|---|---|---|---|---|---|
| Bank statement entry | created -> posted | statement line create | undo reconciliation restores default lines | fiscal or tax lock fails the undo | VDR-U32-C009, VDR-U32-C023 |
| Bank statement entry (edited) | posted, lines rewritten | edit of amount, currency, partner, label | none; other lines deleted | more than one liquidity or suspense line raises error | VDR-U32-C012, VDR-U32-C014 |
| Reconcile model | manual or automated trigger (no consumer) | user action | copy; archive | deleting a tax while a preset uses it | VDR-U32-C003, VDR-U32-C004, VDR-U32-C005 |
| Employee receipt | draft -> posted | expense post | cancel or reversal clears the expense link; credit note | locks (generic) | VDR-U32-C046, VDR-U32-C047 |
| Company-paid entry | created with payment | expense post | one entry per expense; reversal generic | second company-paid expense on same entry | VDR-U32-C045, VDR-U32-C044 |
| Landed cost | draft -> posted; cancel blocked after validation | validate | negative landed cost | validated cost cannot be cancelled | VDR-U32-C069, VDR-U32-C070 |
| Exported e-invoice file | generated at send; errors do not block | send action | regenerate not traced | tax missing on a line; invalid tax structure | VDR-U32-C106, VDR-U32-C109, VDR-U32-C115, VDR-U32-C116 |
| Legacy EDI document | to send -> sent -> cancel requested | post, reset, cancel | request EDI cancellation instead of reset | sent documents block reset (TXA2) | VDR-U32-C117 |
| Advance (down payment) lines | order lines created -> deducted | advance wizard; final invoice | final invoice quantity -1 with reversed tax data | none | VDR-U32-C158, VDR-U32-C164 |
| Reward lines | created -> remapped | reward claim; line tax compute | removed with the reward | nothing to discount | VDR-U32-C136, VDR-U32-C143 |
| Early-payment lines | created at invoice save or at payment | payment term; register payment | removed with unreconcile (U12) | none | VDR-U32-C171, VDR-U32-C179 |
| Debit note (uninstalled) | draft copy | wizard on posted invoice | new document only | not posted or already a debit note (U23-C071, C072) | VDR-U32-C216 |
| Tag update (uninstalled) | irreversible SQL update | tool | none (backup advised, U23-C174) | none beyond multi-parent check (U23-C175) | VDR-U32-C214, VDR-U32-C215 |

## REGISTER: Accounting Impact

Valuation context: periodic valuation (manual period) as in the dump; the automated (perpetual) path is RT.

| Event | Entries created or changed (neutral) | Tax lines / tags / accounts affected | Period/lock/date effect | Reversal effect | Claim-IDs |
|---|---|---|---|---|---|
| Bank statement line created | liquidity item and suspense item, posted | none | entry date = line date; lock shift per generic posting | undo reconciliation rewrites to default lines | VDR-U32-C007, VDR-U32-C009 |
| Bank statement line edited | entry rewritten to liquidity and suspense; other items deleted | tax and base items deleted if present | none | none | VDR-U32-C012 |
| Settlement of an invoice with a cash-basis tax (incl. bank line) | cash-basis entry in the cash-basis journal | tax items and tags move at settlement | settlement date, after the user fiscal lock date | follows partial removal | VDR-U32-C017, VDR-U32-C018 |
| Employee-paid expense posted | purchase receipt: expense debit with base, tax items per expense, payable to employee | input tax items and tags per expense | invoice date today; lock shift | credit-note reversal | VDR-U32-C033, VDR-U32-C035, VDR-U32-C038, VDR-U32-C039, VDR-U32-C047 |
| Company-paid expense posted | entry: expense base, engine tax items, outstanding payment item | tax items with tags (cash-basis tags included) | expense date | reversal generic | VDR-U32-C040, VDR-U32-C041, VDR-U32-C042, VDR-U32-C043 |
| Landed cost validated (real-time only) | debit stock valuation, credit cost account | none | cost date; lock shift | negative landed cost | VDR-U32-C063, VDR-U32-C065, VDR-U32-C066, VDR-U32-C069, VDR-U32-C070 |
| Manufacturing WIP entry | WIP debit, stock valuation and overhead credit, automatic reversal | none | posting date and reversal date after it | reversal entry | VDR-U32-C073, VDR-U32-C074 |
| E-invoice export | no entry | none | none | n/a | VDR-U32-C102, VDR-U32-C115 |
| Delivery line invoiced | invoice line with delivery taxes | tax items from the delivery tax set | none | credit note | VDR-U32-C128, VDR-U32-C129 |
| Loyalty discount invoiced | negative lines per tax set | tax reduced per tax set | none | credit note | VDR-U32-C136, VDR-U32-C137 |
| Advance invoiced and deducted | receivable debit, advance credit, tax items per tax set; final invoice quantity -1 | tax per tax set, reversed at same amounts | none | final invoice reverses | VDR-U32-C158, VDR-U32-C161, VDR-U32-C164 |
| Early discount at invoicing (mixed) | discount pair lines; tax recomputed on reduced base per tax set | tax items reduced | none | reset or credit note | VDR-U32-C169, VDR-U32-C171, VDR-U32-C173 |
| Early discount at payment (included) | payment entry with base adjustment and tax adjustment items | tax items adjusted per distribution line with reversed tags | payment date | unreconcile (U12) | VDR-U32-C177, VDR-U32-C179, VDR-U32-C182 |
| Cut-off or reclassification | two lines per source line (account and accrual account) | none (no tags) | new date; lock-safe | opposite lines | VDR-U32-C220, VDR-U32-C221 |
| Accrual from orders | untaxed accrual lines and reversal | none | accrual date | reversal | VDR-U32-C222, VDR-U32-C223 |
| Withholding on payment (uninstalled) | tax items 'WH Tax', base item pair | tax items with tags; base grid on counterpart item (inferred) | payment date | U23 untraced | VDR-U32-C211, VDR-U32-C212, VDR-U32-C213 |

## Neutral statement trace (neutral id -> claims that support it)

| Neutral-ref | Capability | Section | Supporting claims |
|---|---|---|---|
| N-U32-001 | CAP-U32-01 | WHAT | VDR-U32-C007, VDR-U32-C011 |
| N-U32-002 | CAP-U32-01 | WHAT | VDR-U32-C001 |
| N-U32-003 | CAP-U32-01 | WHY | VDR-U32-C008 |
| N-U32-004 | CAP-U32-01 | BUSINESS RULE | VDR-U32-C003 |
| N-U32-005 | CAP-U32-01 | BUSINESS RULE | VDR-U32-C004, VDR-U32-C005 |
| N-U32-006 | CAP-U32-01 | BUSINESS RULE | VDR-U32-C021 |
| N-U32-007 | CAP-U32-01 | STATE | VDR-U32-C009, VDR-U32-C010 |
| N-U32-008 | CAP-U32-01 | STATE | VDR-U32-C023 |
| N-U32-009 | CAP-U32-01 | OPTIONALITY | VDR-U32-C002 |
| N-U32-010 | CAP-U32-01 | OPTIONALITY | VDR-U32-C022 |
| N-U32-011 | CAP-U32-01 | DEPENDENCY | VDR-U32-C017, VDR-U32-C018, VDR-U32-C019 |
| N-U32-012 | CAP-U32-01 | DEPENDENCY | VDR-U32-C020 |
| N-U32-013 | CAP-U32-01 | CONSTRAINT | VDR-U32-C012, VDR-U32-C013, VDR-U32-C014 |
| N-U32-014 | CAP-U32-01 | RISK | VDR-U32-C015, VDR-U32-C016 |
| N-U32-015 | CAP-U32-01 | UNKNOWN | VDR-U32-C006, VDR-U32-C024 |
| N-U32-016 | CAP-U32-02 | WHAT | VDR-U32-C025, VDR-U32-C028, VDR-U32-C032, VDR-U32-C036, VDR-U32-C037 |
| N-U32-017 | CAP-U32-02 | WHAT | VDR-U32-C033, VDR-U32-C035, VDR-U32-C045 |
| N-U32-018 | CAP-U32-02 | WHY | VDR-U32-C034 |
| N-U32-019 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C029, VDR-U32-C030, VDR-U32-C031 |
| N-U32-020 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C038, VDR-U32-C039 |
| N-U32-021 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C026, VDR-U32-C050 |
| N-U32-022 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C053, VDR-U32-C054, VDR-U32-C055, VDR-U32-C056, VDR-U32-C057 |
| N-U32-023 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C058 |
| N-U32-024 | CAP-U32-02 | BUSINESS RULE | VDR-U32-C040, VDR-U32-C042, VDR-U32-C043 |
| N-U32-025 | CAP-U32-02 | STATE | VDR-U32-C046 |
| N-U32-026 | CAP-U32-02 | OPTIONALITY | VDR-U32-C027 |
| N-U32-027 | CAP-U32-02 | OPTIONALITY | VDR-U32-C051, VDR-U32-C052 |
| N-U32-028 | CAP-U32-02 | DEPENDENCY | VDR-U32-C047 |
| N-U32-029 | CAP-U32-02 | CONSTRAINT | VDR-U32-C048, VDR-U32-C049 |
| N-U32-030 | CAP-U32-02 | RISK | VDR-U32-C044 |
| N-U32-031 | CAP-U32-02 | UNKNOWN | VDR-U32-C041, VDR-U32-C059 |
| N-U32-032 | CAP-U32-03 | WHAT | VDR-U32-C060, VDR-U32-C061, VDR-U32-C062 |
| N-U32-033 | CAP-U32-03 | WHAT | VDR-U32-C078, VDR-U32-C079, VDR-U32-C080, VDR-U32-C081, VDR-U32-C071, VDR-U32-C072, VDR-U32-C073, VDR-U32-C074 |
| N-U32-034 | CAP-U32-03 | WHY | VDR-U32-C065 |
| N-U32-035 | CAP-U32-03 | BUSINESS RULE | VDR-U32-C063, VDR-U32-C064 |
| N-U32-036 | CAP-U32-03 | BUSINESS RULE | VDR-U32-C069 |
| N-U32-037 | CAP-U32-03 | STATE | VDR-U32-C070 |
| N-U32-038 | CAP-U32-03 | OPTIONALITY | VDR-U32-C066, VDR-U32-C067 |
| N-U32-039 | CAP-U32-03 | OPTIONALITY | VDR-U32-C082 |
| N-U32-040 | CAP-U32-03 | DEPENDENCY | VDR-U32-C068 |
| N-U32-041 | CAP-U32-03 | DEPENDENCY | VDR-U32-C075, VDR-U32-C076 |
| N-U32-042 | CAP-U32-03 | CONSTRAINT | VDR-U32-C077 |
| N-U32-043 | CAP-U32-03 | RISK | VDR-U32-C078 |
| N-U32-044 | CAP-U32-03 | UNKNOWN | VDR-U32-C083 |
| N-U32-045 | CAP-U32-04 | WHAT | VDR-U32-C084, VDR-U32-C085, VDR-U32-C086, VDR-U32-C087 |
| N-U32-046 | CAP-U32-04 | WHAT | VDR-U32-C089, VDR-U32-C090, VDR-U32-C091, VDR-U32-C092, VDR-U32-C093 |
| N-U32-047 | CAP-U32-04 | WHY | VDR-U32-C095, VDR-U32-C096 |
| N-U32-048 | CAP-U32-04 | BUSINESS RULE | VDR-U32-C099, VDR-U32-C100, VDR-U32-C101, VDR-U32-C102, VDR-U32-C103 |
| N-U32-049 | CAP-U32-04 | BUSINESS RULE | VDR-U32-C097 |
| N-U32-050 | CAP-U32-04 | BUSINESS RULE | VDR-U32-C098 |
| N-U32-051 | CAP-U32-04 | BUSINESS RULE | VDR-U32-C109 |
| N-U32-052 | CAP-U32-04 | BUSINESS RULE | VDR-U32-C104, VDR-U32-C105 |
| N-U32-053 | CAP-U32-04 | STATE | VDR-U32-C115, VDR-U32-C116 |
| N-U32-054 | CAP-U32-04 | STATE | VDR-U32-C117, VDR-U32-C118, VDR-U32-C126 |
| N-U32-055 | CAP-U32-04 | OPTIONALITY | VDR-U32-C111, VDR-U32-C112, VDR-U32-C113, VDR-U32-C114 |
| N-U32-056 | CAP-U32-04 | OPTIONALITY | VDR-U32-C088, VDR-U32-C094 |
| N-U32-057 | CAP-U32-04 | DEPENDENCY | VDR-U32-C119, VDR-U32-C120, VDR-U32-C121, VDR-U32-C122 |
| N-U32-058 | CAP-U32-04 | CONSTRAINT | VDR-U32-C106, VDR-U32-C107 |
| N-U32-059 | CAP-U32-04 | CONSTRAINT | VDR-U32-C123, VDR-U32-C124 |
| N-U32-060 | CAP-U32-04 | RISK | VDR-U32-C110 |
| N-U32-061 | CAP-U32-04 | UNKNOWN | VDR-U32-C125, VDR-U32-C108, VDR-U32-C127 |
| N-U32-062 | CAP-U32-05 | WHAT | VDR-U32-C128, VDR-U32-C129, VDR-U32-C130 |
| N-U32-063 | CAP-U32-05 | WHAT | VDR-U32-C132, VDR-U32-C135, VDR-U32-C136 |
| N-U32-064 | CAP-U32-05 | WHY | VDR-U32-C137 |
| N-U32-065 | CAP-U32-05 | BUSINESS RULE | VDR-U32-C139 |
| N-U32-066 | CAP-U32-05 | BUSINESS RULE | VDR-U32-C138 |
| N-U32-067 | CAP-U32-05 | BUSINESS RULE | VDR-U32-C140, VDR-U32-C141, VDR-U32-C142 |
| N-U32-068 | CAP-U32-05 | BUSINESS RULE | VDR-U32-C131, VDR-U32-C133, VDR-U32-C144, VDR-U32-C145 |
| N-U32-069 | CAP-U32-05 | BUSINESS RULE | VDR-U32-C149, VDR-U32-C150 |
| N-U32-070 | CAP-U32-05 | STATE | VDR-U32-C147, VDR-U32-C148 |
| N-U32-071 | CAP-U32-05 | OPTIONALITY | VDR-U32-C146, VDR-U32-C134 |
| N-U32-072 | CAP-U32-05 | DEPENDENCY | VDR-U32-C152, VDR-U32-C153, VDR-U32-C154 |
| N-U32-073 | CAP-U32-05 | CONSTRAINT | VDR-U32-C151 |
| N-U32-074 | CAP-U32-05 | RISK | VDR-U32-C143 |
| N-U32-075 | CAP-U32-05 | UNKNOWN | VDR-U32-C155 |
| N-U32-076 | CAP-U32-06 | WHAT | VDR-U32-C158, VDR-U32-C159, VDR-U32-C160 |
| N-U32-077 | CAP-U32-06 | WHY | VDR-U32-C164 |
| N-U32-078 | CAP-U32-06 | BUSINESS RULE | VDR-U32-C156, VDR-U32-C157 |
| N-U32-079 | CAP-U32-06 | BUSINESS RULE | VDR-U32-C161, VDR-U32-C162, VDR-U32-C163 |
| N-U32-080 | CAP-U32-06 | OPTIONALITY | VDR-U32-C165 |
| N-U32-081 | CAP-U32-06 | UNKNOWN | VDR-U32-C166 |
| N-U32-082 | CAP-U32-07 | WHAT | VDR-U32-C167, VDR-U32-C177 |
| N-U32-083 | CAP-U32-07 | BUSINESS RULE | VDR-U32-C169, VDR-U32-C170, VDR-U32-C171, VDR-U32-C172, VDR-U32-C173 |
| N-U32-084 | CAP-U32-07 | BUSINESS RULE | VDR-U32-C168, VDR-U32-C178 |
| N-U32-085 | CAP-U32-07 | BUSINESS RULE | VDR-U32-C179, VDR-U32-C180, VDR-U32-C181 |
| N-U32-086 | CAP-U32-07 | BUSINESS RULE | VDR-U32-C182, VDR-U32-C183 |
| N-U32-087 | CAP-U32-07 | STATE | VDR-U32-C174 |
| N-U32-088 | CAP-U32-07 | RISK | VDR-U32-C175 |
| N-U32-089 | CAP-U32-07 | UNKNOWN | VDR-U32-C176, VDR-U32-C184 |
| N-U32-090 | CAP-U32-08 | WHAT | VDR-U32-C185, VDR-U32-C189, VDR-U32-C195, VDR-U32-C196 |
| N-U32-091 | CAP-U32-08 | BUSINESS RULE | VDR-U32-C186, VDR-U32-C187 |
| N-U32-092 | CAP-U32-08 | BUSINESS RULE | VDR-U32-C188, VDR-U32-C192 |
| N-U32-093 | CAP-U32-08 | BUSINESS RULE | VDR-U32-C190, VDR-U32-C191 |
| N-U32-094 | CAP-U32-08 | BUSINESS RULE | VDR-U32-C193, VDR-U32-C194 |
| N-U32-095 | CAP-U32-08 | BUSINESS RULE | VDR-U32-C197 |
| N-U32-096 | CAP-U32-08 | DEPENDENCY | VDR-U32-C201 |
| N-U32-097 | CAP-U32-08 | CONSTRAINT | VDR-U32-C198 |
| N-U32-098 | CAP-U32-08 | OPTIONALITY | VDR-U32-C199 |
| N-U32-099 | CAP-U32-08 | DEPENDENCY | VDR-U32-C200 |
| N-U32-100 | CAP-U32-08 | RISK | VDR-U32-C198 |
| N-U32-101 | CAP-U32-08 | UNKNOWN | VDR-U32-C202 |
| N-U32-102 | CAP-U32-09 | WHAT | VDR-U32-C203 |
| N-U32-103 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C204, VDR-U32-C205, VDR-U32-C206 |
| N-U32-104 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C208 |
| N-U32-105 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C209, VDR-U32-C210, VDR-U32-C211 |
| N-U32-106 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C212, VDR-U32-C213 |
| N-U32-107 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C214, VDR-U32-C215 |
| N-U32-108 | CAP-U32-09 | BUSINESS RULE | VDR-U32-C216, VDR-U32-C217, VDR-U32-C218 |
| N-U32-109 | CAP-U32-09 | RISK | VDR-U32-C207 |
| N-U32-110 | CAP-U32-09 | UNKNOWN | VDR-U32-C219 |
| N-U32-111 | CAP-U32-10 | WHAT | VDR-U32-C220, VDR-U32-C221 |
| N-U32-112 | CAP-U32-10 | WHAT | VDR-U32-C222, VDR-U32-C223 |
| N-U32-113 | CAP-U32-10 | BUSINESS RULE | VDR-U32-C224 |
| N-U32-114 | CAP-U32-10 | UNKNOWN | VDR-U32-C225 |

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U32-C001 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:52 | tax_ids = fields.Many2many( | FACT | always | — | Each reconcile-model line can carry a set of taxes (relation table account_reconcile_model_line_account_tax_rel, company-checked, ondelete restrict) in addition to account, partner, label and analytic distribution. | N-U32-002 |
| VDR-U32-C002 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:29 | Percentage of statement line | INFERENCE | always | — | Model-line amount types are fixed, percentage of balance, percentage of statement line and amount-from-label (lines 25-34); the 203-line file has no price-include or tax-included flag, so whether a model-line amount already contains tax is not configurable on the model (inferred from absence). | N-U32-009 |
| VDR-U32-C003 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:178 | def action_reconcile_stat | INFERENCE | always | — | The model class contains only compute, constraint, set-trigger, statistics and copy methods (lines 161-203); no method turns model lines into journal items or applies their taxes. U12-C258 and U12-C259 (engine outside Community) are relied on; this unit adds that the model-line taxes are stored configuration with no Community consumer. | N-U32-004 |
| VDR-U32-C004 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:373 | ('account_reconcile_model_line_ids', '!=', False) | FACT | always | — | A tax referenced by a reconcile-model line is counted as used by the tax is-used computation (lines 368-375). | N-U32-005 |
| VDR-U32-C005 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5133 | You cannot delete taxes that are | FACT | always | — | The tax unlink guard raises a ValidationError for used taxes and suggests archiving; a tax referenced only by a reconcile-model line therefore cannot be deleted. Extensions (e.g. expenses) add their own use link to the same computation. | N-U32-005 |
| VDR-U32-C006 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3547 | 'reconcile_model_id': self.reconcile_model_id.id, | INFERENCE | always | RT | The line-values helper copies reconcile_model_id together with tax_repartition_line_id, tax_ids, tax_tag_ids and group_tax_id (lines 3539-3555); grep over odoo/addons finds no caller, so the consumer (a reconciliation user interface) is outside the studied Community code. | N-U32-015 |
| VDR-U32-C007 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:674 | counterpart_line_vals = { | FACT | always | — | A new statement line receives exactly two journal-item value sets, liquidity and counterpart (suspense account unless counterpart_account_id is supplied); neither contains tax_ids, tax tags or a repartition line, so statement lines are created without tax. | N-U32-001 |
| VDR-U32-C008 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:390 | vals['move_type'] = 'entry' | FACT | always | — | Statement-line creation forces move_type entry, so the statement-line move is a journal entry and not an invoice or receipt. | N-U32-003 |
| VDR-U32-C009 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:420 | st_lines.move_id.action_post() | FACT | always | — | The statement-line entry is posted at creation (U12-C222 relied on). | N-U32-007 |
| VDR-U32-C010 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3365 | if move.state != 'draft': | FACT | always | — | Tax-line synchronisation processes only draft moves; a posted statement-line entry is not re-taxed when its lines are changed. | N-U32-007 |
| VDR-U32-C011 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:985 | self.move_id.is_entry() | FACT | always | — | For entry-type moves (statement-line moves are entries) default line taxes from the account are not applied unless the context asks for account default taxes (lines 981-985). | N-U32-001 |
| VDR-U32-C012 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:826 | line_ids_commands.append((2, line.id)) | FACT | always | — | When payment_ref, amount, amount_currency, foreign currency, currency or partner of a statement line change, the entry is rewritten to liquidity plus suspense and every other line is deleted (command 2); manually added tax or base lines would be discarded. | N-U32-013 |
| VDR-U32-C013 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:703 | other_lines += line | FACT | always | — | Journal items that are neither on the journal default account nor on the suspense account are classified as other lines; tax lines of a statement entry would fall in this class. | N-U32-013 |
| VDR-U32-C014 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:731 | if len(liquidity_lines) != 1: | FACT | always | — | The statement-line synchronisation from the entry requires exactly one liquidity line and at most one suspense line but does not constrain other lines, so an entry may carry base and tax lines after an external reconciliation (U12-C229 relied on). | N-U32-013 |
| VDR-U32-C015 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:659 | company_amount = journal_currency | FACT | always | — | Company-currency amount of a statement line is the journal amount (journal currency equals company currency), or the foreign transaction amount (foreign currency equals company currency), or the journal amount converted at the line date (lines 654-660); no tax is involved in the conversion. | N-U32-014 |
| VDR-U32-C016 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:600 | rate_journal2foreign_curr = | INFERENCE | always | — | The helper that converts counterpart amounts with the bank-provided rates (lines 581-627) takes a currency, a balance and an amount_currency only; it has no tax input, so tax amounts of a taxed counterpart are not recomputed by it (U12-C240 relied on). | N-U32-014 |
| VDR-U32-C017 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:259 | for partial in self: | INFERENCE | always | — | Cash-basis tax entries are collected from every partial reconcile and both of its sides without a check on the kind of counterpart (lines 259-267); matching an invoice that carries cash-basis taxes with a bank statement line would therefore create cash-basis tax entries. | N-U32-011 |
| VDR-U32-C018 | PCO-F01 | account/models/account_partial_reconcile.py:554 | move_date = max(partial_values['settlement_date'] | FACT | always | — | The cash-basis entry date is the settlement date of the partial, moved to the day after the user fiscal lock date when that is later. | N-U32-011 |
| VDR-U32-C019 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection( | OBSERVATION | restored dump | — | Restored DB: all 18 taxes have exigibility on invoice and none on payment; the company flag that shows the cash-basis option is true; so no cash-basis tax entry can arise from statement matching in this configuration (configuration query). | N-U32-011 |
| VDR-U32-C020 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5070 | bank reconciliation widget | INFERENCE | always | — | The early-payment-discount counterpart helper states that it serves the register-payment wizard and the bank reconciliation widget (lines 5069-5071, 5239-5240); the widget is not in Community, the wizard is (account_payment_register.py lines 1023 and 1105). | N-U32-012 |
| VDR-U32-C021 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1044 | 'name': self.writeoff_label, | FACT | always | — | The wizard manual write-off line holds name, account, partner, currency, amount_currency and balance only (lines 1043-1050); it has no tax fields, so payment write-offs are untaxed; with an early-payment discount the write-off lines come from the tax-aware helper (lines 1023-1025). | N-U32-006 |
| VDR-U32-C022 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1195 | @template(model='account.reconcile.model') | OBSERVATION | restored dump | — | Restored DB: two reconcile models exist (trigger manual; one with a label condition), the model-line tax relation table has 0 rows, and there are 0 statements and 0 statement lines; the models are seeded by the chart template (U12-C256). | N-U32-010 |
| VDR-U32-C023 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1882 | st_line.move_id.line_ids._check_tax_lock_date() | FACT | always | — | Undoing the reconciliation of a statement line is applied only when the fiscal and tax lock checks pass; otherwise the statement line is dropped from the undo set (U12-C160 relied on). | N-U32-008 |
| VDR-U32-C024 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: how a reconciliation tool outside the studied code would build taxed lines (rates, rounding, tags, foreign-currency tax) on a bank-statement entry, and the effect of a cash-basis tax matched from a bank line, cannot be resolved from source; resolve with an AWT run in a configuration with a reconciliation tool and a cash-basis tax. | N-U32-015 |
| VDR-U32-C025 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:274 | behave as price-included taxes | FACT | always | — | Expense taxes are a stored, editable many-to-many (table expense_tax) limited to purchase-type taxes and computed from the product; the help text states every tax behaves as price-included on an expense (lines 265-274; U16-C007 relied on). | N-U32-016 |
| VDR-U32-C026 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:574 | taxes only from the same company | FACT | always | — | Default expense taxes are the product vendor taxes filtered with the company domain of the expense (lines 571-575; U16-C009 relied on). | N-U32-021 |
| VDR-U32-C027 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1104 | r.company_id == company | INFERENCE | mail gateway in use | RT | The mail-gateway path sets taxes from the product vendor taxes whose company equals the expense company exactly (line 1104), while the manual path uses the company domain (line 575); behaviour for taxes owned by a parent company is not run. | N-U32-026 |
| VDR-U32-C028 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:600 | expense.untaxed_amount_currency = tax_details['total_excluded_currency'] | FACT | always | — | For the typed total the tax amount and untaxed amount in expense currency come from the tax engine on a base line of unit price equal to the total and quantity 1, so the typed total is treated as tax-included (lines 577-600). | N-U32-016 |
| VDR-U32-C029 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:626 | expense.tax_amount = tax_details['total_included_currency'] - tax_details['total_excluded_currency'] | FACT | always | — | In a multi-currency expense the company-currency tax and untaxed amounts are recomputed by the engine on the company-currency total with the company currency; in a single-currency expense they copy the currency amounts (lines 602-630). | N-U32-019 |
| VDR-U32-C030 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:537 | price_unit=expense.total_amount_currency * expense.currency_rate, | FACT | always | — | In a multi-currency expense the company-currency total is the foreign total multiplied by the expense rate, run through the engine with rate 1 in company currency (lines 535-544), so tax rounding happens in company currency. | N-U32-019 |
| VDR-U32-C031 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:567 | expense.currency_rate = expense.total_amount / expense.total_amount_currency if | FACT | always | — | Writing the company-currency total stores a derived rate and recomputes tax and untaxed amounts, giving the user a custom rate for the expense (lines 548-568; U16-C012 relied on). | N-U32-019 |
| VDR-U32-C032 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1742 | 'special_mode': 'total_included' | FACT | always | — | The expense base line uses the vendor as partner, special mode total-included and the expense rate (lines 1738-1743; U16-C008 relied on). | N-U32-016 |
| VDR-U32-C033 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1619 | 'move_type': 'in_receipt', | FACT | always | — | Employee-paid expenses are posted as purchase receipts whose partner is the employee work contact and whose currency is the company currency (lines 1616-1625). | N-U32-017 |
| VDR-U32-C034 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1622 | 'currency_id': expenses_sudo.company_currency_id.id, | FACT | always | — | The receipt is created in company currency, so a foreign-currency expense is converted at the expense rate before posting and the receipt tax lines are in company currency. | N-U32-018 |
| VDR-U32-C035 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1729 | 'price_unit': self.price_unit, | FACT | always | — | A receipt line carries the expense price_unit (total divided by quantity), quantity, expense link and the expense taxes (lines 1723-1736); with the total-included mode the engine extracts the tax from this price. | N-U32-017 |
| VDR-U32-C036 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:98 | results['special_mode'] = 'total_included' | FACT | always | — | For lines of employee-paid expenses the receipt base line is prepared with special mode total-included (lines 94-99; U16-C121 relied on). | N-U32-016 |
| VDR-U32-C037 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move_line.py:38 | with_context(force_price_include=True) | FACT | always | — | Totals of expense journal items are computed with force_price_include so every tax acts as price-included (lines 36-39; U16-C122 relied on). | N-U32-016 |
| VDR-U32-C038 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move_line.py:42 | base_line.expense_id IS NULL | FACT | always | — | The SQL base-to-tax line mapping used by tax-detail reporting is restricted so a tax line maps only to base lines of the same expense (lines 41-42; base query in account_move_line_tax_details.py lines 83-85). | N-U32-020 |
| VDR-U32-C039 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:39 | results['expense_id'] = base_line['expense_id'].id | FACT | always | — | The base-line grouping key and the tax-line repartition grouping key both include the expense id, so tax lines are generated per expense and not merged across the expenses of one receipt (lines 36-46; U16-C123 relied on). | N-U32-020 |
| VDR-U32-C040 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1639 | rate = abs(self.total_amount_currency / self.total_amount) | FACT | always | — | For company-paid expenses the engine runs on the foreign total with the rate implied by the expense totals, then accounting data (tags, accounts) are added and tax lines prepared (lines 1638-1650). | N-U32-024 |
| VDR-U32-C041 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1649 | include_caba_tags=self.payment_mode == 'company_account' | FACT | always | — | Cash-basis tags are requested only for company-paid expenses (line 1649; U16-C137 relied on); Thai withholding on expense lines was not traced by U16 and is not traced here. | N-U32-031 |
| VDR-U32-C042 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1676 | base_move_line['balance'] = self.total_amount - total_tax_line_balance | FACT | always | — | In the company-paid entry the base line balance is set to the expense total minus the sum of tax-line balances, so the base absorbs any rounding difference and the entry total equals the expense total. | N-U32-024 |
| VDR-U32-C043 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1682 | 'balance': -self.total_amount, | FACT | always | — | The outstanding-payment line of the company-paid entry carries minus the expense total in company currency (lines 1679-1686). | N-U32-024 |
| VDR-U32-C044 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1707 | 'line_ids': [Command.create(line) for line in move_lines], | INFERENCE | always | RT | The company-paid entry is built from raw line dictionaries with no move_type key and a context cleaned of defaults (line 1582), so it is a miscellaneous entry whose tax lines carry repartition lines and tags but which has no vendor-bill or receipt document type; execution not run. | N-U32-030 |
| VDR-U32-C045 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:35 | Each expense paid by the company | FACT | always | — | A constraint allows only one expense on a journal entry that holds a company-paid expense (lines 30-35); employee-paid expenses of one employee may share a receipt. | N-U32-017 |
| VDR-U32-C046 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:103 | self.filtered('expense_ids').write({'expense_ids': [Command.clear()]}) | FACT | always | — | Cancelling the receipt, or reversing it (override of the reversal method), clears the expense link so the expense can be reimbursed again; the reversal itself is the generic credit-note reversal (lines 101-112). | N-U32-025 |
| VDR-U32-C047 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1562 | company.expense_journal_id | FACT | always | — | The receipt journal is the company expense journal, else the first purchase journal of the company (lines 1558-1563); receipts are posted with the invoice date set to today and the generic post routine (lines 1564-1575). | N-U32-028 |
| VDR-U32-C048 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_split.py:72 | taxes = split.tax_ids.with_context(force_price_include=True).compute_all( | FACT | always | — | The split wizard computes each split tax with the legacy compute_all in forced price-included mode (lines 69-78); each split keeps the expense taxes (hr_expense.py line 1496). | N-U32-029 |
| VDR-U32-C049 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1489 | price_round_up = float_round(half_price | FACT | always | — | A split divides the expense total in two halves rounded up and down at the currency precision so that the parts add up to the original total (lines 1486-1505). | N-U32-029 |
| VDR-U32-C050 | FUNCTION MAPPING REQUIRED | hr_expense/models/product_template.py:15 | result['supplier_taxes_id'] = False | FACT | always | — | When a product is created from the expense context the default vendor tax is blanked (lines 11-16). | N-U32-021 |
| VDR-U32-C051 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_data.xml:5 | expense_product_meal | OBSERVATION | restored dump | — | Restored DB: the seven expense products carry the 7% sale tax and the 7% purchase tax; expense_policy is sales_price for Meals and Mileage, cost for Travel and Communication, none for Gifts and Expenses; the data file itself sets no taxes. | N-U32-027 |
| VDR-U32-C052 | FUNCTION MAPPING REQUIRED | hr_expense/models/res_company.py:9 | expense_journal_id = fields.Many2one( | OBSERVATION | restored dump | — | Restored DB: the company expense journal is set (purchase-type journal); 0 expenses exist; hr_expense seeds 14 ACL rows, 12 record rules and 1 cron. | N-U32-027 |
| VDR-U32-C053 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:181 | fpos = order.fiscal_position_id or | FACT | always | — | The reinvoice line evaluates the fiscal position as the order position, else the finder for the order partner (line 181), then maps the product customer taxes (lines 182-183); U16-C182 relied on. | N-U32-022 |
| VDR-U32-C054 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:190 | 'tax_ids': [x.id for x in taxes], | FACT | always | — | The reinvoiced sale line receives the mapped product customer taxes and a zero discount; the expense taxes are not carried over, so billed tax may differ from recovered input tax. | N-U32-022 |
| VDR-U32-C055 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:206 | amount = (self.credit or 0.0) - | FACT | always | — | With policy cost the reinvoice unit price is the absolute value of the receipt line balance divided by quantity (lines 205-229); for an employee-paid receipt built in total-included mode that balance is the untaxed amount, so the billed price is inferred to be tax-excluded. | N-U32-022 |
| VDR-U32-C056 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:209 | return order.pricelist_id._get_product_price( | FACT | always | — | With policy sales_price the reinvoice price is the pricelist price of the product at the order date, independent of the expense amount (lines 208-214). | N-U32-022 |
| VDR-U32-C057 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:16 | self.expense_id.product_id.expense_policy in {'sales_price', 'cost'} | FACT | always | — | An expense journal item is reinvoiced only when the product policy is sales_price or cost, the expense has an order and the line is a product line (lines 9-20). | N-U32-022 |
| VDR-U32-C058 | FUNCTION MAPPING REQUIRED | sale_expense_margin/models/sale_order_line.py:16 | product_cost = expense.untaxed_amount_currency / (expense.quantity or | FACT | always | — | The margin cost of a reinvoiced expense line is the untaxed expense amount per unit, so margin ignores recoverable tax (lines 11-19). | N-U32-023 |
| VDR-U32-C059 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: numeric tax results of foreign-currency expenses with a custom rate, company-paid expense entries as seen by the input-tax ledger, and Thai withholding on expense lines were not executed; resolve with an AWT run on representative expenses. | N-U32-031 |
| VDR-U32-C060 | GRV-F05 | stock_landed_costs/models/account_move.py:35 | 'price_unit': sign * l.company_currency_id.round(l.price_subtotal / l.currency_rate), | FACT | always | — | A landed-cost line created from a vendor bill takes the bill line price_subtotal (before tax) divided by the invoice currency rate and rounded in company currency, with the sign reversed for vendor refunds; bill taxes are not part of the landed cost. | N-U32-032 |
| VDR-U32-C061 | GRV-F05 | stock_landed_costs/models/account_move.py:36 | 'split_method': l.product_id.split_method_landed_cost or 'equal', | FACT | always | — | Each cost line copies product, name, expense account, amount and split method only (lines 31-37); no tax, repartition or tag information is copied. | N-U32-032 |
| VDR-U32-C062 | GRV-F05 | stock_landed_costs/models/account_move.py:26 | landed_costs_lines = self.line_ids.filtered(lambda line: line.is_landed_costs_line) | FACT | always | — | Only bill lines flagged as landed-cost lines are mirrored; the flag is set by onchange from the product landed-cost option and is reset for non-service products by a second onchange (lines 60-76). | N-U32-032 |
| VDR-U32-C063 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:119 | 'move_type': 'entry', | FACT | always | — | Validating a landed cost builds a journal entry of type entry in the chosen journal at the cost date; the lines are produced by the valuation-adjustment lines and have no tax_ids. | N-U32-035 |
| VDR-U32-C064 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:364 | 'quantity': 0, | FACT | always | — | Entry line values contain only name, product, quantity 0 and the account and amount set later (lines 360-365); there is no tax field. | N-U32-035 |
| VDR-U32-C065 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:368 | In real time the vendor bill | FACT | always | — | The entry debits the stock valuation account and credits the cost account by additional cost times remaining quantity over quantity; a negative cost reverses the entry (lines 367-388); the bill keeps its own tax lines unchanged, so tax on the bill is not re-booked by the landed cost. | N-U32-034 |
| VDR-U32-C066 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:123 | Products with manual inventory valuation are | FACT | valuation periodic (dump) | — | Only products with real-time valuation produce entry lines; for periodic valuation (the dump) no journal entry is created and the cost is applied through the move value update (lines 121-125, 145-152). | N-U32-038 |
| VDR-U32-C067 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:152 | cost.valuation_adjustment_lines.move_id._set_value() | FACT | always | — | After validation the stock-move values are refreshed through the move value routine whether or not an entry was created. | N-U32-038 |
| VDR-U32-C068 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:177 | FIFO or average costing method | FACT | cost method standard (dump) | — | Landed costs apply only to moves of products with FIFO or average costing; otherwise a user error is raised (lines 159-177); the dump uses standard cost, so landed costs cannot be applied in the dump configuration. | N-U32-040 |
| VDR-U32-C069 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:100 | Validated landed costs cannot be cancelled | FACT | always | — | A validated landed cost cannot be cancelled; the reversal path is a negative landed cost (lines 97-101). | N-U32-036 |
| VDR-U32-C070 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:151 | move._post() | FACT | always | — | The landed-cost entry is posted with the generic posting routine, so lock-date date shifting applies (U10-R2 relied on). | N-U32-037 |
| VDR-U32-C071 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:11 | ('manufacturing', "Manufacturing Orders") | FACT | always | — | Manufacturing orders are an additional landed-cost target selecting finished moves (and cost-bearing by-products); no tax logic is present in the file. | N-U32-033 |
| VDR-U32-C072 | GRV-F05 | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:14 | if move.is_subcontract: | FACT | always | — | For subcontracted moves the landed cost targets the origin moves of the subcontract; no tax logic is present in the file. | N-U32-033 |
| VDR-U32-C073 | MFG-F03 | mrp_account/wizard/mrp_wip_accounting.py:131 | 'move_type': 'entry', | FACT | always | — | The manufacturing WIP wizard creates an entry with lines holding label, account, debit and credit only, posts it and reverses it at the reversal date (lines 120-146); no tax fields exist on the lines. | N-U32-033 |
| VDR-U32-C074 | MFG-F03 | mrp_account/wizard/mrp_wip_accounting.py:88 | Command.create({ | FACT | always | — | The proposed WIP lines are component value (credit stock valuation), overhead (credit overhead account) and total (debit WIP account) (lines 76-103). | N-U32-033 |
| VDR-U32-C075 | FUNCTION MAPPING REQUIRED | mrp_subcontracting_purchase/models/account_move_line.py:10 | price_unit_val_dif, relevant_qty = super()._get_price_unit_val_dif_and_relevant_qty() | FACT | anglo-saxon accounting on (dump: off) | — | For standard-cost products with a purchase line the price difference used by bill valuation is increased by the subcontract component cost per produced unit (lines 9-22). | N-U32-041 |
| VDR-U32-C076 | FUNCTION MAPPING REQUIRED | purchase_stock/models/account_invoice.py:85 | 'tax_ids': [], | FACT | anglo-saxon accounting on (dump: off) | — | Price-difference and cost lines generated on a vendor bill are created with an empty tax set (lines 82-107), so they carry no tax. | N-U32-041 |
| VDR-U32-C077 | FUNCTION MAPPING REQUIRED | purchase_mrp/report/mrp_report_mo_overview.py:43 | rounding_method="round_globally", | FACT | always | — | The manufacturing-order overview computes the cost of replenished purchase lines with total_void of the line taxes (lines 37-44, 90-97), i.e. taxes without an account become cost, in a report only. | N-U32-042 |
| VDR-U32-C078 | FUNCTION MAPPING REQUIRED | stock_landed_costs/__manifest__.py:13 | 'depends' | INFERENCE | always | — | Search record: a case-insensitive search for tax and fiscal in the python, xml and csv files of stock_landed_costs, mrp_landed_costs, mrp_subcontracting_landed_costs, mrp, mrp_account, mrp_subcontracting, mrp_subcontracting_account, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping, sale_mrp and sale_mrp_margin returned no match; purchase_mrp returned only the two report-level compute_all calls. NO TAX HANDLING FOUND in these modules. | N-U32-033 |
| VDR-U32-C079 | FUNCTION MAPPING REQUIRED | mrp_account/__manifest__.py:21 | 'depends' | INFERENCE | always | — | mrp_account depends on mrp and stock_account only and contains no tax computation or tax posting (same search record as above). | N-U32-033 |
| VDR-U32-C080 | FUNCTION MAPPING REQUIRED | mrp_subcontracting/__manifest__.py:10 | 'depends' | INFERENCE | always | — | mrp_subcontracting depends on mrp only; the subcontract service is bought through a normal purchase order whose taxes follow the purchase path (U06 relied on); this module posts no tax. | N-U32-033 |
| VDR-U32-C081 | FUNCTION MAPPING REQUIRED | mrp_subcontracting_account/__manifest__.py:11 | 'depends' | INFERENCE | always | — | mrp_subcontracting_account adds valuation links between subcontracting and accounting without tax logic (same search record). | N-U32-033 |
| VDR-U32-C082 | FUNCTION MAPPING REQUIRED | stock_landed_costs/__manifest__.py:13 | 'depends' | OBSERVATION | restored dump | — | Restored DB: stock_landed_costs, mrp_landed_costs, mrp_subcontracting_landed_costs, mrp_account, mrp_subcontracting and mrp_subcontracting_account are installed; 0 landed costs exist; stock_landed_costs seeds 3 ACL rows and 1 record rule, mrp_account 6 ACL rows, mrp_subcontracting 17 ACL rows and 13 rules, mrp_subcontracting_account 2 ACL rows and 2 rules. | N-U32-039 |
| VDR-U32-C083 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of landed costs and subcontracting service bills carrying non-deductible tax or withholding, and the real-time-valuation entries, were not executed; the dump uses periodic valuation and standard cost; resolve with an AWT run in a perpetual-valuation configuration. | N-U32-044 |
| VDR-U32-C084 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:7 | ubl_cii_tax_category_code = fields.Selection( | FACT | always | — | A tax carries an optional e-invoicing category code chosen from AE, E, S, Z, G, O, K, L, M and B (reverse charge, exempt, standard, zero-rated, free export, outside scope, intra-community, two Spanish regional codes, transferred); the help text calls it the VAT category code for electronic invoicing. | N-U32-045 |
| VDR-U32-C085 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:23 | ubl_cii_tax_exemption_reason_code = fields.Selection( | FACT | always | — | A tax carries an optional exemption reason code chosen from a fixed list of VATEX codes that contains European Union and French entries only (lines 23-119); no Thai reason code exists in the list (inferred from reading the list). | N-U32-045 |
| VDR-U32-C086 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:125 | ['AE', 'E', 'G', 'O', 'K'] | FACT | always | — | The reason code is required (computed flag) when the category is AE, E, G, O or K; an onchange, not a constraint, clears the reason when it is not required (lines 120-131). | N-U32-045 |
| VDR-U32-C087 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/views/account_tax_views.xml:10 | ubl_cii_tax_exemption_reason_code | FACT | always | — | The two fields are added after the country field on the tax form and the reason code is hidden unless the category requires it. | N-U32-045 |
| VDR-U32-C088 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:1 | price_include_override | OBSERVATION | restored dump | — | The Thai tax template header has no e-invoicing category or reason column; restored DB: all 18 Thai taxes have an empty category code and an empty reason code (configuration query). | N-U32-056 |
| VDR-U32-C089 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:420 | if tax.ubl_cii_tax_category_code: | FACT | always | — | The category code is predicted by a function that returns the tax own code when set (lines 405-421). | N-U32-046 |
| VDR-U32-C090 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:432 | if not tax or tax.amount == | FACT | always | — | When supplier and customer are in the same country and no code is set, a tax with amount 0 maps to E (exempt). | N-U32-046 |
| VDR-U32-C091 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:435 | elif tax.has_negative_factor: | FACT | always | — | In the same-country case a tax with a negative repartition factor (buyer-side reverse charge) maps to AE; any other non-zero tax maps to S (lines 435-445). | N-U32-046 |
| VDR-U32-C092 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:450 | if (supplier_in_eea or customer_in_eea) and supplier.vat: | FACT | always | — | The export or intra-community codes G and K are produced only when the supplier or the customer is in the European Economic Area and the supplier has a tax id (lines 447-458). | N-U32-046 |
| VDR-U32-C093 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:460 | if tax.amount != 0: | FACT | always | — | In every other cross-border case a non-zero tax maps to S and a zero tax maps to E (lines 460-463). | N-U32-046 |
| VDR-U32-C094 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:14 | tax_output_vat_0 | INFERENCE | always | RT | Thai zero-rated output VAT (id tax_output_vat_0, line 14) and Thai exempt output VAT (tax_output_vat_exempted, line 22) are both percent taxes of amount 0 with no e-invoicing code; with the default logic both map to E for a domestic or non-EEA customer, so zero-rated and exempt supply cannot be told apart in an exported document unless a code is set on each tax (execution not run). | N-U32-056 |
| VDR-U32-C095 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:479 | if tax and (code := tax.ubl_cii_tax_exemption_reason_code): | FACT | always | — | The exemption reason is taken from the tax code first, with a text from the mapping table; otherwise the default text is "Exempt from tax" for E, with VATEX-EU-G for G and VATEX-EU-IC for K (lines 465-500). | N-U32-047 |
| VDR-U32-C096 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:492 | tax_exemption_reason_code = 'VATEX-EU-G' | FACT | always | — | The default reason codes generated by the base logic are European Union codes only; no Thai statutory reference is produced by the base module. | N-U32-047 |
| VDR-U32-C097 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:111 | or self._ubl_is_excise_tax(tax_data) | FACT | always | — | The tax-category grouping key is empty for non-percent taxes and for recycling-contribution and excise taxes, so those taxes never appear in the tax category totals (lines 97-113). | N-U32-049 |
| VDR-U32-C098 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:117 | scheme_id = 'GST' | FACT | always | — | The tax scheme is GST when the supplier country is in the GST country set and VAT otherwise (lines 115-119); that set (account_edi_common.py lines 228-231) does not contain Thailand. | N-U32-050 |
| VDR-U32-C099 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:151 | 'is_withholding': tax.amount < 0.0, | FACT | always | — | A percent tax with a negative amount is flagged is_withholding in the grouping key, and its percent is the tax amount itself unless the tax has a negative factor (lines 133-153). | N-U32-048 |
| VDR-U32-C100 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:145 | percent = tax.amount if not tax.has_negative_factor | INFERENCE | always | RT | Thai withholding taxes are percent taxes with negative rates and positive repartition (U23-C058), so they are flagged withholding and would export a negative percent; whether a Thai-oriented format accepts that was not run. | N-U32-048 |
| VDR-U32-C101 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:263 | if not tax_grouping_key or tax_grouping_key['is_withholding']: | FACT | always | — | Withholding taxes are left out of the item-level classified tax category (lines 253-265). | N-U32-048 |
| VDR-U32-C102 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2221 | target_key = 'cac:WithholdingTaxTotal' | FACT | always | — | In the tax total builder, withholding taxes go to a separate withholding-tax total node with the sign reversed, other taxes to the normal tax total node, each in invoice currency and in company currency when different (lines 2178-2301). | N-U32-048 |
| VDR-U32-C103 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2349 | -tax_total_node['cbc:TaxAmount']['_text'] | FACT | always | — | The tax-inclusive monetary total equals the tax-exclusive total plus the tax totals minus the withholding totals (lines 2339-2360); the tax-exclusive total is line extension plus charges minus allowances (lines 2317-2336). | N-U32-048 |
| VDR-U32-C104 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2446 | payable_rounding_amount = expected_tax_inclusive_amount - tax_inclusive_amount | FACT | always | — | A payable rounding amount equals the engine total (excluded plus tax per base line) minus the exported tax-inclusive amount and is omitted when zero at currency precision; this is the amount-consistency reconciliation of the export (lines 2429-2456). | N-U32-052 |
| VDR-U32-C105 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2421 | amount_total - amount_residual, | FACT | always | — | The exported payable amount is the residual of the document and the prepaid amount is total minus residual, in invoice currency or in company-currency signed amounts (lines 2406-2423); a document already partly paid exports the residual as payable. | N-U32-052 |
| VDR-U32-C106 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2723 | self._validate_taxes(invoice.invoice_line_ids.tax_ids) | FACT | always | — | The generic export first validates the taxes of the invoice lines (lines 2719-2724); the validation calls the tax repartition check and raises a ValidationError naming the tax (account_edi_common.py lines 396-403). | N-U32-058 |
| VDR-U32-C107 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:400 | tax._validate_repartition_lines() | FACT | always | — | Tax structure validation is delegated to the tax repartition validator; an invalid tax aborts the export with a message. | N-U32-058 |
| VDR-U32-C108 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2730 | errors = [constraint for constraint in | FACT | always | — | Format constraints are collected from the document node constraint hook and returned as a set of messages; the base hook returns an empty dictionary, so tax-total validation beyond the shared checks is delegated to format classes (lines 2580-2594, 2729-2740). | N-U32-061 |
| VDR-U32-C109 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:550 | Each invoice line should have at | FACT | always | — | A shared constraint requires at least one tax on every non-section, non-note invoice line; the check is skipped for combo products by the line hook (account_move_line.py lines 3536-3537). | N-U32-051 |
| VDR-U32-C110 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:713 | document_node['cac:WithholdingTaxTotal'] = None | FACT | always | RT | The older UBL 2.0 builder leaves the withholding total empty and builds its own tax total nodes (lines 712-728), while the BIS 3 class calls the newer generic tax total builder (account_edi_xml_ubl_bis3.py line 128); the base file carries 30 deprecation markers, so which generation runs for a given format was not traced. | N-U32-060 |
| VDR-U32-C111 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:178 | 'ubl_sg': {'countries': ['SG'] | FACT | always | — | Export formats are bound to countries: BIS 3 to the default Peppol country list, XRechnung and ZUGFeRD to DE, A-NZ to NZ and AU, NLCIUS to NL, SG to SG, Factur-X to FR (lines 167-181); no format lists Thailand. | N-U32-055 |
| VDR-U32-C112 | FUNCTION MAPPING REQUIRED | account/models/company.py:34 | PEPPOL_DEFAULT_COUNTRIES = [ | FACT | always | — | The default Peppol country list holds 21 European countries and does not contain Thailand. | N-U32-055 |
| VDR-U32-C113 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:199 | if country_code in format_mapping: | FACT | always | — | A format is suggested only when the partner country has one; otherwise the suggestion is false, so a Thai-country partner gets no suggested format (lines 195-209). | N-U32-055 |
| VDR-U32-C114 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:33 | EU Standard (Peppol Bis 3.0) | INFERENCE | always | RT | The partner format selection lists all formats and is not filtered by country, so a Thai partner can be given a European format manually; the resulting document with Thai taxes was not run. | N-U32-055 |
| VDR-U32-C115 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:367 | and ubl_cii_format in self.env['res.partner']._get_ubl_cii_formats() | FACT | always | — | The XML is generated only for sale documents, or for posted purchase documents of a self-billing journal, and only when the format is one of the UBL or CII formats (lines 363-367). | N-U32-053 |
| VDR-U32-C116 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:143 | invoice_data['error_but_continue'] = True | FACT | always | — | When the export returns errors the send flow records the errors and continues without the XML attachment (lines 124-152). | N-U32-053 |
| VDR-U32-C117 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:240 | for edi_format in move.journal_id.edi_format_ids: | OBSERVATION | restored dump | — | Restored DB: the legacy EDI format table has 0 rows, so the post-time loop over journal EDI formats does nothing; the legacy framework still provides the posting, reset and cancel hooks (TXA2 relied on) and 4 ACL rows and 1 cron. | N-U32-054 |
| VDR-U32-C118 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:216 | return self._prepare_invoice_aggregated_taxes( | FACT | always | — | The legacy EDI tax-detail helper delegates to the core aggregated-tax routine and returns base and tax amounts per grouping key and per line in company and foreign currency (lines 155-220). | N-U32-054 |
| VDR-U32-C119 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1471 | fiscal_position = self.env['account.move'].new({ | FACT | always | — | On import the fiscal position is evaluated on a new move built with the company, the move type and the retrieved customer, and passed to the tax search (lines 1470-1477). | N-U32-057 |
| VDR-U32-C120 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5150 | if 'payment_state_before_switch' not in self.env['account.move']._fields: | FACT | always | — | The predictive step of the import tax search is skipped unless the accounting enterprise module is installed, so Community has three effective steps: account default tax, price-include or exclude with fiscal position, and fixed charge match (lines 5136-5244). | N-U32-057 |
| VDR-U32-C121 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5253 | Domain('amount_type', '=', tax_values['amount_type']) & | FACT | always | — | An imported tax is matched on amount type, tax use and amount, optionally on name, exigibility, tax country and the e-invoicing category code, ordered by sequence (lines 5247-5268). | N-U32-057 |
| VDR-U32-C122 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:764 | Could not retrieve the tax: | FACT | always | — | A tax that cannot be matched is written to the import log in the chatter and the line is left without tax; the import does not stop (lines 1485-1524). | N-U32-057 |
| VDR-U32-C123 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1725 | tolerance = 0.03 | FACT | always | — | After import the tax-fix step rewrites tax-line amounts to the document tax totals when every tax was matched and the difference to the computed tax is within 0.03 (lines 1721-1799). | N-U32-059 |
| VDR-U32-C124 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1774 | _distribute_delta_amount_smoothly( | FACT | always | — | The difference between the file tax total and the computed tax is spread over the tax data proportionally to raw tax amounts and written back to the tax lines through the dynamic-line synchronisation. | N-U32-059 |
| VDR-U32-C125 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:13 | _inherit = ['account.edi.xml.ubl_21', 'account.edi.ubl_pint_eu'] | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: format-specific builders (BIS 3, PINT, CII Factur-X, XRechnung, NLCIUS, A-NZ, SG, E-FFF) were read only down to class headers and the call lines cited above; they are country-pack material, not studied. Resolve by a future optional country pack study and a runtime export of a Thai document. | N-U32-061 |
| VDR-U32-C126 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:39 | 'auto_install': True, | OBSERVATION | restored dump | — | The UBL and CII module depends on account only and is auto-installed; restored DB: installed, with the Peppol module not installed (only its advanced-fields companion and the proxy client installed) and 0 EDI documents. | N-U32-054 |
| VDR-U32-C127 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: the exported document for a Thai invoice with 7 percent, zero-rated, exempt and withholding taxes, the amount checks of each format class and any Thai-specific file format (ETDA XML or RD reporting) are not established; foreign formats are future optional country-pack material and were not studied. | N-U32-061 |
| VDR-U32-C128 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order.py:211 | taxes = carrier.product_id.taxes_id._filter_taxes_by_company(self.company_id) | FACT | always | — | A delivery line takes the carrier product customer taxes of the order company (line 211), mapped by the order fiscal position only when the order has a partner and a position (lines 213-214). | N-U32-062 |
| VDR-U32-C129 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order.py:230 | 'tax_ids': [(6, 0, taxes_ids)], | FACT | always | — | The delivery line values set tax_ids explicitly together with price_unit, quantity 1 and the delivery flag (lines 223-232), so the standard line tax computation is not used for the delivery line. | N-U32-062 |
| VDR-U32-C130 | FUNCTION MAPPING REQUIRED | delivery/models/delivery_carrier.py:325 | res['price'] = self.product_id._get_tax_included_unit_price( | FACT | always | — | A provider rate in company currency is converted by the shared tax-included unit price helper with the order fiscal position at the order date, then margins are applied, before it becomes the line price (lines 306-337; TXA1-C153 relied on). | N-U32-062 |
| VDR-U32-C131 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order.py:34 | delivery_cost = sum([l.price_total for l in | FACT | always | — | The amount used for free-over-threshold shipping is the order total minus the tax-included price of delivery lines, so the threshold is compared on a tax-inclusive amount (lines 32-35). | N-U32-068 |
| VDR-U32-C132 | FUNCTION MAPPING REQUIRED | sale_loyalty_delivery/models/sale_order.py:34 | taxes = delivery_line.product_id.taxes_id._filter_taxes_by_company(self.company_id) | FACT | always | — | A free-shipping reward line copies the delivery line product taxes mapped by the order fiscal position and sets a negative price equal to the delivery line price, capped by the reward maximum (lines 32-49). | N-U32-063 |
| VDR-U32-C133 | FUNCTION MAPPING REQUIRED | sale_loyalty_delivery/models/sale_order.py:16 | l.coupon_id.program_type in ['ewallet', 'gift_card'] | FACT | always | — | The amount without delivery also subtracts the price of gift card and eWallet lines, so those payment-type lines do not count towards the free-shipping threshold (lines 12-18). | N-U32-068 |
| VDR-U32-C134 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order.py:231 | 'is_delivery': True, | OBSERVATION | restored dump | — | Restored DB: the standard delivery product and the other delivery-type service products carry the 7% customer tax and the 7% vendor tax; delivery seeds 10 ACL rows and 1 record rule. | N-U32-071 |
| VDR-U32-C135 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:272 | 'discount': 100, | FACT | always | — | A free-product reward is an order line of the reward product with discount 100, the product taxes mapped by the order fiscal position and a cleared-then-linked tax set (lines 259-280); the taxable base of the free line is therefore zero. | N-U32-063 |
| VDR-U32-C136 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:638 | for tax, price in discountable_per_tax.items(): | FACT | always | — | A discount reward creates one negative line per distinct set of non-fixed taxes of the discounted lines, each with that tax set mapped by the fiscal position and a price equal to the share of the discount for that set (lines 636-658; TXA1-C306 relied on). | N-U32-063 |
| VDR-U32-C137 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:636 | discount_factor = min(1, (max_discount / discountable)) | FACT | always | — | The discount is capped at the order total (line 581), converted to a factor of the tax-inclusive discountable amount, and applied to each tax-set price, so the split lines add up to the capped discount. | N-U32-064 |
| VDR-U32-C138 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:393 | if tax_data['tax'].price_include | FACT | always | — | The discountable amount per tax set adds the raw tax amount of price-included taxes to the raw base, while non-included taxes stay outside the line price and are recomputed on the discount line (lines 387-395). | N-U32-066 |
| VDR-U32-C139 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:358 | This does not apply to Gift | FACT | always | — | Fixed taxes are removed from the discountable taxes except for payment programs (gift card, eWallet), where the whole order total may be paid with the balance (lines 351-363). | N-U32-065 |
| VDR-U32-C140 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:611 | # For gift cards, the SOL | FACT | always | — | A gift-card redemption line takes the taxes of the reward discount product mapped by the fiscal position, computes the tax with forced price-included mode and sets the price to the untaxed value plus price-included tax amounts (lines 603-634). | N-U32-067 |
| VDR-U32-C141 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_reward.py:13 | 'taxes_id': False, | FACT | always | — | Discount products created for rewards while the order-loyalty module is installed get no customer and no vendor taxes and invoice policy order (lines 9-17; U05-C019 relied on). | N-U32-067 |
| VDR-U32-C142 | FUNCTION MAPPING REQUIRED | sale_loyalty/data/sale_loyalty_data.xml:4 | loyalty.gift_card_product_50 | FACT | always | — | The order-loyalty data file clears the customer taxes of the gift-card and top-up trigger products, so selling a gift card carries no tax by default. | N-U32-067 |
| VDR-U32-C143 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:46 | line.tax_ids = fpos.map_tax(taxes) | INFERENCE | always | RT | For reward lines the tax computation maps the already-set line taxes through the fiscal position again (lines 35-46) although the reward values were mapped when built (d09, d13); whether a second mapping changes anything depends on the position mapping and was not run. | N-U32-074 |
| VDR-U32-C144 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_rule.py:68 | minimum_amount_tax_mode = fields.Selection( | FACT | always | — | A loyalty rule has a minimum purchase amount with a tax mode, tax included (default) or tax excluded. | N-U32-068 |
| VDR-U32-C145 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1301 | rule.minimum_amount_tax_mode == 'incl' | FACT | always | — | The rule threshold is compared with the sum of line subtotals plus line taxes (included mode) or with the sum of subtotals (excluded mode) (lines 1299-1303). | N-U32-068 |
| VDR-U32-C146 | FUNCTION MAPPING REQUIRED | loyalty/data/loyalty_data.xml:38 | gift_card_program_reward | OBSERVATION | restored dump | CONTRA | Restored DB: one gift-card program (trigger automatic, applies to future orders) with one discount reward (per point, applies on order); the reward discount product (a service, not sold) carries the 7% customer tax, which is inferred to come from its creation by the base loyalty data before the order-loyalty module was installed (install order and creation timestamps), while the gift-card trigger product has no customer tax (loyalty seeds 8 ACL rows and 5 rules, sale_loyalty 17 ACL rows). Narrows U05-C019, which describes reward discount products as created without taxes. | N-U32-071 |
| VDR-U32-C147 | FUNCTION MAPPING REQUIRED | sale_product_matrix/models/sale_order.py:107 | default_so_line_vals = OrderLine.default_get(OrderLine._fields.keys()) | FACT | always | — | The sale matrix adds new cells as order lines built from field defaults with product, quantity and variant attributes only (lines 44-120); taxes and price come from the normal line computation of the product and fiscal position. | N-U32-070 |
| VDR-U32-C148 | FUNCTION MAPPING REQUIRED | purchase_product_matrix/models/purchase.py:106 | product_qty=qty, | FACT | always | — | The purchase matrix likewise creates lines from product and quantity only; taxes are then derived through the purchase line onchange and missing-field routines (U06-C177 relied on). | N-U32-070 |
| VDR-U32-C149 | FUNCTION MAPPING REQUIRED | sale_margin/models/sale_order_line.py:47 | line.margin = line.price_subtotal - (line.purchase_price * | FACT | always | — | Line margin is the untaxed subtotal minus cost times ordered quantity; with the delivered policy the subtotal is price_unit times delivered quantity, which ignores line discount and tax (lines 38-48). | N-U32-069 |
| VDR-U32-C150 | FUNCTION MAPPING REQUIRED | sale_margin/models/sale_order.py:19 | order.margin_percent = order.amount_untaxed and order.margin/order.amount_untaxed | FACT | always | — | Order margin percent divides by the untaxed order total (lines 14-34). | N-U32-069 |
| VDR-U32-C151 | FUNCTION MAPPING REQUIRED | product_matrix/__manifest__.py:11 | 'depends' | INFERENCE | always | — | Search record: the python, xml and js files of product_matrix, sale_product_matrix, purchase_product_matrix, sale_mrp_margin contain no tax or fiscal reference; sale_margin and sale_expense_margin refer to untaxed amounts only. NO TAX HANDLING FOUND in the matrix modules. | N-U32-073 |
| VDR-U32-C152 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:738 | def _create_downpayments(self, line_vals): | FACT | always | — | The purchase order can hold down-payment section and lines created from vendor-bill lines (lines 724-758). | N-U32-072 |
| VDR-U32-C153 | FUNCTION MAPPING REQUIRED | purchase/wizard/bill_to_po_wizard.py:61 | 'tax_ids': aml.tax_ids, | FACT | always | — | The bill-to-purchase-order wizard creates a down-payment line per selected bill line with quantity 0, the bill line price converted at the purchase order date, and the taxes copied from the bill line without fiscal-position mapping (lines 43-70). | N-U32-072 |
| VDR-U32-C154 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:543 | 'price_unit': line.price_unit, | FACT | always | RT | Converting bill lines into purchase order lines passes product, quantity, unit, price_unit and discount but no taxes (lines 537-547), so the order line taxes come from the product vendor taxes and the order fiscal position; a price-included bill line price may then meet different taxes (execution not run). | N-U32-072 |
| VDR-U32-C155 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: numeric tax effect of gift-card redemption, stacked rewards, free-product lines and free shipping with withholding taxes was not executed; resolve with an AWT run. | N-U32-075 |
| VDR-U32-C156 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3159 | return self.amount_type not in ('fixed', 'code') | FACT | always | — | A tax can be discounted unless its type is fixed or code; percent taxes, including the negative-rate Thai withholding taxes, are discountable and therefore take part in discounts, down payments and early-payment splits (lines 3150-3159). | N-U32-078 |
| VDR-U32-C157 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4015 | return not tax_data['tax']._can_be_discounted() or (exclude_function and | FACT | always | — | The down-payment preparation wraps the non-discountable taxes into the base amount before reduction (lines 3999-4017; U05-C107 relied on). | N-U32-078 |
| VDR-U32-C158 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:149 | base_lines = [line._prepare_base_line_for_taxes_computation() for line in | FACT | always | — | The advance is computed from every non-display order line at ordered quantity through the tax engine, rounded, before the down-payment lines are prepared (lines 147-166; U05-C104 relied on). | N-U32-076 |
| VDR-U32-C159 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3742 | expected_total_amount_currency = currency.round(total_amount_currency * sign * | FACT | always | — | For a percentage advance the target is that percentage of the tax-inclusive order total (excluded plus tax per base line) (lines 3700-3743). | N-U32-076 |
| VDR-U32-C160 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3737 | percentage = (signed_amount / total_amount_currency) if | FACT | always | — | For a fixed advance the amount is read as a tax-inclusive amount and converted to a percentage of the tax-inclusive order total. | N-U32-076 |
| VDR-U32-C161 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3748 | 'tax_amount_currency': currency.round(values['tax_amount_currency'] * sign * percentage), | FACT | always | — | The expected tax is computed per tax from the order tax amounts and the percentage, rounded in invoice currency and company currency independently; the expected base is the target total minus the expected taxes (lines 3746-3762), so with several taxes each tax reaches its own rounded share. | N-U32-079 |
| VDR-U32-C162 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3785 | # Smooth distribution of the delta | FACT | always | — | After lines are reduced and rounded, the remaining delta per tax and per base is spread smoothly over the lines carrying that tax (lines 3785-3860), separately in currency and company currency. | N-U32-079 |
| VDR-U32-C163 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4053 | self._fix_base_lines_tax_details_on_manual_tax_amounts( | FACT | always | — | The prepared lines are fixed on manual tax amounts so that stored tax amounts reproduce the computed amounts when the lines are later turned into order lines and invoice lines (lines 4053-4056; TXA1-C043 relied on). | N-U32-079 |
| VDR-U32-C164 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1606 | ._reverse_quantity_base_line_extra_tax_data(line.extra_tax_data) | FACT | always | — | The final invoice emits each down-payment line with quantity -1 and reversed stored tax data, so the advance tax is reversed at the amounts originally computed (lines 1599-1606; U05-C059 relied on). | N-U32-077 |
| VDR-U32-C165 | FUNCTION MAPPING REQUIRED | sale/models/res_company.py:50 | downpayment_account_id = fields.Many2one( | OBSERVATION | restored dump | — | Restored DB: the company down-payment account is not set; down-payment lines then take the product down-payment account or the income account, mapped by the fiscal position (U05-C113, U05-C114 relied on). | N-U32-080 |
| VDR-U32-C166 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: combined behaviour of an advance with a global discount, early-payment discount or withholding taxes in one order was not executed; resolve with an AWT run. | N-U32-081 |
| VDR-U32-C167 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1086 | and l.move_id.invoice_payment_term_id.early_pay_discount_computation == 'mixed' | FACT | payment term mode mixed | — | Invoice-time early-payment-discount lines exist only for taxed product lines of an invoice whose payment term has an early discount in mixed mode (lines 1076-1087); the dump has all payment terms in included mode (TXA1-C280), so no such lines arise there. | N-U32-082 |
| VDR-U32-C168 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1097 | return not tax_data['tax']._can_be_discounted() | FACT | always | — | Fixed (and formula) taxes are dispatched out of the early-payment base before grouping (lines 1096-1125). | N-U32-084 |
| VDR-U32-C169 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1093 | 'tax_ids': [Command.set([tax_data['tax'].id for tax_data in base_line['tax_details']['taxes_data']])], | FACT | always | — | The grouping key for the discount amount is account, analytic distribution and the full set of taxes of the base line, so lines with several taxes form one group per tax set and each group gets its own discount line carrying that tax set (lines 1089-1094). | N-U32-083 |
| VDR-U32-C170 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1135 | epd_amount_currency = currency.round(sign * values['total_excluded_currency'] * | FACT | always | — | The discount of a group is the discount percentage of its untaxed total, rounded in document currency and, separately, in company currency (lines 1134-1136). | N-U32-083 |
| VDR-U32-C171 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1166 | 'tax_ids': [Command.clear()], | FACT | always | — | The discount is booked as a pair: a line with the group tax set and tags and a counterpart without taxes on the same account (lines 1139-1168), so the tax engine sees a reduced base per tax set while the counterpart is untaxed. | N-U32-083 |
| VDR-U32-C172 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1170 | target_factors = [ | FACT | always | — | The group discount is spread over its invoice lines in proportion to their raw untaxed amounts with the smooth-distribution helper, once in currency and once in company currency (lines 1170-1197). | N-U32-083 |
| VDR-U32-C173 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1635 | special_type='early_payment', | FACT | always | — | Early-payment lines enter the engine as base lines of special type early payment in total-excluded mode (lines 1619-1639; TXA1-C107 relied on); for unsaved invoices they are anticipated from the needed values (lines 1641-1671). | N-U32-083 |
| VDR-U32-C174 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:548 | line_amount_after_discount = (line.price_subtotal / 100) * | FACT | always | — | A sale order in mixed mode adds, for each priced line, a negative early-payment line carrying the flattened non-fixed taxes of that line and a positive untaxed counterpart, both computed from the line subtotal times the percentage without rounding (lines 531-568). | N-U32-087 |
| VDR-U32-C175 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:557 | tax_ids=line.tax_ids.flatten_taxes_hierarchy().filtered(lambda tax: tax.amount_type != 'fixed'), | INFERENCE | always | RT | The order excludes only fixed taxes while the invoice excludes every non-discountable tax (fixed and formula) and groups by tax set; for several lines and taxes the order tax total and the invoice tax total can differ by rounding; the numeric comparison was not run. | N-U32-088 |
| VDR-U32-C176 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | always | — | UNKNOWN - EVIDENCE INSUFFICIENT: no early-payment line builder was found for purchase orders (grep for epd and early_pay in purchase models returned nothing); whether purchase order totals include a supplier early discount before billing is not established; U06-C181 states order totals come from the tax totals summary over lines only. | N-U32-089 |
| VDR-U32-C177 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5096 | tax_lines_needed = early_pay_discount_computation == 'included' and | FACT | always | — | In included mode the discount is applied at payment time: taxed invoice lines trigger tax adjustment lines, untaxed invoices only base lines (lines 5068-5096). | N-U32-082 |
| VDR-U32-C178 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5122 | base_line['tax_ids'] = base_line['tax_ids'].filtered(lambda t: t.amount_type != | FACT | always | — | For the payment-time recomputation fixed taxes are removed and every unit price is multiplied by the remaining share (100 minus discount percentage) before the engine recomputes each tax (lines 5121-5128). | N-U32-084 |
| VDR-U32-C179 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5187 | resulting_delta_tax_details[tax_line_vals['tax_repartition_line_id']] = { | FACT | always | — | The tax adjustment is the recomputed tax minus the tax on the invoice, kept per repartition line, so several taxes are each adjusted on their own repartition line; the adjustment uses the repartition line of the opposite document type so tags and accounts are reversed (lines 5082-5087, 5183-5192). | N-U32-085 |
| VDR-U32-C180 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5180 | percentage_paid = abs(payment_term_line.amount_residual_currency / self.amount_total) | FACT | always | — | Base and tax adjustments are scaled by the share of the payment-term line still open, so partial payments and instalments adjust tax proportionally (lines 5180-5221). | N-U32-085 |
| VDR-U32-C181 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5231 | biggest_base_line = max(list(res['base_lines'][payment_term_line].values()), key=lambda x: x['amount_currency']) | FACT | always | — | Any rounding remainder against the discount on the payment-term line is added to the biggest base adjustment line, never to a tax line (lines 5223-5233). | N-U32-085 |
| VDR-U32-C182 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5131 | cash_discount_account = company.account_journal_early_pay_discount_loss_account_id | FACT | always | — | The base adjustment lines are posted on the company early-payment loss account for inbound documents and on the gain account for outbound documents (lines 5130-5133); restored DB: both accounts are set. | N-U32-086 |
| VDR-U32-C183 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5287 | exchange_line_account = aml.company_id.expense_currency_exchange_account_id | FACT | always | — | Any exchange difference left after the discount lines is booked on the exchange expense or income account (lines 5283-5302). | N-U32-086 |
| VDR-U32-C184 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: numeric equality of order, invoice and payment-time tax adjustments for several taxes and lines, instalments and foreign currency was not executed; resolve with an AWT run in mixed and included modes. | N-U32-089 |
| VDR-U32-C185 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:424 | cache[key] = self.env['account.fiscal.position'].with_company( | FACT | always | — | On a sale order the fiscal position is a stored compute of company, partner and shipping partner; a change on an order with lines raises the update-taxes prompt (lines 411-429; TXA1-C213 relied on). | N-U32-090 |
| VDR-U32-C186 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1358 | lines_to_recompute._compute_tax_ids() | FACT | always | — | Order line taxes are recomputed from product and position only when the user runs the update-taxes action, which also clears the prompt (lines 1346-1359). | N-U32-091 |
| VDR-U32-C187 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:562 | fiscal_position = line.order_id.fiscal_position_id | FACT | always | — | Sale line taxes are mapped by the order fiscal position without re-evaluating the finder (lines 544-571; TXA1-C218 relied on). | N-U32-091 |
| VDR-U32-C188 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1439 | self.fiscal_position_id._get_fiscal_position(self.partner_invoice_id) | FACT | always | — | The invoice created from an order receives the order position, else the position found for the invoice partner (line 1439; TXA1-C224 relied on). | N-U32-092 |
| VDR-U32-C189 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:453 | self.fiscal_position_id = self.env['account.fiscal.position']._get_fiscal_position(self.partner_id) | FACT | always | — | On a purchase order the position is set by the partner onchange (lines 445-456), not by a stored compute; orders created by code must receive it explicitly. | N-U32-090 |
| VDR-U32-C190 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:156 | fpos = line.order_id.fiscal_position_id or line.order_id.fiscal_position_id._get_fiscal_position(line.order_id.partner_id) | FACT | always | — | Purchase line taxes are the product vendor taxes of the line company mapped by the order position or, if none, by the position found for the order partner (lines 153-159; U06-C182 relied on). | N-U32-093 |
| VDR-U32-C191 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:409 | self._compute_tax_id() | INFERENCE | always | — | The purchase line tax routine is called from the product onchange (lines 381-409), from the order onchange on position or company (purchase_order.py lines 468-473) and from the alternative-order wizard (purchase_requisition_create_alternative.py line 45); it is not a stored compute, so a programmatic line without taxes keeps none unless the creator sets them (U06-C177 relied on). | N-U32-093 |
| VDR-U32-C192 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:938 | 'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id._get_fiscal_position(self.partner_id)).id, | FACT | always | — | A vendor bill created from an order receives the order position or the one found for the order partner (line 938). | N-U32-092 |
| VDR-U32-C193 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:342 | fpos = self.env['account.fiscal.position'].with_company(company_id)._get_fiscal_position(partner) | FACT | always | — | A purchase order created by replenishment gets the position found for the supplier partner, and its lines map the product vendor taxes by that position with price-included price correction (purchase_order_line.py lines 679-686). | N-U32-094 |
| VDR-U32-C194 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:50 | fpos = FiscalPosition.with_company(self.company_id)._get_fiscal_position(partner) | FACT | always | — | A purchase order built from a requisition evaluates the position for the partner and maps the vendor taxes of the requisition company hierarchy (lines 36-93; U06-C253 relied on). | N-U32-094 |
| VDR-U32-C195 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1040 | 'in_receipt': move.company_id.account_purchase_receipt_fiscal_position_id, | FACT | always | — | For purchase receipts the position is the company default receipt position and not the position found for the partner; for other types the finder is called with the partner and the delivery partner (lines 1036-1050; TXA1-C103 relied on). | N-U32-090 |
| VDR-U32-C196 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1735 | 'tax_ids': [Command.set(self.tax_ids.ids)], | INFERENCE | always | — | Expense line taxes are the expense taxes with no position mapping, hr_expense has no fiscal-position reference in its python or wizard files, and the receipt created for the employee has its position computed as a purchase receipt (the company receipt position, empty in the dump), so no partner-driven mapping applies to expenses. | N-U32-090 |
| VDR-U32-C197 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:991 | tax_ids = self.move_id.fiscal_position_id.map_tax(tax_ids) | FACT | always | — | Default line taxes (product, then account) are narrowed to the company and mapped by the move position (lines 964-993; TXA1-C138 relied on). | N-U32-095 |
| VDR-U32-C198 | FUNCTION MAPPING REQUIRED | account/models/partner.py:263 | if not delivery or (intra_eu and | INFERENCE | always | RT | The finder reads the first two characters of the company and partner tax ids as country codes and applies EU rules (lines 255-264); a Thai tax id is numeric, so the EU branch is not taken for a Thai company (inferred; not run). | N-U32-097 |
| VDR-U32-C199 | FUNCTION MAPPING REQUIRED | account/models/partner.py:277 | all_auto_apply_fpos = self.search( | OBSERVATION | restored dump | — | Restored DB: 0 fiscal positions and no default receipt position, so every hand-off in the dump evaluates to an empty position and taxes stay the product defaults; foreign customers and vendors therefore need a manual tax choice (U25-C204, U25-C211 relied on). | N-U32-098 |
| VDR-U32-C200 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:971 | vat_required_valid = vat_required_valid and self.vies_valid | FACT | base_vat installed | — | When the optional VAT-validation module is installed, a position that requires a tax id also needs the online-verified flag, but only if the company is in the EU group or the partner country has a foreign fiscal position (lines 962-972; U23-C129 relied on); with no position in the dump it has no effect on Thai flows. | N-U32-099 |
| VDR-U32-C201 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5183 | Domain('fiscal_position_ids', '=', fiscal_position.id) | FACT | always | — | A tax can be restricted to fiscal positions; the import search keeps taxes of the position, and for a domestic position also taxes without position (lines 5177-5197). | N-U32-096 |
| VDR-U32-C202 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of foreign customers and foreign vendors with a configured fiscal position (mapping of Thai output VAT to zero rate, reverse-charge style mapping) cannot be shown because the dump has no fiscal position; resolve by loading a representative position and running orders, bills and expenses. | N-U32-101 |
| VDR-U32-C203 | FUNCTION MAPPING REQUIRED | account_tax_python/models/account_tax.py:119 | return self._eval_tax_amount_formula(raw_base, evaluation_context) | FACT | always | — | A formula tax is evaluated through the override of the fixed-amount evaluation hook (lines 116-120; U23-C157 relied on). | N-U32-102 |
| VDR-U32-C204 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1257 | eval_tax_amount(tax._eval_tax_amount_fixed_amount, tax) | FACT | always | — | The engine evaluates the fixed-amount hook for every tax first, in reverse sorted order, before the price-included and price-excluded passes (lines 1248-1267); a formula tax is therefore evaluated in the fixed pass. | N-U32-103 |
| VDR-U32-C205 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1195 | raw_base + taxes_data[tax.id]['extra_base_for_tax'], | FACT | always | — | The base handed to the evaluation functions is the raw base plus the extra base propagated from previously computed taxes (lines 1188-1199), and this is the base value visible to a formula. | N-U32-103 |
| VDR-U32-C206 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1097 | def _eval_tax_amount_price_included(self, batch, raw_base, evaluation_context): | INFERENCE | always | — | The price-included and price-excluded passes return amounts only for percent and division types (lines 1097-1135), so a formula tax gets its amount only from the fixed pass; the engine batches taxes of the same amount type, so formula taxes batch only with each other (line 955). | N-U32-103 |
| VDR-U32-C207 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1287 | base -= total_tax_amount | INFERENCE | account_tax_python installed | RT | If a formula tax carried the price-included flag the engine would subtract its amount from the base (lines 1286-1287); the module has no constraint on that flag for formula taxes (U23-C139..C165 read), so the combination is allowed by structure and its numeric effect was not run. | N-U32-109 |
| VDR-U32-C208 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:59 | return tax.amount_type == 'code' and tax.include_base_amount | FACT | always | — | The UBL helper treats a formula tax that includes its amount in the base as an excise tax and exports it as an allowance or charge, not in the tax totals (lines 49-59, 1288-1340); this is the only cross-module hook to the formula-tax add-on in the e-invoicing code. | N-U32-104 |
| VDR-U32-C209 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:940 | if filter_tax_function: | FACT | always | — | The engine can drop taxes through a filter function before batching (lines 939-941); the withholding-on-payment add-on sets that filter on every base line unless the key calculate_withholding_taxes is present (U23-C009 relied on), so document taxes are batched and ordered without the withholding taxes. | N-U32-105 |
| VDR-U32-C210 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:177 | calculate_withholding_taxes=True, | FACT | always | — | The original withheld amount for a base is the negated tax amount returned by the engine for the single withholding tax with the flag set (lines 170-181). | N-U32-105 |
| VDR-U32-C211 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:321 | manual_tax_amounts = {str(self.tax_id.id): { | FACT | always | — | The user-edited base and withheld amount are fed back to the engine as manual tax amounts, converted to company currency with the payment-date rate, so the payment entry reproduces exactly the values on the withholding line (lines 308-343). | N-U32-105 |
| VDR-U32-C212 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:379 | tax_results = AccountTax._prepare_tax_lines(base_lines, company) | FACT | always | — | Withholding tax lines of the payment entry are produced by the generic tax-line builder, so they carry repartition line, account and tags like document tax lines (lines 374-390; U23-C025 relied on). | N-U32-106 |
| VDR-U32-C213 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:413 | 'tax_ids': [], | INFERENCE | always | RT | The base item of a withholding set has empty tax_ids and tags while its counterpart item keeps the grouping key values (lines 408-426); the tax grid base therefore sits on the counterpart item and not on the base item (inferred from the grouping key content; not run). | N-U32-106 |
| VDR-U32-C214 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:125 | JOIN account_tax_repartition_line rep_ln ON rep_ln.id = | FACT | always | — | Tax lines are re-tagged from the tags of the repartition line they already point to, for every line of the company dated from the start date (lines 121-128); tax lines created by other modules, such as payment withholding lines, are included (U23-C185 relied on). | N-U32-107 |
| VDR-U32-C215 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:72 | tax_to_rep_line.repartition_type = 'base' | FACT | always | — | Base lines are re-tagged from the base repartition line of the invoice or refund type of the document, or of the origin document for cash-basis entries, or by balance sign for plain entries (lines 52-115; U23-C177, U23-C179 relied on); amounts are never recomputed. | N-U32-107 |
| VDR-U32-C216 | FUNCTION MAPPING REQUIRED | account_debit_note/wizard/account_debit_note.py:77 | new_move = move.copy(default=default_values) | FACT | always | — | A debit note is a copy of the original with business fields, a new date, no payment term and the original link (lines 54-78; U23-C075, U23-C078 relied on); the copy keeps product-line taxes when lines are copied and, for invoice and bill types, only line creation commands (account_move.py lines 3813-3823). | N-U32-108 |
| VDR-U32-C217 | FUNCTION MAPPING REQUIRED | account_debit_note/wizard/account_debit_note.py:64 | 'invoice_payment_term_id': None, | INFERENCE | always | RT | Clearing the payment term removes any early-payment discount lines from the debit note, and its dates come from the dialog, so currency rate and tax date follow the new document and not the original (inferred from the default dict; not run). | N-U32-108 |
| VDR-U32-C218 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3822 | if command == Command.CREATE | FACT | always | RT | When an invoice or bill is copied only line creation commands are kept, so lines are rebuilt as new lines and the tax lines are re-synchronised from the base lines in draft (lines 3813-3823; execution not run). | N-U32-108 |
| VDR-U32-C219 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: the four uninstalled add-ons were read at source only; installing them, numeric effects of formula and withholding taxes with VAT, and re-tagging on a Thai chart were not executed. | N-U32-110 |
| VDR-U32-C220 | FUNCTION MAPPING REQUIRED | account/wizard/account_automatic_entry_wizard.py:400 | self = self.with_context(skip_computed_taxes=True) | FACT | always | — | The cut-off and reclassification wizard runs with the context that suppresses computed line taxes (line 400; effect at account_move_line.py line 985). | N-U32-111 |
| VDR-U32-C221 | FUNCTION MAPPING REQUIRED | account/wizard/account_automatic_entry_wizard.py:266 | reported_debit = aml.company_id.currency_id.round((self.percentage / 100) * | FACT | always | — | Cut-off lines are the chosen percentage of each source line debit, credit and amount_currency, built with name, account, partner, currency and analytic distribution only (lines 263-315); no tax_ids, tags or repartition are copied, so a cut-off of a taxed base line moves the amount without tax-report effect. | N-U32-111 |
| VDR-U32-C222 | FUNCTION MAPPING REQUIRED | account/wizard/accrued_orders.py:200 | price_subtotal = order_line.tax_ids.compute_all( | FACT | always | — | Accrual amounts use untaxed values: for price-included taxes the untaxed subtotal is taken from compute_all, otherwise quantity times price (lines 185-209); accrual lines carry no tax. | N-U32-112 |
| VDR-U32-C223 | FUNCTION MAPPING REQUIRED | account/wizard/accrued_orders.py:103 | get_product_accounts(fiscal_pos=order.fiscal_position_id) | FACT | always | — | The account of an accrual line is the product income or expense account mapped by the order fiscal position (lines 102-107). | N-U32-112 |
| VDR-U32-C224 | FUNCTION MAPPING REQUIRED | purchase_stock/models/account_invoice.py:84 | 'display_type': 'cogs', | FACT | anglo-saxon accounting on (dump: off) | — | Price-difference lines of a vendor bill are display type cogs lines created with an empty tax set (lines 82-107), so they sit outside the tax lines of the bill. | N-U32-113 |
| VDR-U32-C225 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | UNKNOWN - EVIDENCE INSUFFICIENT: cut-off reclassification of taxed base lines and its effect on the tax report, and accrual of price-included lines, were not executed. | N-U32-114 |
