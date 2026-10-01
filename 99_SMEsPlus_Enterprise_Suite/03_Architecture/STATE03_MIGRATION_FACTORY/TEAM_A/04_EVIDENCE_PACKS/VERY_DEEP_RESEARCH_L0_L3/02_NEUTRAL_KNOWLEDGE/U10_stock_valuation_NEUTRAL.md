# U10 — Stock Valuation and Landed Costs — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source product: Odoo 19 Community. Unit U10, capabilities 01 to 09.
> This file states what a stock valuation function must do and why, in plain business language, with no implementation names.

## Capability 01 — Where and how stock value and cost are stored, and the costing methods

### WHAT
- [N-U10-001] Stock value is not kept in a separate ledger of valuation layers. It is derived from three things: the value stored on each completed stock movement, the product's current unit cost, and a history of manual cost changes.
- [N-U10-002] Each completed movement into or out of the company's valued locations stores its own total value in company currency. A movement that is not valued stores zero.
- [N-U10-003] Remaining quantity and remaining value of an incoming movement are worked out on demand from the current stock on hand. They are not stored.
- [N-U10-004] A cost-history record captures each manual change of a product cost, a lot cost or a single movement's value, with date, user and description.
- [N-U10-005] Total value and average cost of a product are calculated on demand according to the product's costing method, optionally as of a past date.
- [N-U10-006] Three costing methods exist: fixed standard cost, first-in first-out, and weighted average cost.

### WHY
- [N-U10-007] The purpose is to give every stocked product a defensible unit cost and total value at any date, which feeds cost of goods sold, sales margin and the period-end valuation entry.

### BUSINESS RULE
- [N-U10-008] A product's costing method comes from its product category when one is set for the company, otherwise from the company default, which is standard cost.
- [N-U10-009] Only stock held in internal or in-transit locations of the company and owned by the company counts as valued stock. Goods owned by third parties are excluded.
- [N-U10-010] A movement counts as incoming when picked goods go from a non-valued location into a valued one, and as outgoing in the opposite case. Drop-shipped movements are treated separately.
- [N-U10-011] Under standard cost, stock is valued at quantity on hand times the single product cost, and receipts and issues are both valued at that cost.
- [N-U10-012] Under average cost, after a receipt the product cost becomes the previous quantity times the old cost plus the receipt value, divided by the new quantity on hand.
- [N-U10-013] Under average cost, when stock was zero or negative before a receipt, the average restarts at the receipt's own unit value.
- [N-U10-014] Under average cost, issues leave at the running average cost.
- [N-U10-015] Under first-in first-out, an issue is valued from the oldest incoming movements still on hand, taking only a part of the oldest one when needed.
- [N-U10-016] Under first-in first-out, the product cost is the total value of stock on hand divided by the quantity on hand, or the unit cost of the last receipt when nothing is on hand.
- [N-U10-017] When more is issued than the receipt history covers, the shortfall is valued at the last known unit cost, or at the product cost if no receipt exists.
- [N-U10-018] A receipt's value is decided in priority order: a manual adjustment, posted vendor bill amounts, production cost, purchase order price, the value of the original delivery for customer returns, and finally the product cost. Landed costs are then added unless the value was manually adjusted.
- [N-U10-019] An outgoing movement is valued when it is completed, just before it is finalised, so that the pool of incoming movements is still intact. Incoming movements are valued just after finalisation.
- [N-U10-020] A customer return is valued proportionally at the original delivery's value when no bill or order price applies.
- [N-U10-021] Inventory gains and losses have no purchase document, so they are valued at the product cost, or at the lot cost for lot-valued products.
- [N-U10-022] Changing the costing method of a category, or moving a product to a category with a different method, triggers recalculation of the product cost under the new method.
- [N-U10-023] A product can be valued per lot or serial number. The lot then carries its own cost and every movement line must carry a lot.

### STATE
- [N-U10-024] A movement has no value until it is completed. Its value can be re-derived afterwards when a vendor bill, order price, landed cost or manual adjustment changes.

### OPTIONALITY
- [N-U10-025] The costing method is chosen at company level as the default and at category level as an override. There is no product-level override.
- [N-U10-026] Valuation by lot is optional per product and is only available for tracked products.

