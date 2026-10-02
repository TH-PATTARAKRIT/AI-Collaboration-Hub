# U32 — Taxes entering entries through other paths — Neutral Knowledge

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room knowledge layer for Thai Tax Core unit U32 (study of Odoo 19 Community behaviour).
> Describes what a ledger system does with taxes on bank lines, employee expenses, landed costs, manufacturing, electronic invoices, discount, loyalty and delivery lines, advances, early-payment discounts, fiscal positions and optional tax add-ons. It states system behaviour only; statutory requirements are validated elsewhere and nothing here is a legal conclusion.
> No V-level, no Complete, no coverage percentage, no Gate PASS.

## CAP-U32-01 Bank statement lines and reconciliation presets that can add taxed lines

### WHAT
- [N-U32-001] A bank statement line becomes a journal entry made of the bank movement and a temporary suspense counterpart. It carries no tax when it is created; any tax must be added later, when the line is classified.
- [N-U32-002] A reconciliation preset is a stored template for the entries a user wants created when a bank line is matched. Each preset line can name an account, a partner, a label, an analytic split and a list of taxes.

### WHY
- [N-U32-003] The bank line is recorded first and classified later, so that a cash movement is never held up by tax classification. The resulting entry is an ordinary journal entry and not a tax document.

### BUSINESS RULE
- [N-U32-004] Nothing in the studied product applies a preset automatically or turns the tax list of a preset into entry lines. The taxes on preset lines are stored configuration only; applying presets to bank lines belongs to a tool outside the studied scope.
- [N-U32-005] A tax named on a preset counts as in use, so it can no longer be deleted and can only be archived.
- [N-U32-006] A write-off typed in the payment registration screen carries no tax. A payment settled with an early-payment discount instead receives its discount, base and tax lines from the invoice, as described under the discount capability.

### STATE
- [N-U32-007] A bank statement entry is posted the moment it is created. Tax lines are synchronised only for entries still in draft, so editing a posted bank entry does not recompute tax.
- [N-U32-008] Undoing the reconciliation of a bank line is attempted only when the fiscal and tax lock checks pass; otherwise the line stays reconciled.

### OPTIONALITY
- [N-U32-009] A preset has no setting saying whether its amounts already include tax.
- [N-U32-010] In the studied database two presets exist, neither names a tax, and there are no statements and no statement lines.

### DEPENDENCY
- [N-U32-011] Cash-basis tax entries are created from every partial match between a document and its settlement, a bank line included. The entry date is the settlement date, moved to the day after the user fiscal lock date when that is later. The studied database holds no cash-basis tax, so none arises there.
- [N-U32-012] The discount-adjustment helper used at payment registration is also documented as serving a bank reconciliation screen that is not part of the studied product.

### CONSTRAINT
- [N-U32-013] Changing the amount, currency, partner or label of a bank line rewrites its entry to the bank item and the suspense item and deletes every other item, so manually added tax or base lines are lost. The entry must always keep exactly one bank item.

### RISK
- [N-U32-014] Foreign-currency bank lines are converted to company currency at the line date, or with bank-given rates, without any tax. Whatever classifies such a line must add the tax treatment itself.

### UNKNOWN
- [N-U32-015] How a reconciliation tool outside the studied product would add tax lines, tags and rounding to a bank entry cannot be determined here; the helper that carries preset and tax data has no caller in the studied product.

## CAP-U32-02 Employee expense taxes

### WHAT
- [N-U32-016] An expense claim carries purchase-type taxes that default from the product and behave as tax-included, so the typed total is split into an untaxed amount and a tax amount.
- [N-U32-017] Employee-paid expenses are posted as purchase receipts addressed to the employee. Company-paid expenses are posted as one journal entry per expense, together with the payment line.

### WHY
- [N-U32-018] Receipts are created in company currency, so every expense is converted once at the expense rate and tax is computed on that converted total.

