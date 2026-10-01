# U02 - Product, units, pricing and analytic foundations - Neutral Knowledge

> Layer: NEUTRAL KNOWLEDGE (clean-room). Source basis: Odoo 19 Community, study date 2026-10-02.
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Statements are tagged with identifiers and linked to the restricted evidence layer by the same identifiers.

## CAP-U02-01 Product master: definition and variants, product type, inventory tracking, variant generation, archiving, uniqueness

### WHAT

- [N-U02-001] The product master has two levels: a product definition that holds description, price, taxes, policies and attributes, and one or more variants that represent each concrete item that can be sold, bought or stocked.
- [N-U02-002] Identity data such as internal reference, barcode, cost, weight and volume belong to the variant; the definition mirrors them only when it has exactly one variant and shows them blank when it has several.
- [N-U02-003] Every product has one type: goods, service or combo, and a new product is goods by default.
- [N-U02-004] Inventory tracking is a separate yes-or-no choice that exists only for goods and is what makes a product behave as a stocked item.
- [N-U02-005] A combo is a sellable bundle made of one or more choice groups, each offering a list of ordinary products.

### WHY

- [N-U02-006] Separating the definition from the variant lets one commercial item be offered in many size, colour or option combinations while sharing one description, one set of policies and one price base.
- [N-U02-007] Separating goods from the tracking choice lets a business sell physical items it does not count in stock (supplies, expensed items) without stock valuation, while services and combos never touch the warehouse.

### BUSINESS RULE

- [N-U02-010] Setting the product type to service or combo automatically switches inventory tracking off.
- [N-U02-011] Switching inventory tracking off also resets lot and serial tracking to plain quantity tracking.
- [N-U02-012] When tracking is switched on for a product that already has completed movements, the system rebuilds on-hand balances from the movement history and applies an inventory adjustment so that valuation stays consistent.
- [N-U02-013] Only goods generate delivery and receipt movements; procurement ignores any product that is not goods and any request with a zero quantity.
- [N-U02-014] Goods that are not tracked still follow delivery and receipt documents but are never reserved from stock, and their availability is simply the requested quantity.
- [N-U02-015] Only tracked goods are eligible for stock valuation entries when a movement is done or a bill is posted.
- [N-U02-016] A sales line for goods is delivered through stock movements, and its ordered quantity cannot be reduced below the delivered quantity; a return must be used instead.
- [N-U02-017] A purchase line for goods is received through stock movements and generates receipts; other product types are not received this way.
- [N-U02-018] The invoicing policy of goods defaults to ordered quantities, the service tracking type defaults to manual quantities, and for tracked goods the cost re-invoicing policy is forced to none.
- [N-U02-019] The purchase billing control policy of a service is based on ordered quantities, while other products follow the system default of received quantities.
- [N-U02-020] A combo needs at least one choice group, each choice group needs at least one product without duplicates, combos cannot be nested, a combo cannot have attributes, cannot be purchasable and carries no taxes, and a sellable combo may contain only sellable products.
- [N-U02-021] Moving a product away from the combo type clears its choice groups.
- [N-U02-022] A service can be configured to create a project, a task or both when it is sold, or to create a vendor purchase request; these options apply only to services and are reset when the type changes to something else.
- [N-U02-023] Each attribute is flagged to create variants instantly, dynamically or never: instantly creates every combination as soon as values are added, dynamically creates a variant only when it is first needed on an order, never records the value without creating variants.
- [N-U02-024] Exclusion rules between attribute values remove impossible combinations from generation and from selection.
- [N-U02-025] The number of variants generated in one go is capped (one thousand by default, adjustable by a system parameter); above the cap the user is told to switch to on-demand creation.
- [N-U02-026] Adding an attribute that has a single value to an existing product does not multiply variants; the value is added to the existing variants.
- [N-U02-027] Variants that are no longer valid after a configuration change are deleted when unused and archived when referenced elsewhere; if every variant would disappear the change is refused.
- [N-U02-028] When any attribute of a product is dynamic, variants are not pre-generated; only already existing valid variants are kept or reactivated.
- [N-U02-029] Archiving a product definition archives all its variants, archiving the last active variant archives the definition, and reactivation reverses this and regenerates missing variants.
- [N-U02-030] Deleting the last variant of a definition deletes the definition too, unless variants can be created on demand.
- [N-U02-031] A barcode must be unique among the products visible to the same company, treating company-less products as visible to every company, and it may not equal any packaging barcode.
- [N-U02-032] A packaging barcode is unique across the whole system and may not equal any product barcode.
- [N-U02-033] A duplicate internal reference only produces a warning and is not refused.
- [N-U02-034] Free-text custom values for an attribute are captured per order line rather than on the product.