### DEPENDENCY
- [N-U10-027] Receipt values depend on purchase orders and vendor bills when purchasing is installed, and on production cost when manufacturing is installed. Without them a receipt is valued at product cost.
- [N-U10-028] Quantity on hand, location types and ownership come from the inventory core. The valuation modules do not define them.

### CONSTRAINT
- [N-U10-029] Lot valuation cannot be switched on while stock without a lot exists in valued locations, and a movement of a lot-valued product is refused when a line has no lot.
- [N-U10-030] A historical product cost for a given date is available only for standard-cost products.

### RISK
- [N-U10-031] Any assumption carried from earlier releases that stock value sits in per-receipt layer records with a stored remaining quantity and remaining value is not valid for this release.
- [N-U10-032] For average-cost and standard-cost products the remaining value of a movement is the remaining quantity times the current product cost, so it is not a historical cost.
- [N-U10-033] Valuation as of a past date under average cost replays movement history. Duration with large histories was not measured.

### UNKNOWN
- [N-U10-034] The numeric effect of completing incoming and outgoing movements in the same operation is flagged as a limitation by the source and was not established without execution.
- [N-U10-035] The restored database holds no stock movements and no stocked products, so none of the valuation paths was observed with data.

## Capability 02 — Valuation mode switch (periodic versus perpetual) and the accounting-style flag

### WHAT
- [N-U10-036] Two valuation modes exist: periodic, where accounting entries are suggested at closing, and perpetual, where entries are created automatically when a product is billed or invoiced.
- [N-U10-037] A separate company-level accounting-style flag exists. In the studied modules it controls price-difference postings on vendor bills for standard-cost products. It is distinct from the valuation mode.

### WHY
- [N-U10-038] The mode decides whether the stock account and cost of goods sold are kept current by billing documents or reconciled in a periodic closing entry.

### BUSINESS RULE
- [N-U10-039] A product's mode comes from its category when set for the company, otherwise from the company default, which is periodic.
- [N-U10-040] In perpetual mode a vendor bill line for a stocked product is booked to the stock account instead of the expense account.
- [N-U10-041] In perpetual mode, posting a customer invoice adds cost-of-goods-sold and stock account lines for stocked products.
- [N-U10-042] In perpetual mode, a completed movement to or from a location that has a valuation account, such as inventory loss or production, creates an immediate entry. In periodic mode that reclassification is done at closing.
- [N-U10-043] The closing entry compares total inventory value with the posted stock account balance for all stocked products, whatever their mode.
- [N-U10-044] The accounts involved are a stock valuation account (category, then company), an expense account, a stock journal, optionally a stock variation account and an expense counterpart on the stock account, and a price difference account on the category.
- [N-U10-045] Company valuation settings are copied as defaults for product categories each time the company record is saved.

### STATE
- [N-U10-046] Changing the mode of a category has no automatic re-posting step. Existing documents keep the accounting they produced.

### OPTIONALITY
- [N-U10-047] Mode and costing method are set as company defaults and per category. The company-level selectors have no screen in the standard interface and are set by data, by chart loading or by configuration.
- [N-U10-048] Price-difference postings occur only when the company flag is on and the product is standard cost.

### DEPENDENCY
- [N-U10-049] Chart loading supplies the default stock journal and valuation account. The generic chart supplies the journal, the valuation account and the flag. The Thai chart supplies only the valuation account.

### CONSTRAINT
- [N-U10-050] Searching products by valuation mode supports only equality with the two defined values.

### RISK
- [N-U10-051] The valuation mode and the accounting-style flag are easy to confuse. Baseline notes that describe the accounting-style flag as the perpetual-valuation flag are imprecise for this release.
- [N-U10-052] If a perpetual product moves through a valued special location while the company has no stock journal, creation of the entry may fail. This was not executed.

### UNKNOWN
- [N-U10-053] The effect of switching a category to perpetual while stock already exists is not described in source and needs execution.
- [N-U10-054] In the restored database the company mode is periodic, the flag is off, every category inherits the company mode, and the company has no stock journal set although an inventory valuation journal exists.

## Capability 03 — Accounting entries at receipt and delivery, billing timing and returns

