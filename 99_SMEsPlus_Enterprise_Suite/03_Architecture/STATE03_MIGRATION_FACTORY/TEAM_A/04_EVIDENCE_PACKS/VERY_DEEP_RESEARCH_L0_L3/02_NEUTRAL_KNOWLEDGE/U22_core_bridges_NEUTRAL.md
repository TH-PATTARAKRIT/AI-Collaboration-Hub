# U22 Core Bridges - Neutral Knowledge (Odoo 19 Community, clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source revision 19.0.post20260921. Scope: bridging features between sales, purchasing, inventory and accounting: customer-linked purchasing, promotions and loyalty, free shipping rewards, margin reporting, project-linked stock re-invoicing, delivery batching and pickup points, variant grid entry, electronic order and invoice exchange, print-on-demand fulfilment, postal dispatch, and small posting-time bridges.

## CAP-U22-01 Customer-demand-linked purchasing

### WHAT
- [N-U22-001] When goods or services that were sold are bought from a vendor, the vendor purchase document stays linked to the customer order that caused it, and either document can be opened from the other.
- [N-U22-002] The link exists in two forms: a direct link between a customer order line and a vendor order line (used for subcontracted services and direct vendor-to-customer shipments), and a shared reference record that groups the customer order, the movements and the vendor order (used for stock replenishment).
- [N-U22-003] When no vendor can be found for demand created by a customer order, the salesperson and the product's responsible person are told through a message on the customer order, and the demand falls back to being served from stock.
- [N-U22-004] Competing vendor quotations created as alternatives of a vendor order keep the link to the customer order line.

### WHY
- [N-U22-005] Sales staff need to see what was bought for their customers, purchasing staff need to see which customer needs a purchase, and both need warnings when the other side is cancelled or cannot be fulfilled.

### BUSINESS RULE
- [N-U22-006] Confirming a customer order creates, for each service flagged to be purchased, a vendor order line linked to the customer line; if no vendor exists for the service the confirmation is refused with a message asking for a vendor.
- [N-U22-007] Vendor orders created this way are grouped per vendor and per customer order: a draft vendor order is reused only if it already belongs to the same customer order, the same vendor and the same company. The customer order name is appended to the vendor order's origin text.
- [N-U22-008] A customer line that already produced a vendor line does not produce a second one when the order is cancelled and reconfirmed.
- [N-U22-009] Raising the quantity of such a service line changes the quantity on the latest vendor line when that vendor order is still a draft, sent or awaiting approval; if the vendor order is approved or cancelled, a new vendor line is created for the extra quantity.
- [N-U22-010] Cancelling a vendor order leaves a warning on each customer order concerned; cancelling a customer order leaves a warning on each generated vendor order that is not cancelled. Neither cancellation cancels the other document automatically.
- [N-U22-011] For stock replenishment, the incoming movement keeps the customer order line only when its final destination is a customer or in-transit location, and it inherits the customer line's routes.
- [N-U22-012] For a vendor line made from a replenishment request without a downstream movement, the customer line is stored on the vendor line, and later demands for the same customer line are merged only into vendor lines of that same customer line.
- [N-U22-013] The delivery address of a vendor order is taken from the customer orders only when all of them ship to the same partner; it is visible to the sales role and cannot be edited when the order is locked or comes from a customer order. Vendor orders created for services never carry a delivery address.
- [N-U22-014] When the vendor order is delivered straight to a customer, the movement description uses the product description in the customer's language so the delivery slip does not repeat the vendor order text.
- [N-U22-015] The analytic distribution of the customer line is copied to the vendor line; when the customer line has none and the order belongs to a project, the project's distribution is used, and the vendor order is also tagged with that project.

### STATE
- [N-U22-016] Vendor order: draft, sent, awaiting approval, approved, cancelled. The link to the customer order persists across these states; only quantity edits depend on the state as described.
- [N-U22-017] Customer order: when confirmed it may generate vendor lines; when cancelled it only leaves warnings. Demand that finds no vendor changes from made-to-order to served-from-stock.

### OPTIONALITY
- [N-U22-018] All three bridges install automatically when their parent modules are present and add no settings. Their behaviour depends on product configuration: vendor list, the flag to purchase a service on sale, the replenishment routes, and the project on the customer order.
- [N-U22-019] The alternative-quotation link exists only when the requisition bridge is installed; without it alternatives lose the customer line.

### DEPENDENCY
- [N-U22-020] Depends on the customer order, vendor order, stock replenishment engine and requisition features; the shared reference record is the stock engine's grouping object in this version.
- [N-U22-021] Service-purchase creation runs with elevated rights so salespeople without purchasing rights can still confirm orders.

### CONSTRAINT
- [N-U22-022] A service flagged for purchase on sale must have a matching vendor at confirmation, otherwise confirmation is blocked.
- [N-U22-023] A replenishment request started from a reordering rule with no matching vendor price fails with an error instead of falling back to stock.

### RISK
- [N-U22-024] The elevated-rights creation of vendor lines bypasses the salesperson's purchasing rights and should be considered in access reviews.
- [N-U22-025] Because cancelling one document only warns on the other, orphaned vendor orders or customer orders can remain open unless staff act on the warning.
- [N-U22-026] Without the requisition bridge, alternative quotations silently lose the customer link.

### UNKNOWN
- [N-U22-027] Behaviour of the shared reference record across companies, and the full result of merging multi-line demand into vendor lines, were not executed and need a runtime check.
- [N-U22-028] It is unknown what happens to the customer link when an alternative quotation is confirmed and the original is cancelled.

## CAP-U22-02 Promotion, coupon, gift card, prepaid wallet and loyalty program definition