### BUSINESS RULE
- [N-U32-019] In a foreign-currency expense the company-currency tax is recomputed on the converted total in company currency, and the user can set a custom rate by typing the company-currency total.
- [N-U32-020] The tax lines of each expense are kept separate from those of other expenses on the same receipt, so every expense keeps its own tax lines.
- [N-U32-021] The vendor taxes of the product, limited to the expense company, are the default; the employee or approver may change them while the expense is editable.
- [N-U32-022] When an expense is re-invoiced, the customer receives the customer taxes of the product mapped by the order position, not the taxes of the expense. The price is the list price of the product, or the unit cost of the expense without tax.
- [N-U32-023] The margin of a re-invoiced expense line uses the untaxed expense amount as cost.
- [N-U32-024] A company-paid expense takes its tax from the tax engine, using the rate implied by the expense totals. The base item absorbs rounding, so that the entry equals the expense total.

### STATE
- [N-U32-025] Cancelling or reversing a receipt detaches the expense so that it can be reimbursed again. The reversal itself is the ordinary credit-note reversal.

### OPTIONALITY
- [N-U32-026] The mail-gateway entry path and the product-creation context can leave expense taxes blank or limited to the exact company, which differs from the manual path.
- [N-U32-027] In the studied database all seven expense products carry the standard 7 percent sales tax and 7 percent purchase tax, the company has a default expense journal and no expense exists.

### DEPENDENCY
- [N-U32-028] Receipts are posted through the standard posting routine into the company expense journal, or the first purchase journal, dated today, so lock dates and numbering of ordinary documents apply to them.

### CONSTRAINT
- [N-U32-029] Splitting an expense divides the total into two rounded halves that add up exactly, each keeping the taxes; the split tax is computed as tax-included.

### RISK
- [N-U32-030] Whether the entry created for a company-paid expense is read by the input-tax ledger as a purchase document, and which supplier identity appears for employee-paid receipts, is not settled without a run.

### UNKNOWN
- [N-U32-031] Cash-basis tags are requested only for company-paid expenses, and no Thai withholding treatment of expense lines was traced; numeric results were not executed.

## CAP-U32-03 Landed costs, manufacturing and subcontracting entries and their tax interaction

### WHAT
- [N-U32-032] A landed cost spreads extra purchase-related costs, taken from vendor-bill lines flagged for it, over received goods. The amount used is the bill line before tax.
- [N-U32-033] Manufacturing records, subcontracting records, the manufacturing work-in-progress entry and the landed-cost targets for manufacturing contain no tax logic; the search found no tax handling in them.

### WHY
- [N-U32-034] Tax on the vendor bill stays on the bill, so recoverable tax is not added to stock cost by a landed cost; only the untaxed cost is allocated.

### BUSINESS RULE
- [N-U32-035] Validating a landed cost creates a journal entry that debits stock valuation and credits the cost account for goods still on hand. The entry has no tax lines.
- [N-U32-036] A negative landed cost reverses the entry; a validated landed cost cannot be cancelled.

### STATE
- [N-U32-037] A landed cost is draft, posted or cancelled. Validation posts the entry with the standard posting routine, so lock-date date shifting applies.

### OPTIONALITY
- [N-U32-038] Landed costs create entries only for products valued in real time. Under periodic valuation, as in the studied database, only the value of the stock moves is updated.
- [N-U32-039] In the studied database the landed-cost, manufacturing and subcontracting modules are installed with their access rows, and no landed cost or manufacturing entry exists.

### DEPENDENCY
- [N-U32-040] Landed costs apply only to products costed at average or first-in-first-out; with standard cost, as in the studied database, none can be applied.
- [N-U32-041] For subcontracted purchases the price difference of a bill adds the component cost, and the price-difference lines of a bill carry no tax. Both matter only when automated valuation is switched on.

### CONSTRAINT
- [N-U32-042] The manufacturing overview report leaves out recoverable tax from the purchase cost it shows; this is a report only and changes no entry.

### RISK
- [N-U32-043] Because none of these flows has tax logic, any tax treatment of manufacturing, subcontracting service or landed-cost documents must come from the vendor bill and purchase order paths; nothing adjusts input tax for them.