### WHAT
- [N-U10-055] In the default configuration, receiving or delivering goods does not by itself create a stock accounting entry. The stock account is debited by the vendor bill and credited by cost lines added to the customer invoice.
- [N-U10-056] A completed movement creates its own entry only when one of its locations carries a valuation account, for example inventory loss or production, and the product is in perpetual mode.
- [N-U10-057] A posted customer invoice for a stocked perpetual product receives two extra lines: cost of goods sold debited and the stock account credited.
- [N-U10-058] When the company flag is on, a vendor bill for a standard-cost product receives price-difference lines.

### WHY
- [N-U10-059] Entries follow billing documents so that the stock account, payables and cost of goods sold stay consistent with invoices rather than with physical movements alone.

### BUSINESS RULE
- [N-U10-060] A posted vendor bill sets the value of the matching receipts. Billed quantity beyond what earlier receipts cover is applied to later receipts, and refunds reduce the billed quantity and value.
- [N-U10-061] Until billed, a receipt is valued at the purchase order price excluding recoverable taxes, converted to company currency at the order date.
- [N-U10-062] The cost-of-goods-sold amount per unit comes from the value of the delivered movements, and cost already booked for the same sales line is deducted, so partial and repeated invoicing book only the difference.
- [N-U10-063] For a credit note, the cost lines are reversed using the unit cost of the original invoice for standard and average methods.
- [N-U10-064] A customer return received before invoicing is valued at the original delivery's value and creates no invoice line. A flag on the return decides whether the sales or purchase order quantities are reduced.
- [N-U10-065] A vendor return is an outgoing movement valued at product cost or from the first-in first-out pool. A vendor refund reduces the billed quantity and value.
- [N-U10-066] Drop-shipped goods are excluded from the stock lines added to invoices because they never enter valued locations.
- [N-U10-067] The price difference is the billed unit price minus the standard cost, times the billed quantity, booked to the category's price difference account with an offset on the bill line's own account.
- [N-U10-068] One entry is created per completion call, grouping all valued movements, dated today unless an accounting date is supplied. It is posted immediately.
- [N-U10-069] Cost lines are skipped when the stock account or expense account is missing or the amount is zero.

### STATE
- [N-U10-070] Cost lines created at invoice posting are removed when the invoice is reset to draft or cancelled. Copying an invoice drops them unless the copy is a reversal.

### OPTIONALITY
- [N-U10-071] All of the above applies only to perpetual products. Periodic products rely on the closing entry.

### DEPENDENCY
- [N-U10-072] Finding the movements behind an invoice line needs the sales and purchasing integration modules. Without them cost lines would have no movements to read.
- [N-U10-073] Valuation entries are posted through the normal posting path and therefore obey accounting lock dates.

### CONSTRAINT
- [N-U10-074] A valuation entry dated inside a locked period cannot be posted.

### RISK
- [N-U10-075] Because cost of goods sold is booked at invoicing and not at delivery, goods delivered but not yet invoiced are not in cost of goods sold until the closing entry is run.
- [N-U10-076] Between receipt and vendor bill, inventory value includes the receipt at order price while the stock account does not yet include it. The difference is only reconciled by the bill or by the closing entry.
- [N-U10-077] The price-difference postings test the company flag and the standard cost method but not the product's valuation mode, so a periodic product could also receive them.

### UNKNOWN
- [N-U10-078] Exact entries for combined partial deliveries, partial invoices and returns need execution to confirm.

## Capability 04 — Inventory valuation closing at period end

### WHAT
- [N-U10-079] A daily scheduled job creates and posts the stock closing entry for every company whose inventory period is daily, and on the last day of the month also for companies whose period is monthly.
- [N-U10-080] The same closing can be triggered by hand from the inventory valuation report for today or a past date. The manual run leaves the entry in draft.
- [N-U10-081] The closing entry has up to three parts: reclassification of valued special locations for periodic products, a global stock variation that aligns the stock account with the inventory valuation, and a period variation for accounts that have both a variation and an expense counterpart.

### WHY
- [N-U10-082] To bring accounting stock balances into line with the cost-based inventory valuation at period end without creating an entry per movement.

### BUSINESS RULE
- [N-U10-083] The stock adjustment equals total inventory value minus the posted stock account balance minus amounts already included in the same entry. Zero differences create nothing.
- [N-U10-084] The counterpart of the stock adjustment is the variation account linked to the stock account, or the company expense account when none is linked. If neither exists the account is skipped.
- [N-U10-085] Location reclassification covers movements dated after the previous posted closing and up to the chosen date.
- [N-U10-086] A closing dated before the last posted closing is refused.
- [N-U10-087] When nothing needs closing, the scheduled run ends silently and a manual run reports that everything is closed.
- [N-U10-088] The identifiers of the last ten closing entries are remembered per company in system parameters.
- [N-U10-089] Entry lines swap debit and credit when the computed balance is negative.

