# U15 — Manufacturing Accounting, Subcontracting and Repair — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source product: Odoo 19 Community. Unit U15, capabilities 01 to 10.
> This file states what manufacturing cost and accounting, subcontracting and repair functions must do and why, in plain business language, with no implementation names.

## Capability 01 — Manufacturing order cost computation and by-product cost allocation

### WHAT
- [N-U15-001] When a manufacturing order is completed, the system works out the unit cost of the finished product and of each by-product from the value of the components consumed, the cost of work-centre time and an optional extra unit cost entered on the order.

### WHY
- [N-U15-002] Finished stock must carry a defensible cost that includes materials and operations, so margins and period-end stock value reflect what was spent.

### BUSINESS RULE
- [N-U15-003] The material part of the cost is the sum of the values of the completed component movements, each valued by its own product costing method.
- [N-U15-004] The work-centre part is, for each work order, the time spent in hours multiplied by the work centre's hourly cost; a work order with no recorded time is costed at its planned duration and a cancelled work order adds nothing. A work centre has one hourly rate only; no per-unit or overhead-rate mechanism exists.
- [N-U15-005] An extra unit cost entered on the order is multiplied by the finished quantity and added to the total; it is not copied when the order is duplicated.
- [N-U15-006] For finished products costed by first-in first-out or by average, the unit cost is the total cost, less the percentage given to by-products (rounded to four decimals), divided by the finished quantity.
- [N-U15-007] For a finished product costed at standard, the finished goods are valued at the standard cost whatever was actually spent; actual-minus-standard is not absorbed into the product.
- [N-U15-008] A finished or by-product movement that belongs to an order is valued at its quantity times the computed unit cost; this value ranks after manual and vendor-bill values and before purchase-order, return and standard values in the receipt value order.
- [N-U15-009] Each by-product line on a bill of materials carries a cost-share percentage of the final production cost. A first-in first-out or average-cost by-product receives total cost times its share divided by its quantity; a share of zero receives nothing so the main product carries the full cost; a standard-cost by-product is valued at standard cost whatever its share. This resolves the earlier open question about the by-product allocation method: allocation is a configured percentage, not value-proportional.
- [N-U15-010] Work-order time can be costed on actual time entries (overlapping entries counted once, optionally only those ended before a given date) or on planned duration when the operation's cost mode is estimated and the work order is in progress or done; the mode is copied from the operation once, when the order is confirmed, and the hourly rate is stored on the work order when it is finished.
- [N-U15-011] A backorder created from an order inherits its extra unit cost.

### STATE
- [N-U15-012] Within completion, components are completed and valued first, then work-order durations are fixed, then the cost is computed, and only then are the finished goods completed and valued from it.

### OPTIONALITY
- [N-U15-013] Without the manufacturing accounting extension no finished-product cost is computed; the base manufacturing function leaves cost computation as an empty step. In the studied configuration the extension is installed automatically with manufacturing and stock valuation.

### DEPENDENCY
- [N-U15-014] The manufacturing order overview report shows the actual unit cost of a completed movement from its posted value, so it depends on this computation having run.

### CONSTRAINT
- [N-U15-015] The by-product cost shares of one order, and of one bill of materials per product variant, may not total more than one hundred percent and may not be negative.
- [N-U15-016] Only finished movements of the order's main product that are not completed or cancelled and have a positive quantity are priced; by-product movements must also be open and have a positive quantity.

### RISK
- [N-U15-017] A by-product left at zero cost share receives no cost under first-in first-out or average costing, so an unintended zero share overstates the main product's cost.

### UNKNOWN
- [N-U15-018] The restored configuration contains no manufacturing orders, work orders, work centres or bills of materials, so the computation has never been exercised there.
- [N-U15-019] The numerical result for orders with several finished movements, partial quantities and backorders, zero consumption or negative component stock is not established by static reading.

## Capability 02 — Production accounting postings, labour posting and manual work-in-progress entries

### WHAT
- [N-U15-020] A location counts as valued stock only if it belongs to a company and is an internal or in-transit location. The production location is therefore outside valued stock, so components consumed into production are outgoing valued movements.
- [N-U15-021] Finished and by-product goods moving from the production location into stock are incoming valued movements.

### WHY
- [N-U15-022] The stated purpose is that, when automated inventory valuation is active, the necessary accounting entries for manufacturing are created; in this version that additionally needs an account to be set on the production location.