### UNKNOWN
- [N-U32-044] Landed costs and subcontracting bills carrying non-deductible tax or withholding, and the entries under automated valuation, were not executed.

## CAP-U32-04 Electronic-invoice tax hooks

### WHAT
- [N-U32-045] A tax can be given an electronic-invoicing category code and an exemption reason code. The category codes are a European standard set, and the reason codes are European Union and French entries only.
- [N-U32-046] When a code is missing the exporter predicts one: a same-country zero tax becomes exempt, a tax with a negative factor becomes reverse charge and other taxes become standard. Export and intra-community codes appear only when a party is in the European Economic Area.

### WHY
- [N-U32-047] The exemption reason is taken from the tax itself and otherwise from a default text for the predicted category, so that an exported document can explain a line without tax.

### BUSINESS RULE
- [N-U32-048] Withholding-type taxes, meaning percent taxes with a negative rate, are reported in a separate withholding total, left out of the line-level tax categories and subtracted when the tax-inclusive total is built.
- [N-U32-049] Taxes that are not percent taxes, and excise-type and recycling-type taxes, never appear in the tax category totals.
- [N-U32-050] The tax scheme is VAT unless the supplier country belongs to a goods-and-services-tax set, which does not include Thailand.
- [N-U32-051] Every invoice line other than sections and notes must carry at least one tax before an export is accepted, except combo products.
- [N-U32-052] A payable rounding amount reconciles the engine total with the exported tax-inclusive total, and the payable amount is the residual of the document, so a partly paid document exports the residual.

### STATE
- [N-U32-053] An export is attempted at sending time for sales documents, or for buyer-issued purchase documents. Errors are reported and sending continues without the file.
- [N-U32-054] An older framework hooks into posting, reset and cancel of documents and offers a tax-detail helper; no format is registered in the studied database.

### OPTIONALITY
- [N-U32-055] No export format is bound to Thailand. A partner can be given a European format by hand, which was not run.
- [N-U32-056] None of the 18 Thai taxes has an electronic-invoicing code. The zero-rated and the exempt Thai taxes would both be predicted as exempt.

### DEPENDENCY
- [N-U32-057] On import the tax of each line is searched by type, use, amount and optional name, country and code, trying the default tax of the account first and then tax-included or tax-excluded variants for the fiscal position. Unmatched taxes are logged and the line is left without tax.

### CONSTRAINT
- [N-U32-058] The tax structure is validated before an export, and an invalid tax stops it.
- [N-U32-059] After an import, tax amounts are rewritten to the tax total of the file when every tax was matched and the difference is within 0.03 currency units.

### RISK
- [N-U32-060] Two generations of tax-total code coexist, so the tax and withholding totals produced for a given format depend on which generation that format uses; this was not traced to execution.

### UNKNOWN
- [N-U32-061] Format-specific builders were not studied; they are future optional country-pack material. How a Thai document would be exported, and what a Thai-specific format would require, is not established.

## CAP-U32-05 Discount, loyalty, delivery, product-matrix and margin lines

### WHAT
- [N-U32-062] A delivery charge is an order line of a carrier product. Its tax is the customer tax of that product mapped by the order fiscal position and set directly on the line, and the price quoted by a provider is adapted to the tax mapping.
- [N-U32-063] Loyalty rewards add order lines: a free product is a fully discounted line with its product taxes, a discount is split into one negative line per tax set of the discounted lines, and free shipping copies the tax of the delivery line.

### WHY
- [N-U32-064] The split lines add up to the capped discount, which can never exceed the order total, so the tax reduction stays exact when an order mixes tax treatments.

### BUSINESS RULE
- [N-U32-065] Fixed-amount taxes are not discounted, except for gift cards and wallets, which may pay the whole total.
- [N-U32-066] Price-included taxes are added to the discountable base, while other taxes are recomputed on the discount line.
- [N-U32-067] Redeeming a gift card takes the tax of the reward product and treats the redeemed price as tax-included, while selling a gift card is untaxed by default.
- [N-U32-068] Free-shipping and loyalty thresholds compare tax-inclusive totals unless the rule says tax-excluded, and payment-type lines do not count towards them.
- [N-U32-069] Margin is computed on untaxed amounts; with the delivered policy the line margin ignores discount and tax on the line.