### STATE

- [N-U02-040] A product definition and a variant are either active or archived; there is no other lifecycle state.
- [N-U02-041] Inventory tracking can be switched on and off repeatedly; switching it off keeps existing on-hand records, switching it on again only counterbalances movements not already reflected.

### OPTIONALITY

- [N-U02-045] Variant management is an optional feature switch; observed in the studied configuration as enabled for all internal users.
- [N-U02-046] Inventory tracking, lot and serial tracking and route selection exist only when the inventory function is installed.
- [N-U02-047] Invoicing policies, project or task creation and vendor-purchase-on-sale options exist only when the corresponding sales, project and purchase functions are installed.

### DEPENDENCY

- [N-U02-050] Accounting, stock, sales, purchase and manufacturing all read the product type and the tracking choice to decide how a line is fulfilled, received, valued and invoiced.

### CONSTRAINT

- [N-U02-055] A product cannot be restricted to a company if its movements, on-hand quantities or sales documents already belong to another company.
- [N-U02-056] The variant creation mode of an attribute cannot be changed, and the attribute cannot be deleted or archived, while it is used on a product.
- [N-U02-057] An attribute value cannot be moved to another attribute while used, and an attribute line on a product needs at least one value and only values of its own attribute.
- [N-U02-058] At most one active variant may exist for a given combination of attribute values on a product.
- [N-U02-059] A multi-checkbox attribute can only be of the never-create-variants kind.

### RISK

- [N-U02-060] Changing the type of a product already used in movements or sales only raises a warning and is not blocked, which can leave history inconsistent; archiving and recreating the product is the safer path.
- [N-U02-061] Switching tracking on late creates adjustment movements that change valuation and on-hand quantities at that moment.
- [N-U02-062] Dynamic variants appear while orders are being entered, so the variant list of a product is not a complete picture of what can be sold.

### UNKNOWN

- [N-U02-065] Whether variant records are filtered by company in the same way as product definitions is not stated by any rule in these functions and needs runtime confirmation.
- [N-U02-066] The effect of data import on existing variants when attribute values differ is declared but its end-to-end behaviour has not been exercised.

## CAP-U02-02 Product categories and company-dependent defaults for accounting, valuation and routing

### WHAT

- [N-U02-070] Products are grouped in a hierarchical category tree; categories carry accounting, valuation and routing defaults that products in the category inherit.
- [N-U02-071] Some configuration values are company-dependent: the same record holds a separate value per company, and when no value is stored for the current company a system-wide default for that setting is used instead.
- [N-U02-072] When a company is created or its accounting defaults change, the company's income account, expense account, stock journal, stock valuation account, valuation method and costing method are written as the company-specific defaults for the matching category settings.

### WHY

- [N-U02-073] Keeping accounts and valuation settings on the category, per company, lets finance steer posting and costing for whole product families in each legal entity without editing every product.

### BUSINESS RULE

- [N-U02-075] The income account of a product is its own income account if set, otherwise the first one found walking up the category tree, otherwise the company default income account; the expense account is resolved the same way.
- [N-U02-076] The resolved accounts are mapped through the fiscal position of the document before use.
- [N-U02-077] The stock valuation account is the category value for the current company, then the default for that setting, then the company-level stock valuation account; the stock journal follows the same order.
- [N-U02-078] The production cost account is taken from the product's category even when empty; only a product without any category falls back to the default, and then only under perpetual valuation.
- [N-U02-079] The valuation method (periodic or perpetual) and the costing method (standard price, first-in-first-out, average cost) of a product are those of its category for the current company, falling back on the company setting.
- [N-U02-080] Changing the costing method of a category, moving a product to a category with a different method, or changing lot valuation triggers recalculation of the product standard prices and lot costs.
- [N-U02-081] The cost of a product is stored per variant and per company; the product definition shows it when a single variant exists, and a negative cost is refused in the form.
- [N-U02-082] The price difference account is the category value when the costing method is standard price, otherwise none.
- [N-U02-083] The responsible user, the production location and the inventory-loss location of a product are company-dependent values.
- [N-U02-084] A category carries selectable routes that its sub-categories inherit, plus a forced removal strategy and a rule on reserving full or partial packagings; these are not company-dependent.
- [N-U02-085] A category can define custom property fields that every product of the category fills in.
- [N-U02-086] The stored pricelist of a partner is company-dependent while the effective pricelist is computed from it, the country and fallbacks.
- [N-U02-087] The default applicability of an analytic plan is company-dependent and initialised to optional.

