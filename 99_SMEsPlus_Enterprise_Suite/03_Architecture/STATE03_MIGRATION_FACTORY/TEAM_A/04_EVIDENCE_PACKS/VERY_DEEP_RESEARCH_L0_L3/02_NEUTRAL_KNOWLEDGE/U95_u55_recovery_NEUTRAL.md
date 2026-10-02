# U95 Neutral Knowledge — U55 Recovery

> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U95-001 | The opportunity-to-quotation bridge installs automatically whenever both the sales and CRM modules are active, requiring no manual configuration step. |
| NR-U95-002 | The bridge depends on both the base sales module and the CRM module; it cannot be installed without both present. |
| NR-U95-003 | The bridge module includes a cleanup routine that executes when the module is removed from the system. |
| NR-U95-004 | A CRM opportunity record can display three aggregated sales figures: total untaxed revenue of confirmed orders, a count of draft/sent quotations, and a count of confirmed orders. |
| NR-U95-005 | The link between a CRM opportunity and its associated sales orders is stored as a one-to-many relationship; each sale order carries a reference back to its originating opportunity. |
| NR-U95-006 | When computing total revenue on an opportunity, the system converts each order's untaxed amount to the company's base currency using the order date as the conversion rate reference point. |
| NR-U95-007 | Orders in draft, sent, or cancelled state are excluded from the confirmed-order count on a CRM opportunity; only fully confirmed orders are counted. |
| NR-U95-008 | Creating a new quotation from a CRM opportunity pre-fills marketing attribution fields (campaign, medium, source) and contact details automatically. |
| NR-U95-009 | When two CRM opportunities are merged, all sales orders linked to both records are consolidated under the surviving opportunity. |
| NR-U95-010 | If a newly linked sales order has a higher untaxed value than the opportunity's current expected revenue — and both share the same currency — the expected revenue is automatically raised to match. |
| NR-U95-011 | The sale-loyalty bridge activates automatically when both the sales and loyalty-program modules are installed; it enables discount codes, gift cards, and reward programs on sales orders. |
| NR-U95-012 | A sales order tracks coupons that a user explicitly applies and the promotion rules that are manually triggered; both lists are not copied when the order is duplicated. |
| NR-U95-013 | Each sales order maintains a set of coupon-point records that describe how many loyalty points have been earned and how they are allocated across loyalty cards. |
| NR-U95-014 | The total reward value on an order is the sum of discount-type reward lines minus the list price of any free-product reward lines; free products are ordinary order lines priced at zero. |
| NR-U95-015 | For confirmed orders, loyalty history is read from the database in a single aggregated query, summing points issued and points used per order; the result is serialized as structured data for display. |
| NR-U95-016 | The Sales application module is the user-facing sales management product; it installs on top of the base sales module and adds quotation templates, digest integration, and online-signature or payment confirmation flows. |
| NR-U95-017 | A quotation template is a reusable record that stores a set of product lines, terms-and-conditions text, a validity period in days, online-signature and prepayment requirements, and an optional confirmation email. |
| NR-U95-018 | If a quotation template specifies an invoicing journal, all sales orders created from that template will invoice into that journal; the setting is company-specific. |
| NR-U95-019 | A shared quotation template (not restricted to a single company) cannot contain products that belong to a specific company; a template scoped to one company cannot include products from an incompatible company. |
| NR-U95-020 | When online prepayment is required, the prepayment percentage must be strictly greater than zero and at most one hundred percent; any other value is rejected. |
| NR-U95-021 | Archiving a quotation template automatically removes it as the default template from all companies that referenced it, preventing future orders from referencing a deactivated template. |
| NR-U95-022 | A sales order may reference a quotation template; if it does, the template's settings override the corresponding order-level settings for signature requirement, payment requirement, validity date, and invoicing journal. |
| NR-U95-023 | Switching the quotation template on an unsaved order clears all existing order lines and replaces them with the lines from the new template, with the first line set to a low sequence number to avoid page mixing in reports. |
| NR-U95-024 | Confirming a sales order that has a template with a notification email sends that email after confirmation, but only when the confirmation was initiated from the back end without a simultaneous send-email action. |
| NR-U95-025 | The margins module adds profitability fields to the sales module; it depends on the Sales application module rather than the base sales module. |
| NR-U95-026 | Each sales order line gains a cost field, a margin amount, and a margin percentage; the cost field is editable so users can override the computed default. |
| NR-U95-027 | The computed cost on a sales order line is derived from the product's standard cost, converted to the line's unit of measure and then to the order's currency using the product's cost currency. |
| NR-U95-028 | For order lines added from a delivery (where the ordered quantity is zero), margin is computed using the delivered quantity and unit price rather than the ordered quantity and subtotal. |
| NR-U95-029 | The sales order header aggregates margin from all lines; the margin percentage at order level uses the order's untaxed total as the denominator. |
| NR-U95-030 | When recomputing margins in batch (for example during module installation), the system uses a single database aggregation query for efficiency; for single unsaved records it falls back to an in-memory sum. |
| NR-U95-031 | The sales-manufacturing bridge activates automatically when both the manufacturing and sales-warehouse modules are installed; it adds a sales-order count and an originating sales-line reference to production orders. |
| NR-U95-032 | A production order can display how many sales orders are linked to it, combining orders reachable via stock references and the direct originating sales-order line. |
| NR-U95-033 | The count of linked sales orders on a production record uses set-union logic to avoid double-counting orders reachable via multiple paths. |
| NR-U95-034 | When a production order is confirmed, the finished-goods stock move inherits the sales-order-line reference so that the linkage is preserved into the downstream delivery. |
| NR-U95-035 | The sale-matrix module adds a grid-based variant entry interface to sales orders; it depends on the base sales module and the product-matrix module. |
| NR-U95-036 | A sales order gains a flag controlling whether variant grids appear in printed reports, plus three transient (non-stored) fields that form the client-side matrix state machine. |
| NR-U95-037 | When a user submits matrix changes, each modified cell is translated into a create or update of the corresponding product-variant order line; setting a cell to zero removes the line if the order is still in draft or sent state. |
| NR-U95-038 | The matrix displayed to the user is constructed server-side by fetching the product template's attribute matrix and overlaying current order-line quantities into the matching cells. |
| NR-U95-039 | The sales-project bridge activates automatically when both the Sales application and the project-accounting module are present; it enables task and project generation from sales orders. |
| NR-U95-040 | A service sales order line can be configured to deliver by milestones; it gains a generated-project field, a generated-task field, and a link to the reached milestones that determine delivered quantity. |
| NR-U95-041 | Milestone-based delivery is activated per line when the product is a service with the milestones delivery type; all other lines use the standard delivery method resolution. |
| NR-U95-042 | When adding a sales order line directly from a project context, the system finds or creates a sales order for the given partner, optionally linking it to an existing project. |
| NR-U95-043 | The sales-warehouse bridge activates automatically when both the base sales and stock-accounting modules are installed; it adds incoterms, shipping policy, warehouse, and full delivery tracking to sales orders. |
| NR-U95-044 | A sales order gains fields for international commercial terms, delivery location, a shipping-policy choice (ship as soon as possible or all at once), a warehouse reference, and a link to all related stock transfers. |
| NR-U95-045 | The delivery status on a sales order is a stored computed field with four states: not delivered, started, partially delivered, and fully delivered; it is recomputed whenever linked picking states change. |
| NR-U95-046 | During installation, the warehouse column on existing sales orders is backfilled by a direct database update matching each order's company to a warehouse of that company. |
| NR-U95-047 | A confirmed sales order with storable products must have a warehouse assigned; the system raises an error if no warehouse is found for the order's company or for a cross-company delivery route. |
| NR-U95-048 | If a confirmed sales order's ordered quantity decreases, the system schedules a warning activity on affected stock transfers to alert the warehouse team. |
| NR-U95-049 | Updating the commitment date on a confirmed sales order propagates the deadline to all open outgoing stock moves associated with that order. |