### WHAT
- [N-U22-029] The business can define eight kinds of customer-incentive programs: coupons, gift cards, loyalty cards, automatic promotions, prepaid wallets, discount codes, buy-X-get-Y offers and next-order coupons. Promotion is the default kind.
- [N-U22-030] Each program has earning rules (what a customer must buy to earn points), rewards (what points can be exchanged for) and an optional communication plan of emails sent to card holders.
- [N-U22-031] A card or coupon belongs to one program, optionally to one customer, holds a points balance, has a unique code and may expire. Every manual issue or balance change leaves a history line.
- [N-U22-032] Staff can issue cards in bulk, adjust a card's balance with a recorded reason, and send a card by email; customers can view their own cards, history and affordable rewards in their portal.

### WHY
- [N-U22-033] Programs encourage repeat purchases and let the business sell prepaid value, and the history lines give an audit trail for every balance change.

### BUSINESS RULE
- [N-U22-034] A program is valid from its start date to its end date, both days included.
- [N-U22-035] A program is tied to named customers when it applies to both current and future orders, or when it is a prepaid wallet or loyalty program applying to future orders; otherwise cards may be anonymous.
- [N-U22-036] Gift cards and prepaid wallets are treated as payment instruments rather than discounts.
- [N-U22-037] Each program kind starts with sensible defaults: coupons are code-triggered with a 10 percent reward and a creation email; promotions are automatic, one point per order above a minimum of 50 with a 10 percent reward; loyalty cards earn points per money spent and give 5 off for 200 points; discount codes carry a generated code and give 10 percent on specific products; buy-X-get-Y earns per unit with a minimum of 2 and gives a free product for 2 points; next-order coupons need a minimum of 100 and give 15 percent.
- [N-U22-038] Gift card and prepaid wallet programs default to use on future orders, automatic trigger, portal visibility, earning per money spent on a dedicated top-up product, and a reward worth one currency unit per point on the whole order.
- [N-U22-039] Changing a program's kind replaces its rules, rewards and communication plan with the defaults of the new kind.
- [N-U22-040] Archiving a program archives its rules, rewards, communications and the hidden products behind its rewards; restoring it restores them. Archiving or restoring a single reward does the same for its hidden product.
- [N-U22-041] The trigger-product shortcut on a program is honoured only for gift card and prepaid wallet programs.
- [N-U22-042] A rule is code-triggered when it has a code and automatic when it has none.
- [N-U22-043] Product filters of rules and rewards combine explicit products, a category with all its subcategories and a tag with OR, then apply an optional extra condition with AND; with no filter every product qualifies.
- [N-U22-044] A rule's minimum purchase amount is converted to the order currency at the current exchange rate.
- [N-U22-045] Each reward owns a hidden service product used to show its discount on documents; it is not sellable, not purchasable, priced at zero and named after the reward description.
- [N-U22-046] A reward is a global discount when it is an order-wide discount given in percent or as a fixed amount per order.
- [N-U22-047] Card codes are generated automatically with a fixed prefix and a random part so that they can be scanned as barcodes.
- [N-U22-048] The creation email is sent only when the program has such a communication, the holder is known and no suppress-mail option is active; the sender falls back to the current internal user or the company when the template has none.
- [N-U22-049] When a card's points increase past one or more milestone thresholds, only the highest crossed milestone is emailed; decreases and cards without a customer never send milestone emails.
- [N-U22-050] Point changes on a card are tracked, and history lines record issued and used points with a mandatory description.
- [N-U22-051] A manual balance update must change the balance and cannot make it negative; it records the difference as issued or used points with a description, defaulting to a gift description.
- [N-U22-052] Bulk generation needs a program and a positive quantity, creates one card per selected customer or per unit of quantity for anonymous cards, and records an issuance history line for each card.
- [N-U22-053] Merging customers combines their named cards of the same program: points are added onto one surviving card for the kept customer and the others are zeroed and archived.
- [N-U22-054] A customer's active-card count includes cards with positive points in an active program that have not expired, including cards of the customer's contacts, and is rolled up to the parent company.
- [N-U22-055] The portal shows a customer only their own non-expired loyalty and prepaid-wallet cards, the five latest history lines of a card and up to three rewards the card can currently afford.
- [N-U22-056] Programs, rules, rewards, cards and history are visible only for the user's companies and shared records that have no company.

### STATE
- [N-U22-057] A program is active or archived; an active program cannot be deleted. Changing the kind rewrites its content. A card is active, or archived with zero points after a customer merge.
- [N-U22-058] A card's balance moves through issuance, manual adjustment, order-driven earning and spending, and merging; each manual change is matched by a history line.

### OPTIONALITY
- [N-U22-059] Programs can be created from templates, the gift card image is applied only when requested, and the whole feature is optional until a sales layer applies programs to orders.
- [N-U22-060] The simplified single-email setting exists only for gift card and prepaid wallet programs; other programs use the full communication plan.
- [N-U22-061] A global setting decides whether the full list of discounted products is precomputed; when absent it is enabled, and in the studied database it is explicitly disabled.
- [N-U22-062] The studied database contains only the default gift card program and no issued cards or history.

### DEPENDENCY
- [N-U22-063] The base feature only stores definitions and balances; applying programs to orders, spending points and the accounting of gift cards depends on the sales layer and is described elsewhere.
- [N-U22-064] Emails and printable gift card and coupon documents depend on the mail and reporting features.

### CONSTRAINT
- [N-U22-065] Limits, earned points, required points, reward quantity and discount values must all be strictly positive.
- [N-U22-066] A program's currency must match the currency of its price lists.
- [N-U22-067] A program's start date cannot be later than its end date.
- [N-U22-068] A program must always keep at least one reward, except while its kind is being changed.
- [N-U22-069] An active program cannot be deleted, and a program that has cards cannot be deleted.
- [N-U22-070] Splitting rewards per unit is not allowed for programs that apply to both current and future orders, nor for prepaid wallets.
- [N-U22-071] Codes must be unique: card codes among cards, and rule codes among active rules and cards.
- [N-U22-072] A reward product cannot be a combination product.
- [N-U22-073] Products and price lists used by active programs cannot be archived, and the seeded gift card and wallet products cannot be deleted.

