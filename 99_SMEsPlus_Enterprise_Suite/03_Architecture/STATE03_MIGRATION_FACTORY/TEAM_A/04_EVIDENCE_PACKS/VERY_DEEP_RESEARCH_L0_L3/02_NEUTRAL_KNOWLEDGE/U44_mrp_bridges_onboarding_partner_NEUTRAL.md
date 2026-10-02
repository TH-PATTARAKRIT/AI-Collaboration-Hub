# U44 mrp bridges, onboarding, partner autocomplete, partnership — neutral knowledge

> Source: Odoo 19 Community. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Date: 2026-10-02. Plain business language; behaviour is from source reading, not runtime proof.

Scope: twelve modules around production bridges, onboarding panels, outside-service contact suggestions and membership levels. Statements marked inference are interpretations of design intent, not stated in source.

## CAP-U44-01 Landed costs on production orders and subcontract receipts

### WHAT
- [N-U44-001] Extra costs such as freight or handling can be spread over finished goods that were made in own production. The user picks one or more production orders as the target of the extra cost. A second small extension lets the same function work for goods received from a subcontractor.
- [N-U44-002] For goods received from a subcontractor, extra cost is redirected to the production side of the receipt instead of the receipt movement itself.

### WHY
- [N-U44-003] Finished goods should carry the real cost of getting them made, so freight, handling or similar charges are spread over them (inference from the design).

### BUSINESS RULE
- [N-U44-004] Changing the kind of target clears any production orders already chosen.
- [N-U44-005] When production orders are the target, the cost is spread over the finished-product movements of those orders.
- [N-U44-006] By-product movements that carry no cost share are left out of the allocation. By-products that do carry a share stay in.
- [N-U44-007] A cost document with no selected target cannot be confirmed; the user gets an error naming the missing target kind.
- [N-U44-008] Any subcontract receipt movement chosen as a target is replaced by the movements that fed it; other movements are kept.
- [N-U44-009] The resulting list of target movements has no duplicates and keeps its order.

### STATE
- [N-U44-010] The cost document is first a draft and becomes done once confirmed; only drafts can be confirmed. The extension adds no state of its own.

### OPTIONALITY
- [N-U44-011] Both extensions switch on automatically when their parent functions are present; no user setting is needed.

### DEPENDENCY
- [N-U44-012] Depends on the core extra-cost function, on production, and for the second extension on subcontracting.

### CONSTRAINT
- [N-U44-013] Only warehouse managers can see or set the production-order selection.
- [N-U44-014] Core allocation only accepts products that are valued by first-in-first-out or by average cost, and refuses the document otherwise. The restored configuration values products at standard cost, so production-order extra costs would be refused for current products (not exercised at runtime).

### RISK
- No statement in this pass.

### UNKNOWN
- No statement in this pass.

## CAP-U44-02 Subcontracting valuation and portal analytic access

### WHAT
- [N-U44-015] Adds subcontracting cost to the valuation of goods made by a subcontractor, and gives subcontractors who use the portal a narrow view of related analytic data.

### WHY
- [N-U44-016] The subcontracting fee is a cost of the goods and should be visible in their valuation (inference).

### BUSINESS RULE
- [N-U44-017] The computed cost of a subcontracted bill of materials adds the price quoted by the matching subcontractor, converted into the company currency and the product unit.
- [N-U44-018] When a subcontracted order is closed, an extra cost per unit is set from billed amounts plus not yet billed order amounts, or else from the receipt price.
- [N-U44-019] For products not valued at standard cost, the value posted for the finished goods excludes the subcontracting service amount. Products at standard cost are never adjusted, so the current configuration does not use this rule (not exercised at runtime).

### STATE
- No statement in this pass.

### OPTIONALITY
- [N-U44-020] Switches on automatically when subcontracting and production accounting are installed.

### DEPENDENCY
- [N-U44-021] Depends on subcontracting and on production accounting.

### CONSTRAINT
- [N-U44-022] Portal users get read access to analytic accounts and read and change access to analytic lines, limited by rule to records tied to the bills of materials of their own company. The restored configuration holds exactly two access entries and two rules for this.