### STATE
- [N-U10-090] A closing entry is draft after a manual run and posted after a scheduled run. Once posted it counts as the last closing.

### OPTIONALITY
- [N-U10-091] The inventory period defaults to manual, in which case the scheduled job processes nothing for that company.

### DEPENDENCY
- [N-U10-092] A stock journal and a stock valuation account must be set on the company whenever an entry is needed.
- [N-U10-093] Posting honours accounting lock dates. In the scheduled run a user-facing refusal skips the company silently.

### CONSTRAINT
- [N-U10-094] Changing the done date of a completed transfer into a locked period (fiscal-year lock or hard lock) is refused unless a technical system parameter turns the check off.
- [N-U10-095] A missing journal or valuation account is reported only after a non-empty entry has been calculated.

### RISK
- [N-U10-096] Scheduled failures caused by user-facing errors are swallowed, so a company can stay unclosed without any alert.
- [N-U10-097] Month-end accrual of goods received or delivered but not invoiced is not produced by the closing. The accrual placeholder in the report is empty and the legacy helper calculations in the purchasing and sales integrations have no callers.

### UNKNOWN
- [N-U10-098] In the restored database the job is active and daily, but the only company has a manual period and no closing record exists, so no run has produced anything.
- [N-U10-099] Whether posting succeeds for a company that has no stock journal set was not executed.

## Capability 05 — Landed costs

### WHAT
- [N-U10-100] A landed cost document allocates extra costs such as freight and customs onto completed receipts or manufacturing orders and adds them to the value of the stocked products.
- [N-U10-101] Cost lines refer to a service product flagged as a landed cost, with an amount, a split method and an expense account.
- [N-U10-102] Five split methods exist: equal, by quantity, by current cost, by weight and by volume.

### WHY
- [N-U10-103] So that stock value reflects the true acquisition cost including costs billed separately from the goods.

### BUSINESS RULE
- [N-U10-104] Only products costed by first-in first-out or average cost can receive landed costs. Cancelled movements and movements with zero quantity are ignored.
- [N-U10-105] Equal split divides the amount by the number of valuation lines. By quantity uses units. By weight and by volume use product master data times quantity. By current cost uses the current value of the movement. A method whose total is zero falls back to an equal split.
- [N-U10-106] Each share is rounded half up to currency precision and any rounding difference is added to one line so that shares sum exactly to the cost line.
- [N-U10-107] Validation requires draft status and at least one target. Allocation lines must sum to each cost line and to the total. Missing allocation is calculated automatically before the check.
- [N-U10-108] For perpetual products, validation creates one entry: debit the stock account and credit the cost line's account for the part of the allocation matching the quantity still on hand. A negative cost reverses the entry.
- [N-U10-109] After validation each allocated movement's value rises by its share and the product cost is recomputed for first-in first-out and average products.
- [N-U10-110] A validated landed cost cannot be cancelled or deleted. To reverse it, a negative landed cost is created.
- [N-U10-111] A vendor bill that contains landed-cost service lines can generate a landed cost document mirroring those lines. Credit notes invert the sign.
- [N-U10-112] Valuation as of a past date includes landed costs only up to their own date.

### STATE
- [N-U10-113] A landed cost goes from draft to posted by validation, or from draft to cancelled. Posted is final.

### OPTIONALITY
- [N-U10-114] Landed costs are an optional feature switched on in inventory settings. A default journal can be set on the company.

### DEPENDENCY
- [N-U10-115] Landed costs need purchasing and stock accounting. Manufacturing, subcontracting and project variants extend the allowed targets and the analytic distribution.

### CONSTRAINT
- [N-U10-116] Errors are raised when validating a non-draft document, when no target is chosen, when totals do not match, when no eligible movement exists, and when no expense account can be found.

### RISK
- [N-U10-117] The entry covers only the quantity still on hand. The share relating to goods already sold stays in the expense account where the vendor bill booked it.
- [N-U10-118] Nothing in the logic requires the linked vendor bill to be posted, or checks that the bill's receipts match the transfers selected on the landed cost.