### RISK
- [N-U22-074] Issuing cards to selected customers without choosing any customer or tag appears to select every customer, which could mass-issue and mass-email cards; this needs a runtime check.
- [N-U22-075] The ban on expiry dates for loyalty cards is enforced only when editing a card in the form, so bulk issuance can still set expiry dates on loyalty cards.
- [N-U22-076] The base permission table gives ordinary internal users no access to any loyalty record; access to manage programs depends entirely on the sales layer's permissions, so a deployment without it would lock everyone except administrators out.

### UNKNOWN
- [N-U22-077] Whether creation and milestone emails are actually delivered depends on mail configuration and was not tested.
- [N-U22-078] The accounting treatment of selling and redeeming gift cards and wallets, and how usage limits are consumed, are not in the base feature and were not studied here.
- [N-U22-079] How the product-matching helper behaves for rules without any product filter was not executed.

## CAP-U22-03 Free-shipping reward and prepaid-instrument restrictions

### WHAT
- [N-U22-080] A reward can waive the shipping charge: free shipping is an additional kind of reward in promotions and loyalty programs, optionally limited to a maximum amount.
- [N-U22-081] Gift cards and prepaid wallets cannot be combined with pay-on-delivery payment methods on the same order.

### WHY
- [N-U22-082] Customers can earn free delivery as an incentive, and prepaid value must be fully settled before dispatch, so it cannot be mixed with paying the carrier on delivery.

### BUSINESS RULE
- [N-U22-083] A free-shipping reward adds one negative line equal to the delivery charge of the order, limited by the reward's maximum when one is set, placed after all ordinary lines; if the order has no delivery charge line the reward line is zero.
- [N-U22-084] The points a free-shipping reward costs are its required points, or the customer's entire usable balance when the reward is set to clear the wallet.
- [N-U22-085] The reward line carries the same taxes as the delivery product, mapped by the order's fiscal position.
- [N-U22-086] Only one free-shipping reward can be active on an order at a time.
- [N-U22-087] Delivery charges and the shipping reward line do not count toward the minimum purchase amount or quantity needed to qualify for a program.
- [N-U22-088] Delivery charges never earn reward points.
- [N-U22-089] The order amount used to decide whether shipping is free excludes the delivery charge and adds back the value paid by gift cards and prepaid wallets, so settling part of the order with a prepaid instrument does not make the order look smaller; the same amount decides at shipment time whether the carrier price is forced to zero.
- [N-U22-090] New loyalty-card programs include a free-shipping reward costing 100 points, and a promotion created from the template offers free shipping on orders above 50.
- [N-U22-091] If an order carries gift card or prepaid wallet value, pay-on-delivery payment methods are hidden and reported as incompatible with those instruments.

### STATE
- [N-U22-092] An order either has no free-shipping reward line or exactly one; the line amount follows the delivery charge whenever the loyalty engine recomputes the order.

### OPTIONALITY
- [N-U22-093] The feature installs automatically when the promotion and delivery features are both present.
- [N-U22-094] The maximum amount on a free-shipping reward is optional; leaving it empty means no limit.
- [N-U22-095] In the studied database a pay-on-delivery provider is enabled and published, so the restriction can apply, but no program offers a free-shipping reward.

### DEPENDENCY
- [N-U22-096] The behaviour relies on the promotion engine of the sales layer, the delivery charge line and carrier price rules.
- [N-U22-097] The restriction relies on the payment method list and on the definition of which providers are pay-on-delivery.

### CONSTRAINT
- [N-U22-098] Only one free-shipping reward can be claimable at a time.
- [N-U22-099] Creating a payment on a pay-on-delivery method for an order that holds gift card or wallet value is refused with an error.

### RISK
- [N-U22-100] If the delivery charge line is missing when the reward is calculated, the reward line has zero value and may mislead staff into thinking shipping was waived.
- [N-U22-101] A promotion made from the template and one made by choosing the program kind receive different default rewards, which can surprise administrators.
- [N-U22-102] The payment restriction in the web checkout relies on a piece of the web shop that this feature does not declare as a dependency and that is not installed in the studied database, so it may be inactive.

### UNKNOWN
- [N-U22-103] Whether the web checkout restriction is active in a deployment without the web shop was not tested.
- [N-U22-104] The recomputation order of the delivery charge and the free-shipping line when the carrier changes after the reward was applied was not tested.
- [N-U22-105] The effect of clearing the whole wallet on a free-shipping reward was read only at its call site.

## CAP-U22-04 Margin cost sources and product margin report

### WHAT
- [N-U22-106] Every sales order line carries a cost and a margin: the margin is stored for reporting, the cost is an editable stored value, and the margin percent is the margin over the line subtotal.
- [N-U22-107] When the costing method is not standard, delivered quantities are costed at the actual outgoing valuation of the deliveries and the undelivered remainder at the standard price.
- [N-U22-108] Lines created from employee expenses use the actual expense amount per unit as their cost.
- [N-U22-109] A product margin report, launched from a small dialog, shows per product the sales and purchase quantities, average prices, turnover, total cost, expected versus actual sales and margins, based on invoices in a chosen period.

### WHY
- [N-U22-110] Sales staff and managers need margins that reflect what goods actually cost to deliver, not only a catalogue cost, and accountants need an invoice-based view of profitability per product.