### RISK
- No statement in this pass.

### UNKNOWN
- [N-U44-023] Whether the list of bills of materials on an analytic account is ever filled is not shown by the files read. If it stays empty, the portal rules would match nothing.

## CAP-U44-03 Purchase and subcontracting bridge (resupply, lead time, demand, report)

### WHAT
- [N-U44-024] Links purchase orders with the subcontracting production that they trigger. A purchase order shows its resupply transfers, a transfer shows its source orders, and the bridge adjusts lead times, demand and reports for subcontracted products.

### WHY
- [N-U44-025] Buyers and planners need one picture of the purchase order and the subcontracting production behind it (inference).

### BUSINESS RULE
- [N-U44-026] Production orders whose operation type is archived are left out of the order's resupply list unless explicitly requested.
- [N-U44-027] When a shortage is raised on a component of subcontracted production, the product's responsible person and the buyer of the originating order are both notified.
- [N-U44-028] The planning delay for a subcontracted product is the longer of the vendor lead time and the own manufacturing lead time plus the days needed to prepare, and the purchase order date is moved accordingly.
- [N-U44-029] Monthly demand counts movements into subcontracting locations, so supplying components to subcontractors counts as demand.
- [N-U44-030] A return of a subcontract receipt is treated as a purchase return.
- [N-U44-031] The value of the finished goods is recomputed from the receipt price, removing the earlier extra cost and adding the extra cost derived from bills and quotations.
- [N-U44-032] For standard-cost products, price differences on vendor bills include the component cost of the subcontracted production per unit, and bills also match the finished movements of that production (not exercised at runtime).
- [N-U44-033] In the bill of materials overview, a subcontract bill is never shown as a plain purchase route, and its resupply always adds the company's days to purchase and is labelled as estimated.

### STATE
- No statement in this pass.

### OPTIONALITY
- [N-U44-034] Switches on automatically when subcontracting and the purchase-production bridge are installed; demo data exists but is not loaded.

### DEPENDENCY
- [N-U44-035] Depends on subcontracting and the purchase-production bridge.

### CONSTRAINT
- No statement in this pass.

### RISK
- No statement in this pass.

### UNKNOWN
- No statement in this pass.

## CAP-U44-04 Dropship subcontracting

### WHAT
- [N-U44-036] Lets a vendor deliver components directly to a subcontractor. The bridge creates a company-wide operation type for this, prepares purchase rules and decides how such flows are classified.

### WHY
- [N-U44-037] Allows components to ship from a vendor straight to the subcontractor without passing the own warehouse (inference).

### BUSINESS RULE
- [N-U44-038] On installation every warehouse is set to supply components to subcontractors. This is applied once and not repeated on upgrade.
- [N-U44-039] Each warehouse gets a pull rule on the direct-delivery route, active only while the warehouse supplies subcontractors.
- [N-U44-040] The shared route and the company operation type are archived when no active rule is left, and restored when one returns.
- [N-U44-041] The direct-delivery route cannot be picked in the manual replenishment dialog.
- [N-U44-042] Flows between vendors, subcontractors and customers are classed as direct deliveries, and returns of them as purchase returns.
- [N-U44-043] For a direct subcontract receipt tied to a purchase line, the account value comes from the finished production movement instead of the receipt (not exercised at runtime).
- [N-U44-044] The purchase order for components bound for a subcontractor names that subcontractor as delivery partner and is never merged with another subcontractor's order.
- [N-U44-045] A purchase order delivering to a subcontracting location takes its destination from the subcontractor, fills the delivery address when only one subcontractor exists, and shows a warning when the operation type is chosen.
- [N-U44-046] A reorder rule on a subcontracting location with exactly one subcontractor passes that subcontractor on as partner.

### STATE
- No statement in this pass.

### OPTIONALITY
- [N-U44-047] Switches on automatically when subcontracting and direct delivery are both present.

### DEPENDENCY
- [N-U44-048] Depends on subcontracting and direct delivery.

### CONSTRAINT
- No statement in this pass.