### STATE
- [N-U32-070] Matrix cells create order lines from product and quantity only, so their taxes follow the standard line rules.

### OPTIONALITY
- [N-U32-071] In the studied database the reward discount product carries the standard 7 percent sales tax, while the gift-card product has no sales tax, and the delivery products carry the 7 percent tax.

### DEPENDENCY
- [N-U32-072] A vendor bill can be turned into purchase order lines or down-payment lines. Down-payment lines copy the bill taxes unchanged, order lines recompute their taxes from the product and the fiscal position, and the bill price is converted at the order date.

### CONSTRAINT
- [N-U32-073] The matrix, margin and manufacturing-margin modules contain no tax logic of their own.

### RISK
- [N-U32-074] Reward lines are mapped by the fiscal position twice, when they are built and when line taxes are computed; the effect of a mapping chain was not run.

### UNKNOWN
- [N-U32-075] The numeric tax effect of gift-card redemption, stacked rewards and free shipping with withholding taxes was not executed.

## CAP-U32-06 Down-payment lines

### WHAT
- [N-U32-076] An advance is computed from the tax-inclusive order total through the tax engine, then split into lines per tax set so that tax is stated in proportion to the advance.

### WHY
- [N-U32-077] Tax on an advance is stated when the advance is invoiced and is reversed at the same amounts on the final invoice.

### BUSINESS RULE
- [N-U32-078] Every percent-type tax, including negative withholding rates, takes part in the advance, while fixed and formula taxes are folded into the base.
- [N-U32-079] With several taxes each tax reaches its own rounded share of the advance, and any remaining rounding is spread across the lines.

### OPTIONALITY
- [N-U32-080] No down-payment account is set in the studied database, so advance lines use the product advance account or the income account mapped by the fiscal position.

### UNKNOWN
- [N-U32-081] The combined behaviour of an advance with a global discount, an early-payment discount or withholding taxes in one order was not executed.

## CAP-U32-07 Early-payment discount tax-base redistribution with several taxes

### WHAT
- [N-U32-082] The early-payment discount can reduce tax when the invoice is created (mixed mode) or when it is paid (included mode). All payment terms in the studied database use the included mode, so tax changes happen at payment.

### BUSINESS RULE
- [N-U32-083] In mixed mode the discount lines are grouped by account, analytic split and the whole tax set of the line. Lines with several taxes form one discount line carrying that tax set, and lines with different tax sets stay separate.
- [N-U32-084] Fixed and formula taxes are left out of the discount base, both at invoicing and at payment.
- [N-U32-085] At payment each tax is recomputed on the remaining share of the price and the difference is booked per tax distribution line with reversed tags. Partial payments scale the adjustment, and a rounding remainder goes to the biggest base line.
- [N-U32-086] Base adjustments are booked on the company early-payment loss account for receivables and the gain account for payables, and any exchange difference goes to the exchange accounts.

### STATE
- [N-U32-087] An order in mixed mode shows a taxed negative line and an untaxed positive line for each priced line, while the invoice groups them by tax set.

### RISK
- [N-U32-088] The order excludes only fixed taxes while the invoice excludes every non-discountable tax, so the order tax total and the invoice tax total can differ by rounding when several lines and taxes are present.

### UNKNOWN
- [N-U32-089] No early-discount line builder was found for purchase orders, so whether a supplier discount changes the tax of a purchase order before billing is not established.

## CAP-U32-08 Fiscal-position and partner-driven tax mapping at document hand-offs

### WHAT
- [N-U32-090] A fiscal position maps taxes and accounts. Sales orders compute it from customer and shipping address, purchase orders set it when the vendor is chosen, invoices and bills compute it from partner and delivery address, purchase receipts use the company default receipt position, and expenses use none.