### BUSINESS RULE
- [N-U22-111] By default a line's cost is the product's standard cost converted to the line's unit of measure and the order currency.
- [N-U22-112] A line's margin is its subtotal minus cost times quantity; for a line added from a delivery with no ordered quantity the delivered quantity is used instead.
- [N-U22-113] Margin and cost on order lines are visible only to internal users.
- [N-U22-114] Delivery-based costing applies only to lines that have at least one movement that is neither cancelled nor still a draft; other lines, and lines added from a delivery, use the default cost.
- [N-U22-115] Under a non-standard costing method the cost of a partly delivered line is the weighted average of the delivered quantity at its actual delivery unit cost (itself an average of direct-delivery and regular outgoing movements) and the undelivered remainder at standard cost, converted to the line's unit and currency; with nothing delivered it equals the standard cost.
- [N-U22-116] A line linked to an employee expense takes the expense's untaxed amount per unit as cost, converted from the expense currency; re-invoicing a bill line that comes from an expense stores the expense on the new sales line.
- [N-U22-117] The product margin report covers a period that defaults to the current calendar year and includes open and paid invoices unless the user chooses only paid, or also drafts.
- [N-U22-118] The report opens as a read-only list, form and chart of products.
- [N-U22-119] Paid means posted invoices that are in payment, paid or reversed; open and paid means all posted invoices; the draft option also adds draft invoices.
- [N-U22-120] The report always covers one company: the forced company or the current one.
- [N-U22-121] Report amounts come from invoice lines of product type only; credit notes and refunds reduce quantities and amounts, and prices are converted with the rate valid at the invoice date.
- [N-U22-122] Total margin is turnover minus the cost of vendor bills in the period; expected margin is the catalogue sale value of invoiced quantities minus the product's standard cost times the quantity billed by vendors.
- [N-U22-123] Only users with the full accounting role may use the report model, and the report appears under the accounting reporting menu without any further restriction.

### STATE
- [N-U22-124] A line's cost moves from the default standard cost to a blended delivery cost as deliveries are done, and to the expense cost when it comes from an expense; the report has no state, it recomputes from invoices each time it is opened.

### OPTIONALITY
- [N-U22-125] The delivery-cost and expense bridges install automatically; the report is an optional module.
- [N-U22-126] In the studied database every product category uses the standard costing method, so the delivery-cost blend has no effect there.

### DEPENDENCY
- [N-U22-127] Line margins rely on the sales margin feature; delivery costing relies on inventory valuation of outgoing movements; expense costing relies on the expense feature; the report relies on posted invoices and exchange rates.

### CONSTRAINT
- [N-U22-128] No validation rules are added; the cost can be edited by internal users.

### RISK
- [N-U22-129] For a line with deliveries under the standard method and an ordered quantity, the stored cost is not refreshed, so later changes of the standard cost do not flow into the margin of such lines.
- [N-U22-130] The report ignores draft invoices that have no invoice date even when drafts are requested, so draft-inclusive totals can be understated.
- [N-U22-131] Report totals are computed in application memory for all products in a grouped view, which can be slow on large catalogues.

### UNKNOWN
- [N-U22-132] Numerical results with partial deliveries, returns and direct vendor deliveries under non-standard costing were not tested.
- [N-U22-133] Report results and speed on a populated database were not tested.
- [N-U22-134] How an expense turns into the re-invoiced sales line is outside the studied features and was not read.

## CAP-U22-05 Project-linked stock transfers and re-invoicing of consumed materials

### WHAT
- [N-U22-135] Stock transfers can be tied to a project. When the transfer's operation type is set to generate analytic costs, validating the transfer records the cost on the project, and materials flagged for re-invoicing are billed through new lines on the project's sales order.
- [N-U22-136] Each sales line can list the stock movements linked to it for users who work in inventory.

### WHY
- [N-U22-137] Project profitability needs full traceability of inventory operations, and materials consumed by a project must be billed to the customer when the contract says so.

### BUSINESS RULE
- [N-U22-138] Re-invoicing happens only after a successful validation, only when the transfer's project has a re-invoiced sales order belonging to the project's customer and the operation type has the analytic-cost option, and only for products flagged to be re-invoiced at sales price or at cost.
- [N-U22-139] Re-invoiced lines are added to the existing order and do not start new deliveries.
- [N-U22-140] Under the sales price policy the line price is the order's price list price for one unit at the order date; under the cost policy it is the product's standard cost, converted to the order currency at the order date when currencies differ; a move with no done quantity is priced at zero.
- [N-U22-141] A new line is named after the transfer reference, its ordered quantity is the transfer demand, its delivered quantity the done quantity, it has no discount, takes the product's taxes mapped by the order's fiscal position, and is placed after the last line of the order (starting at 100 for an empty order).
- [N-U22-142] The order's project is copied to the transfers and procurement requests created from the order so that downstream operations remain tied to the project.
- [N-U22-143] With the analytic-cost option, a transfer's cost is distributed to the project's analytic accounts, named after the transfer and categorised as a transfer entry; transfers without a project or without the option produce no project cost.
- [N-U22-144] When anglo-saxon accounting is on, products re-invoiced at sales price or cost produce no project analytic entries, so their cost is not counted twice.
- [N-U22-145] From a project, delivery and receipt shortcuts default to the current user's warehouse operation types.
- [N-U22-146] The list of stock movements of a sales line is offered only for non-service lines and only to inventory users.

### STATE
- [N-U22-147] Validation of a project transfer is blocked while the order is a draft or sent quotation, cancelled, or locked; otherwise the transfer completes and the new lines appear in the same transaction.

### OPTIONALITY
- [N-U22-148] The behaviour is switched on per operation type and per project, and per product through its re-invoicing policy.
- [N-U22-149] Both bridges install automatically with their parent features.
- [N-U22-150] In the studied database no operation type has the analytic-cost option and anglo-saxon accounting is off, so none of this behaviour is active.

### DEPENDENCY
- [N-U22-151] Relies on the project, inventory, sales and analytic accounting features; the exclusion of re-invoiced products from project cost relies on the anglo-saxon accounting setting.

### CONSTRAINT
- [N-U22-152] A transfer cannot be validated when the project's sales order is a quotation, cancelled or locked.
- [N-U22-153] Every mandatory analytic plan for stock transfers must be set on the project before analytic entries can be generated.