### RISK
- [N-U44-049] When creating the production order for a direct delivery, the fallback operation type is assigned in a form that may be a one-element tuple instead of a single value; whether the platform accepts it was not tested.

### UNKNOWN
- No statement in this pass.

## CAP-U44-05 Expiry confirmation and repair bridges

### WHAT
- [N-U44-050] Before a production order is closed, the system checks whether any consumed component lot is flagged as expired or near expiry and, if so, asks for confirmation.
- [N-U44-051] Connects repair orders with production orders: each shows a count and a link to the other.
- [N-U44-052] The subcontracting-repair bridge contains only dependencies on subcontracting and repair and carries no behaviour of its own in this release.

### WHY
- [N-U44-053] Prevents consuming expired material without a conscious decision, and avoids kits in repair parts (inference).

### BUSINESS RULE
- [N-U44-054] Closing is interrupted by a confirmation dialog whenever at least one consumed lot carries an expiry alert.
- [N-U44-055] Accepting the dialog closes the order without asking again; declining leaves the order unchanged.
- [N-U44-056] The dialog names the lot when there is one and lists the lots when there are several.
- [N-U44-057] Whenever a repair order is created or changed, any part that is a kit product is replaced by its components, with quantities scaled; service components are skipped.
- [N-U44-058] When adding parts from the catalogue, a filter limited to the repaired product's bill of materials is switched on if one exists.

### STATE
- No statement in this pass.

### OPTIONALITY
- [N-U44-059] Each bridge switches on automatically when its two parent functions are present.

### DEPENDENCY
- [N-U44-060] Expiry depends on production and product expiry; repair on repair and production; subcontracting-repair on subcontracting and repair.

### CONSTRAINT
- No statement in this pass.

### RISK
- [N-U44-061] Each component line takes the kit line's unit price unchanged, so a kit price may be repeated on every component.

### UNKNOWN
- [N-U44-062] The dialog contains a branch for work orders, but nothing in the files read opens it from a work order; a module not read might.

## CAP-U44-06 BoM Overview report

### WHAT
- [N-U44-063] The bill of materials overview shows, for a product and quantity, the component tree with quantities, availability, lead time, cost and by-product shares, on screen and as a printable document.

### WHY
- [N-U44-064] Planners need cost, lead time and availability of a product in one view before committing to production (inference).

### BUSINESS RULE
- [N-U44-065] The producible quantity is the smallest, over stocked components, of free stock divided by the quantity needed per unit, rounded down; the top line reads as ready to produce for that quantity.
- [N-U44-066] Component cost is always the standard price times the line quantity; operation cost is added to give the bill cost, whatever costing method the product uses.
- [N-U44-067] With by-products the bill cost is multiplied by the main product share, and each by-product line gets its own percentage of the total.
- [N-U44-068] Route lead time is manufacturing lead time plus rule delays plus the days to prepare; the separate manufacture delay leaves out the days to prepare.

### STATE
- [N-U44-069] Availability is shown in one of four states: available, expected, estimated or unavailable.

### OPTIONALITY
- No statement in this pass.

### DEPENDENCY
- [N-U44-070] Two special-rule hooks are empty in core and filled by the subcontracting module, which this pass did not re-read.
- [N-U44-071] The bill of materials itself reuses this report to derive the days to prepare, so the report logic also drives planning.
- [N-U44-072] Part of core production; the subcontracting modules add their own special cases.

### CONSTRAINT
- No statement in this pass.

### RISK
- [N-U44-073] Operation cost is rounded in the user's company currency rather than the bill's company currency; with one currency this has no effect.
- [N-U44-074] When the same component appears on two lines, the merged per-bill quantity appears to count the second quantity twice (not tested).

### UNKNOWN
- No statement in this pass.

## CAP-U44-07 MO Overview report and printed production documents

### WHAT
- [N-U44-075] The production order overview and the printed documents for production: order sheet, labels in two formats, work order and overview.

### WHY
- [N-U44-076] Shop-floor staff and planners compare expected with real cost and status of an order and need paper output (inference).