### BUSINESS RULE
- [N-U15-023] A stock journal entry for a movement is a two-line entry: when the source location has a valuation account the entry debits stock valuation and credits that account, otherwise it debits the destination location's account and credits stock valuation. Consumption therefore debits the production-location account and credits stock valuation; finished goods do the reverse; the amount is the movement's stored value and the entry is posted immediately.
- [N-U15-024] The account on a production location is labelled Cost of Production and is documented as the expense account used to re-qualify products removed from stock to that location. It is not the company-level work-in-progress account, which is used only by the manual work-in-progress entry. This differs from the earlier description of an automatic move to a work-in-progress account.
- [N-U15-025] Labour is posted when an order is completed, only if the finished product is valued perpetually and its production location has an account; each work order is booked to its work centre's expense account, else the finished product's expense account, rounded in company currency, and skipped if the total is zero.
- [N-U15-026] The labour entry is dated the day of posting, uses the stock journal of the finished product, credits the expense accounts and debits the production-location account for the total, and is posted immediately.
- [N-U15-027] An accountant can post a manual work-in-progress entry from selected manufacturing orders, as an optional separate action that is not triggered automatically at any milestone.
- [N-U15-028] Selected orders count only if confirmed, in progress or to close; with none the wizard is a manual entry. The journal defaults to the default stock journal and the reference to the order names or Manual Entry.
- [N-U15-029] The proposed component value is the sum, over picked component lines dated up to the chosen date, of quantity times the lot cost or the current product cost; the proposed overhead is the work-centre cost of the orders' work orders up to the chosen date.
- [N-U15-030] The proposed entry credits component value to the default stock valuation account of the product category setting (not each product's own category), credits overhead to the company overhead account, and debits the sum to the company work-in-progress account.
- [N-U15-031] The proposed lines are recomputed when the date changes while orders are attached, and can be edited by the accountant; for a manual entry without orders the lines are kept as entered.
- [N-U15-032] Confirming the manual entry posts it and immediately creates and posts its reversal on a reversal date chosen by the user (default the next day, always after the posting date); the reversal is automatic and independent of when the order is completed. This replaces the earlier assumption that reversal follows order completion and answers the earlier open question that reversal was either manual or automatic.

### STATE
- [N-U15-033] Outgoing movements are valued just before completion so the first-in first-out stack is intact, and incoming movements right after completion; consumed components are valued at the product's current cost under standard and average costing, or by a first-in first-out run.

### OPTIONALITY
- [N-U15-034] A stock journal entry for a manufacturing movement is produced only if the product is storable, the movement is valued, the product is valued perpetually, the quantity is not zero and a valuation account exists on the source or destination location. This differs from the earlier description, which gated only on automated valuation and category accounts; this version also has no separate stock input or output accounts.
- [N-U15-035] Nothing in installation or the chart of accounts sets an account on the production location, so manufacturing postings stay inactive until a user sets one; in the restored configuration the production and inventory-adjustment locations have no account and the category production account is empty on every category.
- [N-U15-036] In the restored configuration the company has no work-in-progress account and no overhead account, no stock journal is set on the company (a stock journal exists), and valuation is periodic.

### DEPENDENCY
- [N-U15-037] A manual work-in-progress entry keeps a link to the orders it was based on, shown by buttons on the order and on the entry, and the links are kept when the entry is duplicated.
- [N-U15-038] The stock valuation report gains a Cost of Production section only when some production location has an account.

### CONSTRAINT
- [N-U15-039] Labour is posted only once per order: if any time entry is already linked to a journal line the order is skipped, and posted lines are linked back to the time entries.
- [N-U15-040] A line of the manual entry cannot be both debit and credit, total debit must equal total credit, and the reversal date must be later than the posting date.

### RISK
- [N-U15-041] The stock entry uses the company's stock journal; with no journal set, a perpetual posting has no journal and its failure mode was not observed.
- [N-U15-042] With entries on one production-location account, consumption debits it, finished goods credit it and labour debits it, so the account keeps labour and any actual-versus-standard difference as a residual; whether it nets as intended is not observed.
- [N-U15-043] The manual entry's supporting records grant access to the adviser group while the action is offered to the accountant group, so an accountant without the adviser group may be refused.

### UNKNOWN
- [N-U15-044] A production account setting exists on product categories and is documented as the counterpart for components and finished goods, but no code reading it was found; its intended use is unclear.
- [N-U15-045] No revaluation entry for components consumed before they were received (the older negative-inventory behaviour) was found in the studied code; later value changes come only from vendor bills, landed costs or manual values.
- [N-U15-046] The actual journal lines for a full perpetual order with a configured production-location account, and behaviour when the stock journal is missing, need a runtime test.

## Capability 03 — Work-centre cost, analytic and project cost tracking

### WHAT
- [N-U15-047] A work centre can carry an analytic distribution next to its hourly cost, and the analytic accounts it names are stored on the work centre.
- [N-U15-048] A printable work-in-progress report lists analytic lines with date, reference, product, quantity, unit and amount and a total.

### WHY
- [N-U15-049] The stated purpose is analytic accounting in manufacturing, with cost structure reporting.

### BUSINESS RULE
- [N-U15-050] Whenever a work order's duration is computed or set, its analytic cost lines are created or updated.
- [N-U15-051] Analytic lines for work orders are named after the work order, measured in hours, reference the order name and are categorised as manufacturing; component lines from the project bridge carry the same category.
- [N-U15-052] Cancelling or deleting a work order deletes both its work-centre and its project analytic lines.
- [N-U15-053] Renaming an order re-labels the reference and name of its component and work-order analytic lines.
- [N-U15-054] Stock movements have no analytic distribution of their own; where a distribution is supplied, a picked but unfinished movement gets an estimated line at quantity times standard price, a completed movement uses its stored value, outgoing amounts are negative, and lines are refreshed when the movement is picked and again when it completes.
- [N-U15-055] Component lines and work-order cost are also distributed over the order's project analytic distribution, and changing the project of an order that is not in draft regenerates these lines.
- [N-U15-056] Project profitability shows a Manufacturing Orders cost item equal to the sum of manufacturing-category analytic lines, converted to the project currency, and excludes them from the generic analytic domain.
- [N-U15-057] Analytic lines gain a manufacturing category and analytic plans gain a manufacturing business domain for applicability; no applicability rule exists in the restored configuration.
- [N-U15-058] Accounting read-only and billing groups get read-only access to bills of materials and their lines.

### STATE
- Not applicable: no distinct statement for this capability in this section.

### OPTIONALITY
- [N-U15-059] Work-centre analytic lines are produced only if the work centre has an analytic distribution, or if lines already exist so they can be updated or removed.

### DEPENDENCY
- [N-U15-060] Component movements of an order take the analytic distribution of the order's project, so the project bridge must be installed; it installs automatically with manufacturing accounting and the project integration.
- [N-U15-061] A project given in a procurement request is set on the order the rule creates.
- [N-U15-062] In the restored configuration there are no work centres; the manufacturing accounting function adds no groups, record rules or scheduled jobs of its own.

### CONSTRAINT
- [N-U15-063] If an analytic plan is mandatory for manufacturing and the order's project lacks it, confirming the order, or generating component analytic lines, is refused.

### RISK
- [N-U15-064] The analytic cost of a work order uses the work centre's current hourly rate, whereas the manufacturing cost uses the rate stored on the work order at completion, so the two can differ if the rate changes.

### UNKNOWN
- [N-U15-065] The analytic account gains order, bill-of-materials and work-centre relations with counters and buttons, but no studied code fills them, so they are expected to stay empty unless set elsewhere.
- [N-U15-066] Employee-level costs and allowed employees are not in the studied community modules; the amounts of analytic lines against journal cost under rate changes need a runtime test.

## Capability 04 — Cost roll-up from the bill of materials and kit valuation treatment

### WHAT
- [N-U15-067] A user can compute a product's price from its bill of materials; the result is written to the product's standard cost, and a product that has no bill but is a by-product of one gets its price from that bill when non-zero.

### WHY
- [N-U15-068] The stated purpose is to compute the price of a manufactured product from the products and operations of its bill of materials.

### BUSINESS RULE
- [N-U15-069] The list action recomputes all selected products together, and sub-assemblies found in the same batch are rolled up first.
- [N-U15-070] The price starts with the cost of each applicable operation (operation time in hours times work-centre hourly cost) plus each component's standard cost converted to the line unit times quantity.
- [N-U15-071] For the main product the total is reduced by the by-products' cost shares, divided by the bill quantity and converted to the product unit; for a by-product the price is total times its share divided by its quantity, zero when it has no share.
- [N-U15-072] A kit product has zero total value and zero average cost, and kits are left out of the products used for valuation and period-end closing, so a kit is not a valuation object and nothing is counted twice.
- [N-U15-073] The unit value of a kit sold or delivered is the sum, over its components, of component unit value times quantity per kit, divided by the kit quantity; this also applies to drop-shipped kits.
- [N-U15-074] Kit moves of the same bill are treated as related, and invoiced kit quantities are converted to component quantities so cost of goods is matched per component.

### STATE
- Not applicable: no distinct statement for this capability in this section.

### OPTIONALITY
- Not applicable: no distinct statement for this capability in this section.

### DEPENDENCY
- [N-U15-075] For a subcontracting bill the price adds the vendor price of the selected subcontractor, converted to company currency and to the product unit.

### CONSTRAINT
- [N-U15-076] The roll-up button is offered only to the manufacturing manager group, when the product has bills, and is hidden for first-in first-out products valued perpetually; bulk actions exist on product lists.

### RISK
- [N-U15-077] Cost of goods for a kit sale prefers the bill recorded on the sale line's movements over the current bill, so a bill changed between delivery and invoice may give a wrong price.

### UNKNOWN
- [N-U15-078] The restored configuration has no bills of materials and no stock movements, so neither roll-up nor kit valuation has been exercised.
- [N-U15-079] The effect of a rolled-up cost on already valued stock is not established; no revaluation entry is created by the roll-up itself.

## Capability 05 — Landed costs on manufacturing orders and subcontracting receipts

### WHAT
- [N-U15-080] Additional costs can be applied to manufacturing orders: a new apply-on option selects a set of orders, and changing the target away from orders clears the selection.

### WHY
- [N-U15-081] The stated purpose is to add extra costs on a manufacturing order and choose how they are split among its stock movements so that they enter stock valuation.

### BUSINESS RULE
- [N-U15-082] The movements receiving the cost are the finished movements of the selected orders, including by-products, but not by-products with zero cost share.
- [N-U15-083] Cost lines are split over the targeted movements by quantity, weight, volume, equally or by current cost, and any rounding remainder goes to the last adjustment line.
- [N-U15-084] On validation every adjusted movement is revalued, so for order output the landed cost is added to the production value; the added amount also shows in the movement's value description.
- [N-U15-085] For perpetual products the stock entry debits stock valuation and credits the cost line's account or the cost product's expense account, for the part of the cost applying to quantity still on hand; a negative cost reverses it.
- [N-U15-086] Landed cost records are fully accessible to the stock manager group only; the manufacturing extension adds no access rules.
- [N-U15-087] For subcontracting, a selected receipt movement is replaced by the movement that produced the goods, so the cost lands on the produced goods that carry the value.

### STATE
- [N-U15-088] Only draft landed costs can be validated, at least one target is required, and a validated landed cost cannot be cancelled; a negative landed cost reverses it.

### OPTIONALITY
- [N-U15-089] In the restored configuration there are no landed costs and the manufacturing landed-cost module adds one view and nothing else.

### DEPENDENCY
- [N-U15-090] The subcontracting extension also offers receipts containing completed subcontract movements and shows receipt references in the order picker; it installs automatically with landed costs and subcontracting.
- [N-U15-091] For order-targeted landed costs each journal item takes the analytic distribution of the order's project; this technical bridge installs automatically.

### CONSTRAINT
- [N-U15-092] The order picker offers only same-company orders that have an incoming valued finished movement, and the apply-on selector is shown to stock managers only.

### RISK
- [N-U15-093] Landed costs apply only to products costed by first-in first-out or average; on orders for standard-cost products the user is told landed costs cannot be applied, so such manufactured goods cannot absorb extra cost this way.

### UNKNOWN
- [N-U15-094] Possible double counting when the subcontracting fee is already part of the produced goods' value, and rounding, need a runtime scenario.

## Capability 06 — Subcontracting set-up: bill type, subcontractors, locations, routes and operation types

### WHAT
- [N-U15-095] A bill of materials can be of a subcontracting type; if the subcontracting function is removed such bills become ordinary and are archived.
- [N-U15-096] A subcontracting bill names one or more subcontractor partners, and the subcontractors field is shown and required only for that type.

### WHY
- [N-U15-097] Subcontracting locations must be internal so that stock held at a subcontractor is still managed accurately as company stock.

### BUSINESS RULE
- [N-U15-098] A subcontracting bill is found for a product, company and operation type whose subcontractor list contains the receiving partner or one of its parents; with no subcontractor given none is found.
- [N-U15-099] The components consumed by the subcontractor are those of the bill, used by an ordinary manufacturing order created at receipt, and are what is resupplied; a bill needs no components only if the subcontractor supplies everything.
- [N-U15-100] Each company has one internal location called Subcontracting, created on installation (and on update for companies lacking one) and used by default as the subcontractor location of every partner; locations below it must also be internal and the company's own location may not be altered; this matches the earlier reference finding that stock sent to subcontractors remains in company stock.
- [N-U15-101] A location is a subcontracting location if it is the company subcontracting location or below it; each partner can have its own company-dependent subcontractor location used as source and destination of goods sent to it.
- [N-U15-102] A partner counts as subcontractor only if it has a portal user and appears on a subcontracting bill; putaway checks then run with elevated rights.
- [N-U15-103] A vendor price line is marked subcontracted when its vendor is a subcontractor of a bill of the product, and vendor selection can be restricted to a bill's subcontractors.
- [N-U15-104] Two rules support resupply: stock to subcontracting location on the make-to-order route, and subcontracting location to production on the resupply-on-order route, so that components are delivered to the subcontractor when procured.
- [N-U15-105] A subcontract receipt is excluded from scheduler assignment, a pushed copy of it does not keep the subcontract flag, and resupply movements for a subcontract order take its subcontractor as partner.
- [N-U15-106] The bill overview adds a subcontracting line with the selected vendor price to the cost and estimates subcontract lead time from the larger of vendor and manufacturing lead time plus the longest component resupply delay.
- [N-U15-107] A reorder rule on a subcontracting location defaults its procurement partner to the single subcontractor of that location.

### STATE
- [N-U15-108] The global resupply route is active only while at least one active rule uses it.

### OPTIONALITY
- [N-U15-109] Each warehouse has a Resupply Subcontractors option, on by default, which drives the resupply route, rules and operation type; the subcontracting manufacturing type is created inactive, and the resupply type is active only when the option is on and the warehouse active.
- [N-U15-110] Installation switches resupply on for all warehouses once.
- [N-U15-111] In the restored configuration the module seeds only access rows and record rules for the portal group, views and one route; no groups, scheduled jobs or automations.

### DEPENDENCY
- [N-U15-112] Stock quantities can be filtered to subcontracting locations by manufacturing users, to see what is held at subcontractors.

### CONSTRAINT
- [N-U15-113] A subcontracting bill may not have operations or by-product lines; the earlier registers do not mention this restriction on combining it with routing and by-products.

### RISK
- [N-U15-114] Uninstalling the function archives subcontracting locations and operation types, clears links and tries to delete routes and types, silently skipping those still referenced.

### UNKNOWN
- [N-U15-115] The runtime behaviour of the make-to-order resupply movements, multi-step reception and push rules with subcontract receipts was not exercised.

## Capability 07 — Receipt-driven subcontract production, tracking, returns and the subcontractor portal

### WHAT
- [N-U15-116] Subcontractors reach their receipts through portal pages listing receipts (filter all, done, ready; sort by date or name), a detail page and an embedded form; a logged-in user is required and access errors give not found.

### WHY
- [N-U15-117] Receipt lines and subcontract orders are kept in lockstep on quantity and lot so that what the vendor delivers is exactly what was produced and consumed.

### BUSINESS RULE
- [N-U15-118] When a receipt line from a supplier location is confirmed and a subcontracting bill matches the receiving partner, the line becomes a subcontract receipt: its production group is cleared and its source becomes the partner's subcontractor location; it is reserved again; a receipt already linked to a production is not converted twice.
- [N-U15-119] A subcontract order is created per receipt line with the commercial partner of the receiving partner as subcontractor, the subcontractor location as source and destination, the receipt demand as quantity, the warehouse's subcontracting type, a start date equal to the receipt date less the bill's production delay, the receipt name as origin and a shared stock reference.
- [N-U15-120] For a backorder receipt the existing order is split and the backorder order is linked to the backorder receipt line; a non-positive quantity creates no order.
- [N-U15-121] Cancelling a subcontract receipt line cancels its linked orders that are not done or cancelled.
- [N-U15-122] Receipt quantity and lots stay in step with orders: an untracked receipt has one order following the line quantity, a tracked receipt has one order per lot, created by splitting, orphan orders are deleted but at least one stays; quantity changes on an order do not propagate to a subcontract receipt.
- [N-U15-123] Changing the date of an open subcontract receipt line shifts the start and finish of its open orders.
- [N-U15-124] Applying serial numbers on a subcontract order sets the first serial and quantity one on the order and creates receipt lines for the rest; splitting needs a lot or serial and is refused once goods are received.
- [N-U15-125] A return of a subcontract receipt goes back to the partner's subcontractor location when all returned lines are subcontract, and the return line is not itself flagged subcontract.
- [N-U15-126] Subcontract receipt lines skip reservation.
- [N-U15-127] The portal group has access rows for pickings, operation types, warehouses, locations, bills and lines, products, templates, units and barcode nomenclature (read), moves (read, write, create), orders (read, write), consumption warnings and the serial wizard (read, write, create), move lines (read, write, create, delete), and lots (read, create).
- [N-U15-128] Thirteen portal record rules limit a subcontractor to its own orders, bills, warnings, moves, move lines, receipts, operation types, locations, warehouses, lots and product templates by comparing with its commercial partner.

### STATE
- [N-U15-129] After confirmation the orders are created per company, confirmed, dated to the receipt, chained to the receipt line and reserved.
- [N-U15-130] When the receipt is completed its subcontract orders are marked done, skipping the consumption warning, and the order movement dates are set one second before the earliest receipt line for consistent traceability.

### OPTIONALITY
- [N-U15-131] In the restored configuration the twelve owned modules seed no groups, scheduled jobs or automations, and no subcontracting data exists.

### DEPENDENCY
- [N-U15-132] Movements out of a subcontract location count toward the purchase line's received quantity.
- [N-U15-133] The portal group can read analytic accounts and read and write analytic lines linked to bills of its partner, from the subcontracting valuation bridge.

### CONSTRAINT
- [N-U15-134] Subcontract orders never have work orders.
- [N-U15-135] A subcontract order cannot be unbuilt, and subcontract orders cannot be merged.
- [N-U15-136] A portal user cannot create a move in done state or set one to done, and may write only component lines, producing lot, producing quantity and product quantity on a subcontract order.

### RISK
- [N-U15-137] The analytic access rules compare analytic lines through a bill relation that no studied code fills, so they probably match nothing in practice.

### UNKNOWN
- [N-U15-138] The runtime sequence of order creation and completion with real resupply, lots, backorders and portal editing was not exercised, and the portal's browser components and page templates were not read.

## Capability 08 — Subcontracting valuation and its purchase and drop-shipping integration

### WHAT
- [N-U15-139] Because the subcontracting location is internal and belongs to the company, a resupply movement from stock to it is neither incoming nor outgoing in valuation, so sending components to a subcontractor creates no valuation event; source confirms the earlier reference rule that such shipments do not change inventory value.

### WHY
- [N-U15-140] The valuation bridge exists so that subcontracting can be managed with stock valuation.

### BUSINESS RULE
- [N-U15-141] Before computing the order cost, the order reads its last completed subcontract receipt; the extra cost per unit is the posted vendor bill value plus the purchase-order value for the unbilled part, divided by quantity, or the receipt's own unit price when neither has a value.
- [N-U15-142] With first-in first-out or average costing the subcontracting fee therefore enters the finished unit cost through the extra cost; with standard costing the finished value is the standard cost and the fee appears as a price difference.
- [N-U15-143] For the order's finished movement under non-standard costing, the stock journal amount is reduced by the extra cost times quantity, so the fee is booked only through the vendor bill.
- [N-U15-144] A vendor bill line for a storable perpetual product is posted to the stock valuation account instead of an expense account, including subcontracted goods.
- [N-U15-145] For standard-cost subcontracted products the price difference on the bill adds the components cost per unit: the value of the subcontract orders' consumed components divided by the quantity produced by completed orders.
- [N-U15-146] When a finished movement of a subcontract order is revalued from the receipt's bill or purchase value, its value is the unit price less the old extra cost plus the new extra cost, times quantity; a context flag prevents the drop-ship delegation from looping.
- [N-U15-147] Returning subcontracted goods counts as a purchase return.
- [N-U15-148] Monthly demand statistics include movements into subcontracting locations and exclude movements out of them.
- [N-U15-149] Subcontract lead time is the larger of the vendor lead time and the manufacturing lead time plus days to prepare, plus other delays; the bill overview does not use the buy route for subcontract bills and always adds days to purchase.
- [N-U15-150] Movements from the subcontractor location tree to a customer, from a vendor into the subcontractor location, and customer returns into that tree are treated as drop-shipped for valuation, and a supplier-to-subcontract picking is a drop-ship picking.
- [N-U15-151] For a drop-shipped subcontract receipt linked to a purchase line, bill value is read from the first finished movement of its order.
- [N-U15-152] A purchase order created by procurement into a subcontracting location defaults the vendor to the order's subcontractor and groups orders by destination address; an order delivering into a subcontract location takes the destination from the delivery address partner's subcontractor location and requires that address.

### STATE
- [N-U15-153] Components are valued as outgoing only when the subcontract order's raw movements are completed, which happens when the receipt completes and the order is marked done.
- [N-U15-154] The order's finished movement goes from production to the subcontracting location (incoming valued); the receipt movement that follows is internal to internal and is not valued itself.

### OPTIONALITY
- [N-U15-155] Price-difference lines on vendor bills are created only if the company's anglo-saxon flag is on; in the restored configuration it is off.
- [N-U15-156] Each company gets a drop-ship subcontractor operation type with its own sequence, a buy rule on the drop-ship route, and per warehouse a make-to-order pull rule from the subcontracting location to production; the type and route are active only while an active rule exists and follow the resupply option.
- [N-U15-157] In the restored configuration valuation is periodic at standard cost, no stock journal is set on the company and location accounts are empty, so subcontracting effects on stock journals are inactive and only move values and costing effects apply.

### DEPENDENCY
- [N-U15-158] For subcontract receipts the stock movements of a bill line include the finished movements of their orders, so valuation matching reaches the produced goods.
- [N-U15-159] A purchase order shows a Resupply button for the pickings of its subcontract orders and a receipt shows a Source PO button, both for stock users; a procurement exception while confirming a subcontract receipt notifies the product's responsible user and the order's user; archived operation types hide orders from the purchase order's manufacturing list.

### CONSTRAINT
- [N-U15-160] The drop-ship route is excluded from manual replenishment route choices.

### RISK
- [N-U15-161] If no warehouse is known the order uses the company's first warehouse subcontracting type; the code assigns a one-element tuple, which the data layer normally accepts for a link field, but this was not run.

### UNKNOWN
- [N-U15-162] Values of a complete purchase, resupply, receipt and bill cycle under each costing method with the subcontracting fee, price-difference account and returns were not executed.

## Capability 09 — Repair order lifecycle and its stock movements

### WHAT
- [N-U15-163] A repair order moves through New, Confirmed, Under Repair, Repaired and Cancelled; the status cannot be edited directly and changes through buttons: Confirm Repair, Start Repair, End Repair, Check availability, Unreserve, Create Quotation, Cancel Repair and Set to Draft.

### WHY
- [N-U15-164] The function exists to repair damaged products, with parts added or removed, stock impact, warranty and a quotation.

### BUSINESS RULE
- [N-U15-165] A new repair takes its reference from its operation type's sequence and gets a stock reference record linked to it.
- [N-U15-166] Confirming is refused if a part line has negative demand; a repair without a product, or for a non-storable product, is confirmed without stock checks; otherwise the stock on hand at the product's source location, owned by the customer or unowned, must cover the quantity, or a dialog offers to proceed.
- [N-U15-167] Completing a repair cancels part lines with zero quantity, marks all parts picked if none is, requires a lot or serial for a tracked product, creates a picked movement for the product to repair (owned by the customer only if enough customer-owned stock exists) from its source to its destination location with the parts' lines recorded as consumed, completes all movements without backorder and sets the order to Repaired.
- [N-U15-168] When the repair came from a sale line of a service product (no policy module, or prepaid on order), completion sets that line's delivered quantity to its ordered quantity.
- [N-U15-169] Repair is added as an operation type code; each warehouse's repair type has defaults: component source the warehouse stock, added parts to the production location, removed parts to an inventory-loss location, recycled parts to stock, and the product source and destination the stock.
- [N-U15-170] Part lines are of type Add (component source to production), Remove (production to the removed-parts destination) or Recycle (production to the recycle destination), and only Add lines count as consuming.
- [N-U15-171] Repair movements are not auto-assigned; reservation is done with the repair's Check availability, and they are never split when a repair is completed with partly done parts.
- [N-U15-172] Parts status is Not Available when forecast availability is below demand, otherwise Available or an expected date flagged late if after the schedule date; remove and recycle lines are always available.
- [N-U15-173] Changing the scheduled date updates the dates of open movements; changing the operation type of an open repair renames it from the new sequence and re-reserves its parts; changing a location re-derives the part-movement locations.
- [N-U15-174] Stock users have full access to repair orders and tags and the insufficient-quantity dialog; a multi-company rule limits repairs to the user's allowed companies; the Repairs menu is for stock users and reporting and configuration for stock managers.

### STATE
- [N-U15-175] Confirmation, for new repairs only, checks company, applies the repair procurement method, confirms the part movements, triggers the scheduler and sets Confirmed.
- [N-U15-176] Starting a repair confirms it first if needed and sets Under Repair.
- [N-U15-177] Ending a repair requires the Under Repair state and then completes the repair.
- [N-U15-178] A completed repair cannot be cancelled; cancelling sets the source sale line quantity to zero, cancels part movements and sets Cancelled; a cancelled repair can be reset to New with its sale line quantities restored; deleting a repair first cancels it.

### OPTIONALITY
- Not applicable: no distinct statement for this capability in this section.

### DEPENDENCY
- [N-U15-179] Traceability shows repair orders as document references and links parts to repaired products; removed or recycled parts returning to internal locations count in returned serial-number product counts.

### CONSTRAINT
- [N-U15-180] Creating a warehouse's repair type fails if no inventory-loss location exists or no production location exists; installation creates repair types and sequences for warehouses lacking one, each warehouse gets a make-to-order rule from stock to production for repairs, and in the restored configuration the repair type, rule and sequence exist and there are no repair orders.
- [N-U15-181] Creating a lot from a repair is refused unless the operation type allows new lots or serials; the lot defaults to the single lot of the source return transfer; generating a serial uses the product's lot sequence and errors if none is possible.
- [N-U15-182] Changing a product's unit is refused if repairs used another unit, and the part catalog lists goods only.

### RISK
- [N-U15-183] A repair can be confirmed despite insufficient stock after the warning dialog is accepted.

### UNKNOWN
- [N-U15-184] Whether partial-quantity handling at the end of a repair has any effect beyond the confirmation prompt is unclear.
- [N-U15-185] Runtime results of reservation with owner stock, tracked lots on removed parts, and the repair report layout were not exercised; the quotation report template was not read.

## Capability 10 — Repair links to sales, kits, manufacturing, purchasing and accounting

### WHAT
- [N-U15-186] A service product can be set to create a repair order when sold; confirming a sale order creates one confirmed repair per such line (one per line, not one per unit) with the customer, sale order, line and the warehouse's repair type, and a cancelled bound repair is reset and reconfirmed when quantity returns above zero.

### WHY
- [N-U15-187] The module lists warranty, a repair quotation report and stock impact among the topics it covers.

### BUSINESS RULE
- [N-U15-188] Cancelling the sale order, or setting a line quantity to zero, cancels its repairs that are not completed; a quantity going from non-positive to positive creates a repair.
- [N-U15-189] Sale lines whose movements belong to a repair do not launch the delivery rule; parts are handled by the repair order.
- [N-U15-190] The delivered quantity of a line with exactly one completed repair movement is that movement's quantity.
- [N-U15-191] Adding a part to a repair linked to a sale order creates a sale line for it; changing its quantity or type updates or cleans the line, and cancelling or deleting the part sets the line quantity to zero.
- [N-U15-192] A part's sale line takes the demand quantity (the done quantity once repaired), the delivered quantity if the movement is done, and a price of zero when the repair is under warranty; clearing the warranty recomputes the prices.
- [N-U15-193] An invoice line is not eligible for stock accounting if its Add repair movement already carries its own stock journal entry, which prevents a double posting; cost-of-goods lines are otherwise created only for eligible perpetual lines.
- [N-U15-194] An Add part is an outgoing valued movement at product cost or first-in first-out; a Remove part goes to an inventory-loss location and is not valued; a Recycle part goes into stock as an incoming movement with no bill or order origin, so it is valued at product cost; the repaired product moves stock to stock and changes no value; a stock journal entry arises only if the product is perpetual and the production location has an account.
- [N-U15-195] On create or write of a repair, parts whose product has a kit bill are replaced by component lines (service components skipped) that keep the line type, price and locations, and the generated movements keep the repair link.
- [N-U15-196] A return transfer can open a repair for its goods; the repair's source transfer must be a return containing the product, and customer, lot and quantity default from it.

### STATE
- Not applicable: no distinct statement for this capability in this section.

### OPTIONALITY
- [N-U15-197] In the restored configuration the purchasing link is installed, the point-of-sale link and the DIN 5008 layout are not, and there are no repair orders; the manufacturing link seeds only two views.

### DEPENDENCY
- [N-U15-198] Manufacturing orders show a Repairs button and repair orders a Manufacturing button through shared stock references, and the part catalog offers a filter for the bill parts of the repaired product.
- [N-U15-199] The subcontracting-repair bridge declares its dependencies only; it adds no behaviour, data or screens.
- [N-U15-200] A repair shows the purchase orders generated for its parts, and parts on make-to-order follow the repair type's procurement method, so they can trigger purchase or manufacture.
- [N-U15-201] A sale order shows a Repairs button for stock users, and the forecast report counts a part bound to both a repair and a sale line once.

### CONSTRAINT
- [N-U15-202] Create Quotation is refused when the repair already has a sale order or has no customer.

### RISK
- [N-U15-203] Sale lines linked to repair movements are reported as having no valued movements, so margin cost falls back to generic logic rather than the repair-movement value.
- [N-U15-204] Every change to a repair re-runs the kit-explode scan of its parts whatever field changed; its performance and repeat behaviour were not tested.

### UNKNOWN
- [N-U15-205] Invoicing of repair parts together with the service (proof of the cost-of-goods exclusion), warranty flows and the quotation report need runtime scenarios.