### STATE

- (no statement)

### OPTIONALITY

- [N-U02-092] Valuation, costing and stock account settings exist only when the inventory accounting function is installed, production accounts only with manufacturing accounting, income and expense accounts only with accounting.

### DEPENDENCY

- (no statement)

### CONSTRAINT

- [N-U02-090] A category cannot be its own ancestor.
- [N-U02-091] Income and expense accounts must be of an allowed kind (not receivable, payable, bank or cash, credit card, off-balance) and stock-related accounts must belong to the company.

### RISK

- [N-U02-093] A company-dependent value appears empty or default in other companies, so reading it in the wrong company context silently yields a different account or method.
- [N-U02-094] Accounts and methods are resolved at posting time; changing a category setting later does not restate history already posted.

### UNKNOWN

- [N-U02-095] How the platform physically stores and falls back company-dependent values is a core platform mechanism; only the observed storage form in the studied database is recorded here.

## CAP-U02-03 Price lists and price rules

### WHAT

- [N-U02-100] A price list defines, for one company scope and one currency, how the selling price of a product is derived; it holds an ordered set of rules.
- [N-U02-101] A rule either sets a fixed price, applies a percentage discount, or computes a price by formula from a base (sales price, cost, or another price list) using discount or markup, rounding, an extra fee and minimum and maximum margins.
- [N-U02-102] Each rule targets all products, a product category including its sub-categories, one product, or one variant, optionally within a date window and above a minimum quantity.

### WHY

- [N-U02-103] Price lists let the same product have different prices per customer group, country, currency, period or quantity break without changing the product's own sales price.

### BUSINESS RULE

- [N-U02-105] The rule applied is the first match in a fixed order: most specific target first (variant, then product, then category, then all products), then larger minimum quantity, then the category with the higher rank, then the most recently created rule.
- [N-U02-106] A rule matches only when the quantity, converted to the product's own unit, reaches its minimum quantity and the pricing date lies in its window, an empty start or end meaning open.
- [N-U02-107] When no rule matches, the price is the product's sales price converted to the requested unit and currency.
- [N-U02-108] Rule amounts are expressed in the product's own unit; when another unit is requested the fixed price, extra fee and margins are converted by the unit ratio.
- [N-U02-109] A formula rule computes base minus base times discount, rounds to a multiple if requested, adds the extra fee, then keeps the result at least the minimum margin above the base and at most the maximum margin above the base; for a cost base the markup replaces the discount.
- [N-U02-110] A percentage rule subtracts the percentage from the base, which is the sales price or the result of another price list.
- [N-U02-111] When the base is another price list, that list is evaluated for the same quantity, unit and date and its result is converted into the target currency at the pricing date.
- [N-U02-112] Currency conversion uses the exchange rate on the pricing date and the company of the current context, and the base amount is kept unrounded until the end.
- [N-U02-113] Extra prices from selected attribute values are added to the sales price before any rule is applied.
- [N-U02-114] The cost used as a base is read with system rights so users without cost visibility still obtain a computed price.
- [N-U02-115] To show a discount to the customer the system looks up the price before discount by following chained price lists only through percentage rules, and shows the larger of the original and the final price; this requires the per-line discount feature of sales.
- [N-U02-116] A partner's price list is the partner's own setting if active; otherwise the list for the partner's country group; otherwise a stored generic fallback; otherwise the first active list of the company; if the price list feature is off there is none.
- [N-U02-117] A draft sales order takes the partner's price list and its currency; the list can be changed on a draft only, a change affects only newly added lines until the user asks to update prices, and a confirmed order refuses a price list change.
- [N-U02-118] The unit price of a sales line is recalculated when product, unit or quantity change, unless the price was set manually or the line is already invoiced; the matching rule is remembered on the line.
- [N-U02-119] Vendor-side purchase prices do not use customer price lists; they come from vendor price lines on the product.
- [N-U02-120] A default price list per company is created when the feature is enabled and when a company is created while the feature is enabled.
- [N-U02-121] Disabling the feature archives every price list, archiving a currency archives its price lists, and enabling multiple currencies turns the feature on.
- [N-U02-122] A price list cannot be deleted while another price list uses it as the base of a rule.
- [N-U02-123] Scoping a price list to a particular web shop exists only with the web shop function; it is not installed in the studied configuration.

### STATE

- [N-U02-125] A price list and a rule are active or archived; rules have validity windows rather than states.

### OPTIONALITY