### UNKNOWN
- [N-U10-119] Effects on average cost with partly consumed receipts and on lot-valued products need execution.
- [N-U10-120] The restored database has the feature installed, a numbering sequence and no landed cost documents, and no default landed cost journal.

## Capability 06 — Cost changes, revaluation and adjustment or scrap valuation hooks

### WHAT
- [N-U10-121] A manual change of a product cost records a history entry and from then on values stock and issues at the new cost. No accounting entry is created at that moment.
- [N-U10-122] An individual movement's value can be overridden through an adjust-valuation action that records a history entry and re-derives the value.
- [N-U10-123] There is no dedicated revaluation wizard and no layer-based revaluation in this release.

### WHY
- [N-U10-124] To let cost corrections flow into stock value while keeping an audit trail of who changed what and when.

### BUSINESS RULE
- [N-U10-125] Cost changes on first-in first-out products are not recorded in history, because their cost is derived from receipts.
- [N-U10-126] A technical switch suppresses history recording when the system itself recalculates a cost.
- [N-U10-127] A lot cost change is recorded only for average-cost products. A product cost change on a lot-valued product is copied onto all its lots.
- [N-U10-128] A manual movement value applies to incoming movements. Outgoing movements are re-derived from cost and are not overridden.
- [N-U10-129] A product created with a cost gets an initial history entry dated at the earliest possible date.
- [N-U10-130] Inventory adjustments move goods from or to an inventory-loss location and are valued at product or lot cost. An entry is created only when that location has a valuation account and the product is perpetual.
- [N-U10-131] An optional accounting date on the inventory count overrides the date of the resulting entry.
- [N-U10-132] The loss account is the valuation account set on the inventory-loss location. Scrapped goods go to such a location.

### STATE
- [N-U10-133] A movement's value can be changed repeatedly. The latest history entry that applies prevails.

### OPTIONALITY
- [N-U10-134] The accounting date field appears only when at least one counted product is perpetual.

### DEPENDENCY
- [N-U10-135] Counting, scrapping and quantity updates belong to the inventory core. Valuation only reacts to the movements they create.

### CONSTRAINT
- [N-U10-136] Adjust valuation works on one movement at a time.

### RISK
- [N-U10-137] Because a cost change or movement value override creates no entry, the stock account diverges from the inventory valuation until the closing entry corrects it.
- [N-U10-138] Assumptions from earlier releases of a product revaluation wizard that books revaluation entries are not valid for this release.

### UNKNOWN
- [N-U10-139] Whether any caller outside the studied modules books an entry on a cost change was not found and was not executed.

## Capability 07 — Valuation reports and accounting properties

### WHAT
- [N-U10-140] An inventory valuation report shows, for a chosen date, the initial balance, ending stock, inventory loss, cost of production and stock variation by account, and offers to generate the closing entry.
- [N-U10-141] A cost audit report lists incoming and outgoing movements and manual cost adjustments for products that are not standard cost, with running quantity, value and average cost.
- [N-U10-142] Each quantity record carries a computed value, the forecast report header shows the stock value, and product lists show unit cost and total value, optionally as of a date.
- [N-U10-143] Accounting properties are held per company on categories (mode, costing method, journal, stock account, price difference account), on accounts (variation and expense counterparts), on locations (valuation account) and on products and lots (cost).

### WHY
- [N-U10-144] To let finance compare the cost-based inventory value with the accounting balances and to justify each cost.

### BUSINESS RULE
- [N-U10-145] A quantity record's value is its quantity times the unit value of the product, or of the lot for lot-valued products, and is zero outside valued locations or for third-party owned stock.
- [N-U10-146] The audit report replays movements chronologically and applies manual cost adjustments as resets of the average cost.
- [N-U10-147] The valuation report compares inventory value with posted accounting balances by stock account.
- [N-U10-148] Category defaults for the stock account are looked up from the category, then a stored default, then the company.

### STATE
- [N-U10-149] The reports are read only. They change no data except through the explicit generate-entry action.

### OPTIONALITY
- [N-U10-150] The valuation report is extended by manufacturing for cost of production, and the inventory-loss section appears only when a loss location has a valuation account.

### DEPENDENCY
- [N-U10-151] Visibility of values depends on stock manager rights, and of the audit report on stock manager or accounting read rights.