### BUSINESS RULE
- [N-U44-077] Three cost totals are kept per order: expected from the order, expected from the bill and real, where real counts only picked quantities.
- [N-U44-078] Operation cost equals duration in hours times the hourly cost of the work order, or of the work centre when the work order has none.
- [N-U44-079] A figure is flagged as bad when above expectation and as good when below; equal or unknown values get no flag.
- [N-U44-080] Shortfalls with no covering document appear as a To Order line, and stock in motion toward the order appears as In Transit.
- [N-U44-081] A receipt dated after the planned start of the order is flagged as late.
- [N-U44-082] A per-product cost breakdown exists only for finished orders that have by-products.
- [N-U44-083] Resupply by manufacturing finds the bill of materials and uses its manufacturing lead time and delays.
- [N-U44-084] The label sheet has twelve rows and four columns; it prints one label per unit for countable products and one per line otherwise. A comment still refers to unit categories, which no longer exist.

### STATE
- [N-U44-085] For draft or confirmed orders the displayed state becomes Not Ready, a ready quantity, or Ready, based on reserved and free component quantities.

### OPTIONALITY
- No statement in this pass.

### DEPENDENCY
- [N-U44-086] Replenishment origins and extra sources are hooks: core only recognises production origins and no extra sources.
- [N-U44-087] Part of core production; other modules extend the origin and extra-source hooks.

### CONSTRAINT
- [N-U44-088] The order sheet lists operations only when the order has work orders and the viewer belongs to the routing group.

### RISK
- No statement in this pass.

### UNKNOWN
- No statement in this pass.

## CAP-U44-08 Onboarding steps and panels

### WHAT
- No statement in this pass.

### WHY
- [N-U44-089] Guides a new administrator through setup tasks and shows what is still open (inference).

### BUSINESS RULE
- [N-U44-090] Completing a step by its identifier reports not found, just done or was done; an unknown identifier raises no error.
- [N-U44-091] Switching a step or an onboarding between per-company and shared deletes the progress, so completed steps become not done again.
- [N-U44-092] Accounting steps are completed by their own rules: the company-data step only if a street is filled in, the layout step only if a report layout is set, and the sales-tax step as soon as its save action runs.
- [N-U44-093] Steps are per company by default, and progress is created for the active company, or for no company when shared.
- [N-U44-094] Current progress is the record with no company or with the active company; if none exists the onboarding reads as not done and open.
- [N-U44-095] The accounting side reads onboarding data with elevated rights, so ordinary users still see their panel and complete steps through it.

### STATE
- [N-U44-096] A step moves from not done to just done when completed, then to done once the panel is next shown, so the just-done marker appears once. A step already just done or done is untouched.
- [N-U44-097] The whole onboarding is done when every step is just done or done, otherwise not done; a closed panel reports closed.
- [N-U44-098] Closing the panel only sets a flag on the progress record, and reopening flips it back.

### OPTIONALITY
- [N-U44-099] Each panel can be closed by the user; an onboarding with no per-company step is shared by all companies.

### DEPENDENCY
- [N-U44-100] Accounting creates progress only for the accounting dashboard onboarding when a chart of accounts is loaded; the restored configuration holds one onboarding with five steps and one not-done progress.
- [N-U44-101] Accounting is the only consumer read in this pass.

### CONSTRAINT
- [N-U44-102] A step cannot be attached to an onboarding unless it names an opening action.
- [N-U44-103] There is at most one progress record per onboarding and company, and the short route name of an onboarding must be unique.
- [N-U44-104] Direct access to all four onboarding data kinds is blocked for ordinary users; only system administrators have full access. The restored configuration holds the same twelve access entries.

### RISK
- No statement in this pass.

### UNKNOWN
- [N-U44-105] A comment says the route name defines a web path, but no web handler exists in the module here. The sales-journal dashboard looks for an onboarding that the restored configuration does not contain.

## CAP-U44-09 Partner autocomplete and enrichment (outbound data)

### WHAT
- [N-U44-106] While a user types a company name or tax number on a contact or company form, the system offers suggestions from an outside service and can fill in company details once one is chosen.

### WHY
- [N-U44-107] Saves typing and improves data quality when creating contacts and companies (inference).