- [N-U02-126] Price lists are an optional feature switch; in the studied configuration the feature is on, one default price list exists and it has no rules.
- [N-U02-127] Showing a percentage discount on the sales line needs both a percentage rule and the sales line discount feature.

### DEPENDENCY

- [N-U02-128] Sales documents, product configurators and price-list reports call the price service with product, quantity, unit, date and currency and receive a price and the rule used.

### CONSTRAINT

- [N-U02-130] A rule based on another price list must name it, and circular chains of base price lists are refused.
- [N-U02-131] A rule end date must be after its start date, the minimum margin must not exceed the maximum margin, and the chosen target (category, product or variant) must be specified.
- [N-U02-132] A rule belongs to the company of its price list or, when the list has none, of its product, and changing the company of a price list re-checks its rules.
- [N-U02-133] Rules are normalised on save so unrelated target fields are cleared according to what the rule applies to.

### RISK

- [N-U02-134] Minimum quantities and amounts are in the product's own unit, so changing a product's unit later changes what existing rules mean.
- [N-U02-135] A variant-specific rule is applied when pricing a product definition only if the definition has exactly that one variant.

### UNKNOWN

- [N-U02-137] Final rounding of the displayed price to the currency precision at document level is outside this unit and not studied here.

## CAP-U02-04 Units of measure, conversion, rounding and packagings

### WHAT

- [N-U02-140] Units of measure form a tree in which each unit states how many of its reference unit it contains; units without a reference are roots (piece, hour, millimetre, gram and similar) and the absolute factor of a unit is the product of the ratios along its chain.
- [N-U02-141] The studied version has no fixed unit categories; whether two units belong together is determined only by sharing a root reference.
- [N-U02-142] Packagings are additional units attached to a product, optionally carrying their own barcode, and can be used on sales, purchase and stock lines.

### WHY

- [N-U02-143] A unit tree lets quantities and prices be converted between purchase, sales and stock units of the same product without maintaining conversion tables per category.

### BUSINESS RULE

- [N-U02-145] Every product has one base unit used for all stock operations; the units allowed on a line are the product's base unit, its packagings and, on purchase lines and replenishment, the units named on its vendor price lines.
- [N-U02-146] Quantity conversion multiplies by the source factor, divides by the target factor and rounds in the target unit, rounding up by default.
- [N-U02-147] Price conversion applies the inverse ratio of quantity conversion, so a larger unit has a proportionally larger unit price.
- [N-U02-148] All units share a single rounding precision taken from the system-wide Product Unit precision (two decimals by default) and not from each unit.
- [N-U02-149] Conversion between two units does not verify that they share a root; callers that care, such as timesheets, electronic invoice import and label printing, must test for a common reference themselves, and the failure flag offered by the conversion is not acted upon.
- [N-U02-150] A quantity can be rounded to a whole multiple of a packaging quantity using a chosen direction, with no rounding when the units are the same; stock reservation of packaged quantities uses this.
- [N-U02-151] Price list rules, vendor minimum quantities and procurement quantities are expressed in the product base unit or the vendor unit and are converted when another unit is used.
- [N-U02-152] Product weight, volume and length are expressed in single system-wide units chosen by setting: kilogram or pound, cubic metre or cubic foot, millimetre or foot.
- [N-U02-153] Changing the base unit of a product replaces the unit on existing sales, purchase and stock lines without converting quantities (one old unit equals one new unit); it is refused when other units were already used on those documents, and refused when posted journal entries use a different unit.
- [N-U02-154] Changing the conversion ratio of a unit is refused while open stock movements or move lines use it or on-hand quantities of products with that unit exist.
- [N-U02-155] Units shipped with the system are protected from deletion and can only be archived; hours, dozens and pack of six are the only unprotected ones.
- [N-U02-156] A packaging barcode links one unit to one product and must be unique across the whole system and distinct from any product barcode.
- [N-U02-157] When a procurement unit differs from the stock unit the quantity is converted to the stock unit, unless the setting to propagate the unit is on.
- [N-U02-158] A vendor price line carries its own unit and a minimum quantity in that unit, defaulting to the product base unit.

### STATE

- [N-U02-160] A unit is active or archived; many imperial and secondary units are shipped archived.

### OPTIONALITY

- [N-U02-161] Multiple units of measure is a feature switch that hides unit columns when off; in the studied configuration it is on for all internal users because the timesheet function turns it on.
- [N-U02-162] Unit selection on configurators appears only when the feature is on and the product has more than one available unit.

### DEPENDENCY

- [N-U02-163] Sales, purchase, stock, manufacturing and accounting lines each restrict their unit to the product's allowed units; timesheets and electronic invoicing rely on the common-root test.