### CONSTRAINT
- [N-U10-152] Searching movements by remaining quantity supports only the is-set test.

### RISK
- [N-U10-153] Some front-end logic of the valuation report refers to a data key that the data provider does not return, so a displayed figure may be missing. This was not executed.

### UNKNOWN
- [N-U10-154] Report totals and rendering with real data were not observed.

## Capability 08 — Roles, record rules, multi-company scope, constraints and configuration check

### WHAT
- [N-U10-155] Stock managers have full rights on cost-history records, landed cost documents and allocation lines, and read rights on the cost audit report. Accounting read-only users can read the audit report. Invoicing users can read, change and create transfers and movements, but not delete them.
- [N-U10-156] Record rules restrict cost-history records, the cost audit report and landed cost documents to the user's allowed companies.

### WHY
- [N-U10-157] To keep cost data visible to the people who manage stock and finance, and separated by company.

### BUSINESS RULE
- [N-U10-158] Product and lot unit costs are visible to internal users, while the value of a quantity record is visible only to stock managers.
- [N-U10-159] Cost history, valuation entries and analytic lines are written with elevated rights so that users without accounting rights can still complete stock operations.
- [N-U10-160] The closing job runs as the system administrator user.
- [N-U10-161] Cost, valuation mode, journal and accounts are held per company. Totals across several companies are converted into the current company's currency. First-in first-out pools are searched across the allowed companies.

### STATE
- [N-U10-162] Not applicable: access rules carry no state machine.

### OPTIONALITY
- [N-U10-163] An optional right group shows lots and serial numbers on invoices.

### DEPENDENCY
- [N-U10-164] The rights rely on stock manager, stock user, accounting invoicing and accounting read-only groups defined elsewhere.

### CONSTRAINT
- [N-U10-165] Validations raised in valuation: lot required for lot-valued products, no lot valuation with stock lacking a lot, one movement per manual adjustment, historical cost only for standard cost, closing order and missing accounts, locked-period transfers, and landed cost state and total checks.

### RISK
- [N-U10-166] Transit locations without a company are treated as outside the company. Goods moving through the inter-company transit location are therefore valued as leaving or entering the company, and no automatic inter-company valuation entry exists in the studied modules.
- [N-U10-167] Company rules exist on the cost-history records, the audit report and the landed cost header. Cost lines and allocation lines have no rule of their own and rely on their parent record.

### UNKNOWN
- [N-U10-168] In the restored database the studied access entries and rules exist as defined and there is a single company, so multi-company behaviour was not observed.

## Capability 09 — Cross-module trigger map into valuation

### WHAT
- [N-U10-169] Several other modules call into valuation: purchasing supplies bill and order values, sales supplies the movements and cost already booked behind invoice lines, manufacturing supplies production cost, subcontracting adjusts value and price difference, drop shipping defines which movements are external, repair excludes accounted lines, point of sale and projects read the flag or the movements, and margin reads delivered cost.

### WHY
- [N-U10-170] Valuation cannot find costs or movements by itself. Each integration module links invoices, orders and productions to stock movements.

### BUSINESS RULE
- [N-U10-171] Purchasing supplies the bill-based and order-based value of receipts, triggers revaluation when an order line price or quantity changes, and adds price-difference lines to bills.
- [N-U10-172] Sales supplies the delivered movements, the quantity and cost already booked on earlier invoices, and the original invoice's cost for credit notes.
- [N-U10-173] Manufacturing supplies the production value of finished goods, the cost of kits and a labour entry; subcontracting adjusts the value and price difference for service cost.
- [N-U10-174] Sales margin uses delivered cost for non-standard products and product cost otherwise.

### STATE
- [N-U10-175] Not applicable: this capability is a map of callers and carries no state machine.

### OPTIONALITY
- [N-U10-176] Each caller is active only when its module is installed. Point of sale is not installed in the restored database.

### DEPENDENCY
- [N-U10-177] All callers assume the valuation module's extension points exist and may be overridden by further modules.

### CONSTRAINT
- [N-U10-178] No additional constraints were found at the caller boundaries beyond those listed under the other capabilities.

### RISK
- [N-U10-179] Several callers override the same extension points, so the effective behaviour depends on which modules are installed together.

### UNKNOWN
- [N-U10-180] The point-of-sale valuation path was read from source only; it is not installed in the restored database.