### BUSINESS RULE
- [N-U44-108] Failures are reported as insufficient credit, a transport message, or no token; unable-to-enrich is stated as consuming no credit.
- [N-U44-109] Returned country, state, industry and language values are matched to local records by code and then by name; city matching needs an optional address module that is not installed.
- [N-U44-110] Automatic company enrichment runs once, only when a system user creates a company, and never for tests or demo loading; the web client tells administrators whether it is still due.
- [N-U44-111] Enrichment fills only empty company fields, but always sets the logo, so an existing logo is overwritten.
- [N-U44-112] After enrichment a note with contact details, logo and activity tags is left on the contact, and tags are created when no tag of the same name exists.

### STATE
- No statement in this pass.

### OPTIONALITY
- [N-U44-113] Returned tax numbers are validated locally only when the tax-number validation module is installed; it is not installed in the restored configuration.
- [N-U44-114] The module installs automatically; with no account token or no credit, suggestions simply fail with a message. Tests and demo loading never call out.

### DEPENDENCY
- [N-U44-115] Depends on the outside-service mail bridge, which depends on the outside-service framework.

### CONSTRAINT
- [N-U44-116] Without an account token the call is refused locally and reported as no account token.

### RISK
- [N-U44-117] Queries go to a fixed vendor-hosted service. The address can be replaced by a system setting, which is absent in the restored configuration.
- [N-U44-118] Every request carries the database identifier, application version, user language, account token, and the active company's country and postal code.
- [N-U44-119] Calls are outbound secure web requests with a timeout of fifteen seconds in general and five seconds for company enrichment; nothing is sent during automated tests.
- [N-U44-120] The first use creates an account with the vendor service if none exists, and opening general settings asks the vendor for the credit balance. The restored configuration holds no account yet.
- [N-U44-121] Typed text of more than two characters is sent as a name or tax number search together with a country; a query extending an earlier empty result is not sent again.
- [N-U44-122] If the vendor service fails or finds nothing for a tax number, the number is sent to the public European tax-number checking service as a second outside destination.
- [N-U44-123] Choosing a suggestion triggers enrichment by company registry number, by Indian GST number or by web domain.
- [N-U44-124] Company enrichment sends only a web domain, taken from the company e-mail unless it is a free mail provider, otherwise from the company website.

### UNKNOWN
- [N-U44-125] A worldwide choice sends no country, while a missing country value falls back to the company country; how the vendor treats a missing country was not verified.

## CAP-U44-10 Partnership grades and price lists

### WHAT
- [N-U44-126] Members are graded into levels such as Gold, Silver and Bronze. A level may carry a default price list, and selling a membership product sets the customer's level.

### WHY
- [N-U44-127] Lets a business run a membership or partner programme with price lists tied to levels (inference).

### BUSINESS RULE
- [N-U44-128] When a contact is given a level that has a default price list, the contact's own price list is forced to it.
- [N-U44-129] An order's level is the level of its first membership line.
- [N-U44-130] Confirming an order sets the level on the commercial contact of the customer, with no dates or expiry, so a later lower-level order replaces a higher level.

### STATE
- [N-U44-131] A level is only set or replaced; nothing in the module removes it on cancellation, renewal, expiry or refund, and changes are tracked in the contact history.

### OPTIONALITY
- [N-U44-132] The company can rename the Members label; changing it in settings renames the related menu entry for everyone as soon as the field is edited.
- [N-U44-133] Not installed automatically; it is installed in the restored configuration.

### DEPENDENCY
- [N-U44-134] Depends on sales, customer relationship management and sale-related product fields.

### CONSTRAINT
- [N-U44-135] If the same change also gives a different price list, the change is refused with an error.
- [N-U44-136] An order cannot hold membership lines of two different levels. The check fires when lines change, not at confirmation, although the message speaks of confirming.
- [N-U44-137] Ordinary users read levels, system administrators and sales managers have full rights, and salespeople read, change and create but cannot delete. The restored configuration holds the same four entries and three seeded levels with no graded contacts.

### RISK
- [N-U44-138] Removing or changing a level later does not restore the earlier price list.

### UNKNOWN
- No statement in this pass.