### RISK
- [N-U22-154] Nothing distinguishes returns from deliveries, so returning a re-invoiceable product on a project transfer may add another positive line instead of reducing the billing.
- [N-U22-155] The anglo-saxon check follows the current user's company, which could be wrong in multi-company sessions.
- [N-U22-156] The new lines are created with elevated rights after the transfer is validated, so the validating user needs no sales rights on the order.

### UNKNOWN
- [N-U22-157] Behaviour with backorder dialogs and with several transfers validated at once was not tested.
- [N-U22-158] The resulting price, taxes and delivered quantity on a created line under a real price list and fiscal position were not tested.

## CAP-U22-06 Delivery batching by carrier and weight, and pickup-point shipping

### WHAT
- [N-U22-159] Outbound transfers can be grouped automatically into batches by carrier, with an optional maximum total weight per batch, so that parcels of the same carrier are picked and handed over together.
- [N-U22-160] Automatic batching works only if at least one grouping option is selected, and grouping by carrier counts as one.
- [N-U22-161] A customer can choose a pickup point of a parcel network as the shipping address of an order; the choice creates a delivery contact for the pickup point.

### WHY
- [N-U22-162] Warehouse staff handle fewer, carrier-specific batches, and pickup-point orders must pair the right delivery method with a pickup-point address so parcels are sent to a valid destination.

### BUSINESS RULE
- [N-U22-163] A weight limit per batch may be set on the operation type; a transfer joins a batch or pairs with another transfer only if the combined weight stays within the limit, and for waves the summed weight of the wave's movements is checked; no limit is applied when the value is empty or zero. The limit is shown in the system weight unit.
- [N-U22-164] When grouping by carrier, a transfer is batched only with transfers of the same carrier, or with transfers that have no carrier when it has none.
- [N-U22-165] A carrier-grouped automatic batch is described by its usual description followed by the carrier name.
- [N-U22-166] A ready transfer first tries to join an open compatible batch, otherwise it is paired with a compatible unbatched ready transfer into a new batch (confirmed automatically if configured), otherwise it forms a batch alone.
- [N-U22-167] A transfer's weight is the sum of the weights of its non-cancelled movements, each movement being its quantity times the product weight; products without a weight count as zero.
- [N-U22-168] A delivery method is a pickup-point method when its delivery product has the pickup-point reference, and a contact is a pickup point when its reference starts with the pickup-point prefix.
- [N-U22-169] The tracking link of a pickup-point carrier is built from the carrier's brand code, the parcel tracking reference and the customer's language.
- [N-U22-170] Choosing a pickup point reuses an existing delivery contact of the same customer with the same reference, street and postal code, or creates one named after the pickup point; it then becomes the order's shipping address.
- [N-U22-171] Customers cannot edit pickup-point contacts from the portal.
- [N-U22-172] The pickup-point picker offers only the countries listed on the delivery method.

### STATE
- [N-U22-173] A transfer is batched only while ready; an order cannot move from quotation to confirmed while the delivery method and the shipping address disagree about pickup-point use.

### OPTIONALITY
- [N-U22-174] Carrier and weight options appear only when automatic batching is enabled on the operation type; the batching bridge installs automatically with its parent features.
- [N-U22-175] The pickup-point brand code defaults to a test value and is reset to it whenever a database copy is neutralised.
- [N-U22-176] The pickup-point feature integrates only the picker widget; the carrier web service is not implemented, and the seeded carriers and prices are examples to adapt.
- [N-U22-177] In the studied database three pickup-point carriers exist but no operation type enables automatic batching.

### DEPENDENCY
- [N-U22-178] Batching depends on the batch and carrier-delivery features and on product weights; pickup-point selection depends on the delivery method dialog and on an external script served by the carrier network.

### CONSTRAINT
- [N-U22-179] Automatic batching cannot be enabled without at least one grouping option.
- [N-U22-180] An order with a pickup-point delivery method cannot be confirmed unless its shipping address is a pickup point, and an order with a pickup-point address cannot be confirmed with another delivery method.
- [N-U22-181] Confirming a pickup-point delivery method without choosing a pickup point is refused.

### RISK
- [N-U22-182] A transfer that alone exceeds the weight limit is never batched automatically, so heavy single orders silently stay outside batches.
- [N-U22-183] The pickup-point picker needs the user's browser to reach the carrier network's web host, so it fails where outbound access is filtered.

### UNKNOWN
- [N-U22-184] Behaviour for transfers with no weight data, and with waves, under real volumes was not tested.
- [N-U22-185] The picker widget, brand code validity and the data format returned by the carrier network were not tested.

## CAP-U22-07 Variant grid entry on sales and purchase orders

### WHAT
- [N-U22-186] On sales orders a product with several attribute combinations (for example sizes and colours) can be entered through a grid of quantities, per product, instead of one line per variant.
- [N-U22-187] The same grid entry exists on purchase orders for configurable products.

### WHY
- [N-U22-188] Order takers enter many variants quickly, and the customer or vendor document can show the quantities as a compact grid.

### BUSINESS RULE
- [N-U22-189] Grid headers can show the price extras of attribute values converted to the order currency at today's rate; they are shown on sales orders and not on purchase orders.
- [N-U22-190] The first attribute of the product forms the columns and the remaining attributes combine into rows.
- [N-U22-191] Each cell records whether the combination is possible and starts at zero quantity.
- [N-U22-192] The grid content is held temporarily on the screen and is never stored; only the resulting order lines are stored.
- [N-U22-193] Entering a quantity for a combination creates the variant if it does not exist and adds a line for it, using the usual defaults for a new line.
- [N-U22-194] Lines that belong to a combo item are not matched to grid cells.
- [N-U22-195] Orders print the variant grid when their print option is on (default on); on sales orders only products in grid mode are printed, and a product's grid is printed only when it has more than one line and non-zero quantities.
- [N-U22-196] Setting a cell to zero deletes the line on a draft or sent order, and sets the line quantity to zero on a confirmed order so the line is kept.
- [N-U22-197] On purchase orders, changing the grid does not overwrite the planned dates of existing lines, and the vendor prices of the touched lines are recomputed.