### BUSINESS RULE
- [N-U32-091] Sales order line taxes are mapped by the order position and are recomputed only when the user runs the update-taxes action.
- [N-U32-092] An invoice created from an order receives the order position, otherwise the one found for the invoice partner; a bill created from a purchase order does the same with the order partner.
- [N-U32-093] Purchase line taxes are the vendor taxes of the product mapped by the order position, set by explicit routines and not by a stored computation, so a line created by code keeps no tax unless the creator sets it.
- [N-U32-094] Purchase orders created by replenishment or from a requisition evaluate the position for the vendor themselves.
- [N-U32-095] Default line taxes are narrowed to the company and then mapped by the position of the document.

### OPTIONALITY
- [N-U32-098] The studied database has no fiscal position and no default receipt position, so every hand-off yields an empty position and foreign customers and vendors need a manual tax choice.

### DEPENDENCY
- [N-U32-096] An imported electronic invoice evaluates the position on a new document built from the company, the type and the retrieved customer, and a tax can be restricted to specific positions.
- [N-U32-099] When the optional tax-number validation add-on is installed, a position that requires a tax number also needs an online-verified flag, but only for European companies or partner countries with a foreign position.

### CONSTRAINT
- [N-U32-097] The finder reads the first two characters of the company and partner tax numbers as country codes for its European rules.

### RISK
- [N-U32-100] For a Thai company the European branch of the finder is not expected to be taken because Thai tax numbers are numeric; this was inferred and not run.

### UNKNOWN
- [N-U32-101] The behaviour of foreign customers and vendors with a configured fiscal position cannot be shown because the studied database has none.

## CAP-U32-09 Optional tax add-ons that are not installed

### WHAT
- [N-U32-102] Four optional add-ons that are not installed were read at source for calculation and entry effects: a formula-tax add-on, a withholding-on-payment add-on, a tag-update tool and a debit-note tool.

### BUSINESS RULE
- [N-U32-103] A formula tax is evaluated in the same early pass as fixed taxes, before price-included and price-excluded taxes, on the base that already includes extra base from earlier taxes, and it is excluded from discounts, advances and early-payment splits.
- [N-U32-104] A formula tax that includes its amount in the base is exported as an excise-type charge and not in the tax totals.
- [N-U32-105] Withholding taxes on payment are filtered out of the document computation, computed for a given base by the tax engine, and fed back as manual tax amounts so the payment entry reproduces the user values with the payment-date rate.
- [N-U32-106] The tax lines of a withholding set are produced by the generic tax-line builder and carry distribution line, account and tags; the base item has no tax or tag and the counterpart item carries the grid values.
- [N-U32-107] The tag-update tool re-tags tax lines from their own distribution line and base lines from the base distribution line of the document type, for all lines of the company from a start date; it never recomputes amounts.
- [N-U32-108] A debit note is a copy of the original with a new date, no payment term and a link to the original; invoice and bill copies keep only line creation commands, so lines are rebuilt and taxes re-synchronised in draft.

### RISK
- [N-U32-109] A formula tax with the price-included flag would subtract its amount from the base and nothing forbids the combination; its numeric effect was not run.

### UNKNOWN
- [N-U32-110] The four add-ons were not executed; their numeric effects together with Thai VAT and withholding taxes remain unknown.

## CAP-U32-10 Other entry generators that carry no tax

### WHAT
- [N-U32-111] Cut-off and reclassification entries move amounts between periods or accounts as percentages of source lines, with name, account, partner, currency and analytic split only; they copy no tax, tag or distribution line.
- [N-U32-112] Accrual entries for orders use untaxed amounts, taking the untaxed value from the tax computation when taxes are price-included, and map the account by the order fiscal position.

### BUSINESS RULE
- [N-U32-113] Price-difference lines created on a vendor bill sit outside its tax lines and carry an empty tax set.

### UNKNOWN
- [N-U32-114] The effect of a cut-off reclassification of a taxed base line on the tax report, and the accrual of price-included lines, were not executed.