### CONSTRAINT

- [N-U02-164] The conversion ratio of a unit cannot be zero, and a unit without a reference unit must have ratio one.
- [N-U02-165] A unit may be changed on a product only if no posted journal entry used another unit for it.

### RISK

- [N-U02-166] Changing a product's unit after use is handled differently by each document type: some replace units, some block, so the safe path is to archive the product and create a new one.
- [N-U02-167] The rounding precision is global, so changing it changes every conversion in the system at once.
- [N-U02-168] Because no common-root check is made, a wrongly configured conversion between unrelated units silently produces a number.

### UNKNOWN

- [N-U02-169] Whether any user-facing screen prevents selecting a unit from a different root than the product's base unit is not established by these functions.

## CAP-U02-05 Vendor price lines on the product

### WHAT

- [N-U02-180] Each product can carry vendor price lines holding the vendor, the vendor's own product name and code, a unit, a minimum quantity, a unit price, a currency, a discount percentage, a validity window, a delivery lead time in days, an optional variant restriction and a company.

### WHY

- [N-U02-181] Vendor price lines let purchasing and replenishment propose the right vendor, price and planned date automatically when buying.

### BUSINESS RULE

- [N-U02-182] A vendor line is eligible only if it is shared or belongs to the buying company (the order's company when an order is given), its vendor is active, it is not tied to a different variant, the date lies in its validity window with open ends allowed, the requested quantity converted to the line's unit reaches its minimum, and the vendor matches the requested partner or that partner's parent.
- [N-U02-183] When a unit is forced, as on purchase order lines, only lines whose unit equals the requested unit or the product's base unit qualify.
- [N-U02-184] Eligible lines are first ordered by priority, then larger minimum quantity, then lower price; the selected line is the one with the lowest discounted price in company currency among the lines of the first vendor in that order, with priority and age as tie-breaks.
- [N-U02-185] The discounted price is the line price converted to the product's base unit and reduced by the discount percentage.
- [N-U02-186] Special flows may prefer another sort key such as the minimum quantity, with discounted price as the tie-break, and may ask for any vendor regardless of quantity.
- [N-U02-187] A purchase order line uses the selected vendor line to set its price, converted into the order currency at the order date, its planned date equal to the order date plus the lead time, and its description including the vendor's own name and code.
- [N-U02-188] Replenishment and procurement use the selected vendor to create purchase orders and take the lead time into account when computing order dates.
- [N-U02-189] Subcontracting restricts selection to subcontractor vendors and purchase agreements restrict it to the lines belonging to the order's agreement.
- [N-U02-190] A vendor line given only a variant gets its product definition filled in; a line with a definition and no variant applies to all variants.
- [N-U02-191] The vendor's own product code and name drive the displayed name and search results when a partner is in context.
- [N-U02-192] A new vendor line defaults to a lead time of one day, the company currency (or the vendor's purchase currency on purchase), minimum quantity zero and the product's base unit.

### STATE

- [N-U02-200] A vendor price line has no status of its own; it applies only while the pricing date lies inside its validity window.

### OPTIONALITY

- [N-U02-193] Vendor lines can be shared across companies or restricted to one; each line has its own currency; the studied configuration holds none yet.

### DEPENDENCY

- [N-U02-194] Purchase orders, replenishment rules, vendor bills, service resale to vendors and manufacturing cost reports all call the same vendor selection.

### CONSTRAINT

- [N-U02-195] Vendor, unit, minimum quantity, currency and product definition are mandatory on each line, and removing the vendor or product removes its lines.

### RISK

- [N-U02-196] Lines of another company or of an inactive vendor are silently ignored, so a purchase can end up with price zero and no vendor if lines are mis-scoped.
- [N-U02-197] The price on a new line is not pre-filled from the product cost although a helper to do so exists, so prices must be entered.
- [N-U02-198] A line tied to one variant overrides generic lines for that variant only through ordering, not through an explicit precedence rule.

### UNKNOWN

- [N-U02-199] Whether the unused price-from-cost helper and the unusual default-variant helper on a vendor line are intentional is not established by the source alone.

## CAP-U02-06 Analytic accounting: plans, accounts, applicability, distribution and analytic lines

### WHAT

- [N-U02-210] Analytic accounting tracks cost and revenue by business dimension independently of the general ledger: a plan is a dimension such as project or department, accounts belong to a plan, plans can form a hierarchy, and amounts are recorded as analytic lines.
- [N-U02-211] Each top-level plan gets its own column on every analytic document and analytic line, created automatically when the plan is created or renamed; sub-plans get a read-only grouping field per depth instead, and the first project plan has a fixed column whose identity is held in a system parameter that must not change.
- [N-U02-212] An analytic distribution is a percentage split of a document line across one or more analytic accounts; a split key may combine one account per plan so that several plans share the same percentage.
- [N-U02-213] A distribution model prefills the distribution on documents from rules based on partner, partner category, product, product category, financial account prefix and company.

### WHY

- [N-U02-214] Plans give management several independent views of the same transaction, and distribution models avoid manual analytic coding on every line.

### BUSINESS RULE

- [N-U02-215] The applicability of a plan on a document is optional, mandatory or unavailable; the default is set per company and specific rules refine it by business domain (miscellaneous, invoice, vendor bill, sales order, purchase order, timesheet, expense, stock transfer), account prefix, product category and company; the best-scoring rule wins and a business-domain mismatch excludes a rule.
- [N-U02-216] A mandatory plan requires the distribution of the line to total exactly one hundred percent for that plan; this is checked when posting and flagged on the line beforehand.
- [N-U02-217] When distribution models apply, matching models are taken in order, a model is skipped if its plans were already served, and the merged distribution combines percentages across plans multiplicatively.
- [N-U02-218] When a journal item with a distribution is posted, one analytic line is created per account combination, with the amount equal to minus the item balance times the percentage, the last share of a plan taking the remainder, rounding errors redistributed and zero amounts skipped.
- [N-U02-219] An analytic line copies the date, description, partner, quantity, unit, product, financial account, reference, user, company and a category of customer invoice, vendor bill or other from its journal item.
- [N-U02-220] Editing the distribution on an analytic line splits it into several lines, and editing analytic lines updates the distribution of the source journal item.
- [N-U02-221] Distribution percentages are rounded to the analytic percentage precision, two decimals by default, so equality tests are reliable.
- [N-U02-222] An analytic account has a name, code, partner and company; balance, debit and credit are computed from its lines in the company currency for the selected companies and dates.
- [N-U02-223] Plans can be moved in the hierarchy and accounts moved between plans; existing analytic lines follow to the right column, and the move is blocked with an explanation when it would overwrite existing data.

### STATE

- [N-U02-224] Accounts are active or archived and plans have no state; analytic lines of a journal item exist from posting until the entry is reversed or reset.

### OPTIONALITY

- [N-U02-225] Analytic accounting is an optional switch; every permission on analytic objects is given only to the analytic accounting group, which in the studied configuration is not implied by any other group.
- [N-U02-226] Applicability can be tuned per plan and company, and distribution models are optional.

### DEPENDENCY

- [N-U02-234] Sales lines, purchase lines, expenses, requisitions and journal items inherit the distribution mechanism and look up distribution models with their product, partner, category and company; journal items turn the distribution into analytic lines at posting.

### CONSTRAINT

- [N-U02-227] An analytic line needs at least one account, the company of an analytic account cannot change when it already has lines of other companies, and a model shared across companies cannot use company-specific accounts.
- [N-U02-228] The project plan cannot get a parent, and the system parameter naming it must point to a top-level plan.
- [N-U02-229] An analytic line attached to a journal item must carry the same financial account as that item.

### RISK

- [N-U02-230] A mandatory plan blocks posting when the distribution is not complete, so changing applicability affects documents already in progress.
- [N-U02-231] Creating a plan changes database structure by adding columns; many plans mean many columns, and deleting a plan removes its column and the data in it.
- [N-U02-232] Optional plans may total less or more than one hundred percent, so analytic totals need not equal ledger totals.

### UNKNOWN

- [N-U02-233] Performance and reporting behaviour of the stored distribution format at large volumes is not established here.

## CAP-U02-07 Product documents, combos, tags, attribute exclusions and bulk maintenance helpers

### WHAT

- [N-U02-260] Files or links can be attached to a product or a variant as product documents, each stored as an attachment with an order and a company scope, so they can be shared with customers.
- [N-U02-261] Tags label products and variants; a tag name is unique and a tag can be marked visible or hidden to customers.
- [N-U02-262] A combo choice group lists ordinary products, each with an optional extra price, and a combo product offers one choice per group.
- [N-U02-263] Attribute exclusion rules state that a value is incompatible with other values of the same product or with values of another product that is offered with it; they are stored as pairs and completed in both directions.
- [N-U02-264] A bulk wizard adds an attribute value to every product already using that attribute, or resets the extra price of a value on every product using it, limited to products of the companies the user may access.
- [N-U02-265] A catalog helper lets a document add products from a catalog view, excluding combos and respecting company scope.

### WHY

- [N-U02-276] Documents, tags, combos and exclusions keep supporting master data next to the product so that files can be shared, items grouped, bundles offered and impossible option combinations prevented.

### BUSINESS RULE

- [N-U02-266] A file attached through the chat area of a product automatically becomes a product document.
- [N-U02-267] A link document must start with http, https or ftp, otherwise the user is warned.
- [N-U02-268] The base price of a choice group is the lowest price among its items, converted to the group's currency, and is used to prorate the price between groups; the group's currency is that of its company or of the main company.
- [N-U02-269] Creating, changing or removing an exclusion regenerates the variants of the product, which can archive or delete variants that became impossible.
- [N-U02-270] Combo items that reference variants removed by regeneration are removed too.
- [N-U02-271] The bulk wizard changes many products in one action and can create new variants where a value is added.

### STATE

- [N-U02-277] A product document is either active or archived.

### OPTIONALITY

- [N-U02-273] Documents, tags, combos, exclusions and the bulk wizard are always present in the product function and need no switch; the studied configuration holds none of them yet.

### DEPENDENCY

- (no statement)

### CONSTRAINT

- [N-U02-272] A tag name must be unique; combo choice groups need at least one product and no duplicates; items cannot be combos; combos and their items must share a compatible company.

### RISK

- [N-U02-274] Exclusion changes and the bulk wizard can restructure variants of many products at once without a preview of every affected variant.

### UNKNOWN

- [N-U02-275] Label printing for products and the web-shop uses of tags and documents are not studied here.

## CAP-U02-08 Roles, access rights, company rules and multi-company scoping

### WHAT

- [N-U02-280] Every internal user can read the product master, categories, attributes, price lists and their rules, vendor price lines, combos, tags, documents, units of measure and packagings; creating, changing and deleting them requires the product manager role.
- [N-U02-281] The product manager role is named Create, is implied by the system administration role and is granted to the system user and the administrator account.
- [N-U02-282] Partner managers can additionally read price lists, and internal users may use the label printing wizard freely.

### WHY

- [N-U02-296] Permissions and company rules separate those who maintain master data from those who only use it and keep legal entities apart.

### BUSINESS RULE

- [N-U02-283] Product definitions, product documents, price lists, price list rules, vendor price lines and combos are protected by company rules: a record is visible when it has no company or its company is among the user's allowed companies or their parents.
- [N-U02-284] Categories, attributes, units of measure, tags and attribute values carry no company rule and are shared by all companies.
- [N-U02-285] Variants have no dedicated company rule in these functions, so their company scoping relies on the product definition and on company consistency checks.
- [N-U02-286] Product cost is visible only to internal users, while price computation reads it with system rights.
- [N-U02-287] Analytic accounts, lines, plans, applicability rules and distribution models are accessible only to the analytic accounting group with full rights; accounts, applicability and models are visible when shared or in an allowed company, and lines only for allowed companies.
- [N-U02-288] Units of measure are readable by internal users and writable by system administrators and product managers.
- [N-U02-289] Marketing trackers (campaign, medium, source) can be read, created and changed by internal users but deleted only by system administrators, while stages and tags are read-only for internal users.
- [N-U02-290] Working calendars and their periods are readable by internal users and managed by system administrators; time off entries are readable and manageable by internal users for their own or company-wide entries according to rules, and company-wide time off is managed by administrators.
- [N-U02-291] Product, vendor line and pricelist data validate company consistency of linked records automatically, and a product restricted to a company cannot be used by documents of another company.

### STATE

- (no statement)

### OPTIONALITY

- [N-U02-293] Feature groups for variants, price lists and multiple units add no permissions; they only switch features on, and in the studied configuration all internal users hold the variants, price list and multiple-unit features.

### DEPENDENCY

- (no statement)

### CONSTRAINT

- [N-U02-292] The number of access rows and company rules declared in the source for these functions matches what is loaded in the studied database: product 38 rows and 6 rules, units 2 rows, analytic 5 rows and 4 rules, trackers 10 rows, calendars 8 rows and 5 rules.

### RISK

- [N-U02-294] Several shared master data objects have no company rule, so multi-company installations must rely on conventions and on the consistency checks of the documents that use them.

### UNKNOWN

- [N-U02-295] Whether variant visibility is filtered per company through the product definition could not be established from the declared rules and needs runtime confirmation.

## CAP-U02-09 Automated behaviour and configuration switches

### WHAT

- [N-U02-320] None of the studied functions defines scheduled jobs, automated actions or periodic cleanups; all automatic behaviour is triggered by events such as saving a record, creating a company or changing a setting.
- [N-U02-321] Feature switches in Settings control variants, multiple units of measure and packagings, price lists, analytic accounting, and a promotions and loyalty module option; further preferences set the weight unit and the volume unit.

### WHY

- [N-U02-331] Switches let a business keep the product and pricing foundations simple and turn advanced features on only when needed.

### BUSINESS RULE

- [N-U02-322] Enabling price lists creates or reactivates a default price list for each company, and disabling them archives every price list.
- [N-U02-323] Creating a company while price lists are enabled creates its default price list, and creating any company creates its default working calendar of forty hours per week.
- [N-U02-324] A change of company currency is applied before the default price list is created so that the list gets the right currency.
- [N-U02-325] System parameters tune behaviour: the variant generation limit, the weight and volume unit choices, the project plan of analytic accounting, the fallback price lists for partners, the propagation of procurement units and the similarity threshold used to match product names on electronic invoice import.
- [N-U02-326] Archiving a currency archives the price lists in that currency; enabling multiple currencies turns on price lists.

### STATE

- [N-U02-332] The price list feature is either on or off; turning it off archives all price lists and turning it on reactivates or recreates the default one per company.

### OPTIONALITY

- [N-U02-327] Every switch is optional; in the studied configuration variants, price lists and multiple units are on for all internal users, analytic accounting is off, and the weight and volume unit parameters are present.

### DEPENDENCY

- [N-U02-328] Other functions toggle these switches: timesheets enable multiple units, the variant matrix enables variants and enabling multiple currencies enables price lists.

### CONSTRAINT

- (no statement)

### RISK

- [N-U02-329] Because nothing runs on a schedule, stale data such as expired price list rules or vendor prices is never cleaned automatically and is simply ignored by date filters.

### UNKNOWN

- [N-U02-330] Whether other installed functions add jobs on product, price list or analytic objects was not exhaustively searched beyond these modules.

## CAP-U02-10 Marketing trackers and working calendars (light touch)

### WHAT

- [N-U02-340] Marketing trackers provide three tags, campaign, medium and source, that can be attached to sales orders and invoices to attribute revenue to marketing efforts.
- [N-U02-346] A working calendar describes weekly working periods, optionally in a two-week pattern or flexible, with a timezone and company-wide time off, and can compute working durations and plan hours or days forward or backward while skipping non-working time.

### WHY

- [N-U02-356] Trackers attribute revenue to marketing efforts, and working calendars allow time-aware planning for people and work centers.

### BUSINESS RULE

- [N-U02-341] When a document is created, tracker values come from visitor cookies set for about a month from the web address parameters of the visit; users who are sales representatives are excluded from this automatic defaulting.
- [N-U02-342] Tracker names are unique, a duplicate name gets a numeric suffix, mailing sources are named automatically from their content, and the Referral source and the base mediums cannot be deleted.
- [N-U02-343] The trackers of a sales order are copied to the invoice created from it, and deleting a tracker simply empties it on orders and invoices.
- [N-U02-344] A campaign shows its number of quotations and the revenue invoiced under it when sales is installed, counting only posted invoices, credit notes and receipts.
- [N-U02-345] A tracker can be found or created on the fly by name, matching without regard to case.
- [N-U02-347] Each company gets a default calendar of forty hours per week, created automatically with the company.
- [N-U02-348] In the studied configuration the lead times of sales, purchasing and inventory are plain calendar days: the customer lead time, the vendor lead time, the procurement rule delay, the security lead time and the days to purchase never consult a working calendar.
- [N-U02-349] Working calendars are consulted by manufacturing work centers for scheduling and load, and by time off, employee and project functions that are outside this unit.
- [N-U02-350] A time off entry belongs to a company calendar or to one resource, must end after it starts, and by default covers the current day in the calendar's timezone.

### STATE

- (no statement)

### OPTIONALITY

- [N-U02-352] Marketing trackers and working calendars need no switch; the studied configuration holds one standard calendar, one resource, seeded mediums and sources, and no time off.

### DEPENDENCY

- [N-U02-353] Sales orders and invoices inherit the tracker fields, and sales campaign statistics read them; manufacturing reads working calendars for work center planning.

### CONSTRAINT

- [N-U02-351] Working periods of a calendar must not overlap, and in two-week mode all periods must sit under the week sections.

### RISK

- [N-U02-354] Because stock, sales and purchase lead times ignore working calendars, planned dates can fall on non-working days; the promised dates assume calendar days.

### UNKNOWN

- [N-U02-355] How employee, time-off and project functions consume the working calendar beyond the planning helpers was not studied.