### STATE
- [N-U22-198] Opening the grid pre-fills it from the existing order lines; applying it creates, changes or removes lines according to the order state.

### OPTIONALITY
- [N-U22-199] On sales a product chooses between the configurator and the grid, with the configurator as default; the grid applies only to products with configurable attributes.
- [N-U22-200] Installing the grid feature turns on product variants for every internal user.
- [N-U22-201] In the studied database the variants feature is already granted to internal users and no product is set to grid mode.

### DEPENDENCY
- [N-U22-202] The shared grid builder is a technical component used by the sales and purchase features; it relies on product attributes and on the order lines of each side.

### CONSTRAINT
- [N-U22-203] A quantity cannot be changed through the grid for a variant that appears on more than one line of the order.

### RISK
- [N-U22-204] A screen condition compares the product mode with a value that no mode has, so the optional-products field stays visible in grid mode, which may confuse users.
- [N-U22-205] Setting a quantity to zero on a confirmed order keeps the line, which may leave empty lines on confirmed orders.

### UNKNOWN
- [N-U22-206] The screen widget that edits the grid was not reviewed or run.
- [N-U22-207] How grid quantity changes on confirmed orders propagate to deliveries and receipts was not tested.

## CAP-U22-08 Electronic order exchange, e-document network client and payment QR code

### WHAT
- [N-U22-208] A sales order can be exported as an electronic ordering document in the Peppol ordering format: the XML is embedded in the printed order PDF and portal customers can download it.
- [N-U22-209] Purchase orders can likewise be exported with the XML embedded in the PDF, and purchase orders can be created or completed from an uploaded ordering XML.
- [N-U22-210] A generic network client lets a company register an identity on an electronic-document access point, send signed requests, renew its token and decrypt received documents; it only works once a network-specific feature supplies the network type and server addresses.
- [N-U22-211] Seven extra free-text reference fields on invoices exist in a feature that the supplier itself marks as deprecated and not working.
- [N-U22-212] Invoices can show a SEPA credit transfer QR code when the receiving account is an IBAN account in a SEPA country and the currency is euro.

### WHY
- [N-U22-213] Electronic ordering, secure network connection and scannable payment codes reduce manual data entry and payment errors between trading partners.

### BUSINESS RULE
- [N-U22-214] A file is treated as an electronic order when its customization identifier equals the Peppol ordering value; the order decoder has priority 20 on both sales and purchase sides.
- [N-U22-215] If an import cannot resolve some data (for example an unknown product), the order is still created or completed, a note names the format used, and a to-do activity for the importing user lists what was not imported.
- [N-U22-216] Allowance and charge lines found in an imported order are added with sequence zero so they appear above the product lines.
- [N-U22-217] An exported sales order carries order type 220, its number, creation date, validity end date and the customer order reference; the delivery party is the shipping address, else the customer's first delivery contact, else the customer.
- [N-U22-218] Importing a sales order matches the buyer and delivery parties, stores the document number as the customer reference and the quotation reference as the origin, ignores the document note (the company's own terms prevail) and removes line discounts.
- [N-U22-219] After a sales import, price and discount of every line with a recognised product are recomputed from the company's own pricing, so prices in the received document are replaced.
- [N-U22-220] Variant identifiers in the document (extended item identification) are used, after the main identifiers, to find the exact product variant by internal reference or barcode.
- [N-U22-221] The order's electronic file can be downloaded by portal customers from a public link protected by the order's access token; only the first available format is offered.
- [N-U22-222] Orders created from uploaded files start with the uploading user's contact as customer.
- [N-U22-223] An exported purchase order carries order type 105, its number, creation date and the vendor reference; each line uses the vendor's own product code and name when the product has them; the delivery party is the order's delivery address, else the company's delivery contact, else the company.
- [N-U22-224] Importing a purchase order matches the vendor from the seller party, stores the document number as the vendor reference, the originator reference as the origin and the delivery party as delivery address, and keeps prices and discounts from the document.
- [N-U22-225] The purchase PDF's XML is generated with the current user's rights, whereas the sales PDF's XML is generated with elevated rights.
- [N-U22-226] Grouping or ungrouping invoice lines by tax is refused for invoices linked to a purchase order.
- [N-U22-227] A proxy user belongs to one company, one network type and one mode, owns a generated key pair, and its token is readable only by system administrators; invoicing users have read-only access and the list is visible only in debug mode.
- [N-U22-228] Requests to the access point are signed, time out after 30 seconds and are blocked entirely in demo mode; connection problems are reported as one generic error that names the address.
- [N-U22-229] When the access point reports an expired token the client renews it, saves immediately and retries once; an unknown-user answer deactivates the local identity; an invalid-signature answer explains that another database may be using the same identity.
- [N-U22-230] Received data is decrypted in two steps: a symmetric key is decrypted with the identity's private key, then the data is decrypted with that key.
- [N-U22-231] Demo registrations are simulated locally without any network call, and copying or neutralising a database sets connections to demo or test mode so copies cannot act on live connections.
- [N-U22-232] A SEPA QR code needs euro currency, an IBAN receiving account whose country belongs to the SEPA zone (excluding territories sharing another country's code), and an account holder name or partner name.
- [N-U22-233] The QR content follows the SEPA credit transfer layout; a valid structured payment reference is sent as such, otherwise the free text (up to 141 characters) is used; the beneficiary name is limited to 71 characters.
- [N-U22-234] QR methods are tried in priority order and the first one without an error is used; the SEPA method has priority 20.

### STATE
- [N-U22-235] An uploaded file leads to a created or completed order; an identity is unregistered, registered, deactivated or has an expired or renewed token; a bank account either qualifies for the SEPA code or not.

### OPTIONALITY
- [N-U22-236] The order exchange features and the SEPA code install automatically with their parent features and have no settings; without them an order has no electronic format.
- [N-U22-237] The deprecated reference-field feature is installed only on request and its supplier advises against using it.
- [N-U22-238] In the studied database the network client has no identity and no network feature is installed, the deprecated columns exist, and the SEPA module is installed.

### DEPENDENCY
- [N-U22-239] The network client depends on accounting and key management and is meant to be extended by a network-specific feature that provides the network types and server addresses; none is installed in the studied database.

### CONSTRAINT
- [N-U22-240] A client identifier is unique, and a company can have only one active identity per network type and mode.
- [N-U22-241] A SEPA QR code cannot be created without an account holder name or partner name on the receiving account.

### RISK
- [N-U22-242] A received sales order's prices and discounts are overwritten by the company's own pricing for recognised products, so price disagreements are not visible.
- [N-U22-243] The purchase feature's own description says the PDF is embedded in the XML while the behaviour is the reverse, which may mislead implementers.
- [N-U22-244] The deprecated reference fields are not shown on the invoice form and are apparently not read by the export, so any data entered programmatically would have no effect.
- [N-U22-245] The client saves its work inside a request when renewing a token, and the renewal code reads the new token even after an error response, so failures could leave partial state or raise unexpected errors.

### UNKNOWN
- [N-U22-246] Conformance of exported or imported order documents and all network behaviour were not tested.
- [N-U22-247] Whether a SEPA code actually appears on invoices in this deployment depends on bank account type, invoice currency and company settings, and was not tested.

## CAP-U22-09 Print-on-demand fulfilment through an external service

### WHAT
- [N-U22-248] Sales orders for products that an external print-on-demand service prints and ships are forwarded to that service when the order is confirmed.
- [N-U22-249] Two delivery methods, standard and express, are provided for such orders and are separate from ordinary delivery methods.
- [N-U22-250] Products can be synchronised from a template at the service: variants, attribute values and print images are created from it.
- [N-U22-251] The service reports progress back to the company through a notification channel that is accepted only after a shared secret check.

### WHY
- [N-U22-252] The company can sell customised printed goods without holding stock, while the sales order stays the commercial record and the service handles production and shipping.

### BUSINESS RULE
- [N-U22-253] An order cannot mix print-on-demand products with ordinary goods; sections, notes, non-saleable lines and services are ignored by this check, which runs whenever lines change.
- [N-U22-254] Print-on-demand orders can only use the service's delivery methods, and ordinary orders can never use them.
- [N-U22-255] Before an order is sent or a shipping price is requested, the shipping contact must have city, country, email, name and street, and a postal code unless the country has none.
- [N-U22-256] On confirmation a draft order is created at the service; after the company's transaction is saved the draft is confirmed at the service, and if it is rolled back the draft is deleted, to avoid duplicate live orders.
- [N-U22-257] The order sent to the service lists each product with its identifier, print images (as links carrying an access token), whole-number quantity, the chosen shipping level (standard, express or cheapest) and the shipping address trimmed to the service's length limits.
- [N-U22-258] If creating the draft fails, the confirmation is refused with a message naming the order; if confirming or deleting the draft later fails, only a note is posted, so the two systems can disagree. Calls time out after ten seconds.
- [N-U22-259] The shipping price comes from a quote: for each quote the lowest price of the matching service level is taken and the prices are added; if any quote lacks that level, the method is reported as unavailable.
- [N-U22-260] A notification is accepted only if its secret equals the secret stored for the order's company; with no stored secret every notification is rejected.
- [N-U22-261] A cancelled fulfilment cancels the sales order and logs it; failed and returned fulfilments are logged; in-transit notifications email the customer tracking links; delivered notifications email the customer.
- [N-U22-262] Synchronising a product creates attributes, values and variants from the service template, removes variants the service does not offer, and uses the current company's credentials.
- [N-U22-263] One print image per placement is kept; placements called 1 or front are renamed to the default placement.
- [N-U22-264] Print-on-demand lines do not start any warehouse delivery.

### STATE
- [N-U22-265] A confirmed order stays confirmed while the service works on it; service progress changes only notes and emails, except cancellation which cancels the order.

### OPTIONALITY
- [N-U22-266] Credentials are stored per company, readable only by system administrators, and are cleared when a database is copied for testing.
- [N-U22-267] The warehouse bridge installs automatically with the sales stock feature.
- [N-U22-268] In the studied database the two delivery methods and the status email exist but no credentials are stored.

### DEPENDENCY
- [N-U22-269] The feature depends on sales, delivery methods and, for the warehouse bridge, sales stock.
- [N-U22-270] It depends on the external service being reachable, on a public web address for the print images, and on the service calling back the notification address.

### CONSTRAINT
- [N-U22-271] Print-on-demand and ordinary goods cannot be on the same order.
- [N-U22-272] The shipping contact must be complete before sending the order or requesting a price.
- [N-U22-273] Every print image must have a file before the product can be ordered.

### RISK
- [N-U22-274] Because no warehouse movement exists for these lines, their delivered quantity may stay at zero and delivery-based invoicing could never trigger unless quantities are set manually.
- [N-U22-275] Confirmation at the service happens after the company's transaction is saved, so a service-side failure leaves the order confirmed locally but not at the service.
- [N-U22-276] The notification secret is a fixed value in a header with no timestamp or content binding, so a captured request could be replayed.
- [N-U22-277] An internal customer number and the customer's name, email, phone and address are sent to the service, which matters for data protection.
- [N-U22-278] A notification with missing fields causes a server error instead of a controlled rejection.
- [N-U22-279] Service-driven cancellation runs with elevated rights and bypasses lock or access checks that a user cancellation would meet.

### UNKNOWN
- [N-U22-280] The external service's behaviour and the delivery of notifications were not tested.
- [N-U22-281] How delivered quantity and invoicing are completed for these lines was not determined.

## CAP-U22-10 Postal dispatch of invoices and small posting-time bridges

### WHAT
- [N-U22-282] A customer can be set to receive invoices by post: sending the invoice creates a physical letter through a paid external postal service.
- [N-U22-283] A product can have an email that is sent to the customer when an invoice containing it is posted.
- [N-U22-284] Letters can be re-sent or cancelled from the message that records them.
- [N-U22-285] Vendor bill lines assigned to a company vehicle create a vehicle service log; sales managers can manage text-message templates for orders and contacts; service lines are flagged for faster searching; equipment can be given a stock location and linked to matching serial numbers.

### WHY
- [N-U22-286] Customers who need paper documents receive them without manual printing and posting, and small links keep vehicle costs, customer messages and equipment records consistent with accounting and stock.

### BUSINESS RULE
- [N-U22-287] Letters are sent to an external postal service using the company's prepaid account; the service address and the time limit can be changed by system settings, with a default of thirty seconds.
- [N-U22-288] Creating a letter records a message and a notification on the document and copies the recipient's address; changing the partner's address later updates all letters not yet sent or cancelled.
- [N-U22-289] The letter content is the invoice rendered again in A4 with a supported layout, margins whitened for the printer and an optional cover page showing the address; the return address is the company's address.
- [N-U22-290] A letter can be sent only to a recipient with a name and a complete address (street, city, postal code and country); otherwise it is marked as failed, and the send wizard warns about invoices that will not be sent.
- [N-U22-291] When several letters are sent together, colour, cover and both-sides options are taken from the first letter; the currency used for pricing is euro.
- [N-U22-292] After each letter is sent the work is saved, so it cannot be sent twice; credit errors raise a no-credit notification, and an access error marks all letters of the request as unknown errors.
- [N-U22-293] Sending an invoice by post queues the letter for the daily run, while the manual send-now action sends at once only when a single letter is selected.
- [N-U22-294] A daily queue run sends pending letters and retries letters that failed for trial, credit, attachment or missing-field reasons, stopping after the first credit error.
- [N-U22-295] Cancelling postal notifications cancels the user's failed letters for that kind of document.
- [N-U22-296] Choosing the boxed, bold or striped report layout forces the cover page option on.
- [N-U22-297] Internal users can read, edit and create letters but not delete them; administrators have full control; no company restriction is defined for letters.
- [N-U22-298] Deleting an invoice deletes its letters.
- [N-U22-299] Posting a customer invoice emails the customer once for every invoice line whose product has an email template, even when the same product appears on several lines.
- [N-U22-300] The product form's invoicing tab is shown only to accounting roles.
- [N-U22-301] Posting a vendor bill creates one vehicle service log for each product line that has a vehicle and no log yet, so reposting does not duplicate; refunds and receipts are excluded; a message links the bill.
- [N-U22-302] A vehicle service cost equals the bill line's debit and cannot be edited or deleted directly; clearing the vehicle on the line or deleting the line removes the log.
- [N-U22-303] The vehicle's bill count and list are available only to users with accounting read access.
- [N-U22-304] Period-change accounting entries keep the vehicle on the matching line.
- [N-U22-305] Sales managers may create, change and delete only text-message templates meant for orders and contacts.
- [N-U22-306] Service lines carry a stored flag for services and a fast name search; several service lines of the same product on one order can show their prices in their names.
- [N-U22-307] Equipment can be assigned an internal stock location, a location shows how many items of equipment it holds, and an equipment record links to lots whose name equals its serial number for users with lot tracking rights.

### STATE
- [N-U22-308] A letter is queued, sent, failed or cancelled; failed letters of retryable kinds return to the queue on retry; a posted invoice triggers product emails and a posted vendor bill triggers vehicle logs.

### OPTIONALITY
- [N-U22-309] Vehicle assignment on bill lines is never mandatory, because the required-vehicle helper is fixed to false.
- [N-U22-310] In the studied database the vendor bill service type exists and there are no vehicles.
- [N-U22-311] In the studied database the queue run is active every 24 hours, there are no letters or postal account, and no company report layout is chosen.
- [N-U22-312] The invoice-by-post, fleet, text-message and equipment links install automatically with their parent features; the product email and service flag features are installed on request.
- [N-U22-313] Postal options appear in accounting settings only when the invoice-by-post link is installed.

### DEPENDENCY
- [N-U22-314] Postal sending depends on a prepaid account with an external postal service, on its web address, and on correctly formatted A4 documents; product emails depend on the mail configuration; vehicle logs depend on the fleet feature.

### CONSTRAINT
- [N-U22-315] A letter needs a readable attachment and an A4 report format.
- [N-U22-316] A vehicle service created from a bill cannot have its amount edited or be deleted directly.

### RISK
- [N-U22-317] A letter rejected for having too many pages is stored as an unknown error and is never retried by the queue, so it can stay unsent without attention.
- [N-U22-318] The postage estimate counts recipients, not invoices, so it can understate the cost when one customer has several invoices.
- [N-U22-319] Letters have no company restriction and carry invoice content to a paid third party, which matters for access reviews and data protection.
- [N-U22-320] Product emails are sent at posting time without a visible queue and can duplicate when a product appears on several lines.

### UNKNOWN
- [N-U22-321] The external postal service's behaviour, credits and printed result were not tested.
- [N-U22-322] Who receives product emails and how they are queued was not tested.
- [N-U22-323] Whether letters of one company are visible to users of another was not determined.
- [N-U22-324] What happens to vehicle logs when a posted bill is reset or reversed was not determined.

