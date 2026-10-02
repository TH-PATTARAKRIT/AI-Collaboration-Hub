# U89 Neutral Knowledge — Website eCommerce Flow
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U89-001 | The eCommerce cart is not a separate data entity; it reuses the core sales quotation model with an additional website reference field to distinguish online orders from back-office quotations. |
| NR-U89-002 | Every cart record carries a reference to the originating website, allowing multi-website deployments to isolate their respective carts. |
| NR-U89-003 | The active cart identifier is stored in the web session under a fixed key; the value is the numeric database identifier of the cart record. |
| NR-U89-004 | Cart creation is triggered the first time a visitor adds a product; the platform creates the quotation record with elevated privileges then immediately downgrades to the visitor's permission level for subsequent access. |
| NR-U89-005 | The new cart record is created using administrator-level access to bypass potential permission restrictions for public visitors, then wrapped back to the visitor's access rights. |
| NR-U89-006 | After creation, the cart identifier and cart item count are stored in the session to avoid repeated database queries on page load. |
| NR-U89-007 | On each frontend request the platform retrieves the session cart, validates it is still a draft (not yet confirmed), and verifies the linked payment transaction has not already been processed; mismatches trigger a cart reset. |
| NR-U89-008 | If no session cart is found and the visitor is logged in, the platform searches for an abandoned draft quotation for that customer and resurfaces it as the active cart. |
| NR-U89-009 | A cart is automatically discarded from the session if its state is no longer draft, or if the attached payment transaction has already been paid or is pending capture. |
| NR-U89-010 | A new cart is pre-populated with the website's sales team, the visitor's applicable fiscal position, the current pricelist, and the website company. |
| NR-U89-011 | Adding a product to the cart routes through a single cart-update entry point that determines whether to increment an existing line or create a new one. |
| NR-U89-012 | If a matching cart line exists (same product, unit of measure, no custom attributes), the quantity is incremented on that line rather than creating a duplicate. |
| NR-U89-013 | When no matching line exists, a new order line is created after resolving the closest valid product variant and verifying the variant combination is purchasable. |
| NR-U89-014 | The checkout page at the dedicated checkout URL is accessible to unauthenticated visitors unless the website is configured to require login before checkout. |
| NR-U89-015 | The checkout page reads the session cart and stores its identifier separately in the session to allow post-payment retrieval even after the main cart session key is cleared. |
| NR-U89-016 | If the cart contains physically shippable products, available delivery methods are fetched and the preferred one is automatically applied before rendering the checkout page. |
| NR-U89-017 | Applying a delivery method removes any existing delivery line, fetches a live shipment rate, and creates a new delivery order line if the rate calculation succeeds. |
| NR-U89-018 | Delivery methods eligible for display are filtered to those published on the website and available for the order based on carrier-specific availability rules. |
| NR-U89-019 | The payment step page presents available payment providers and recomputes cart totals (taxes, delivery price) immediately before display. |
| NR-U89-020 | The payment form is configured with two routes: one for initiating the transaction and one as the landing destination after the provider redirects the customer back. |
| NR-U89-021 | The post-payment landing route determines the transaction state and redirects to the order confirmation page; it also handles the edge case where the user navigates back to the cart after payment. |
| NR-U89-022 | For zero-amount carts (fully covered by discounts or free items) there is no payment transaction; the quotation is confirmed directly when the customer proceeds. |
| NR-U89-023 | After the payment landing route processes the result, the session is fully cleared of cart, pricelist, and fiscal-position data. |
| NR-U89-024 | A payment transaction has six possible states: draft (created not yet sent), pending (awaiting provider confirmation), authorized (funds reserved), done (confirmed, funds captured), cancel (voided), and error. |
| NR-U89-025 | Moving a transaction to the confirmed state is permitted from draft, pending, authorized, or error states; the transition also triggers cascading updates on any source transactions. |
| NR-U89-026 | Moving to the cancelled state is only permitted from draft, pending, or authorized; a confirmed transaction cannot be cancelled through the standard state machine. |
| NR-U89-027 | Every state transition records the new state, an optional message, the transition timestamp, and resets the post-processing flag so the new state can be post-processed. |
| NR-U89-028 | After a transaction reaches a terminal state, the sales module's post-processing layer runs additional business logic such as confirming the linked quotation and optionally generating an invoice. |
| NR-U89-029 | For confirmed (done) transactions the post-processing checks whether the paid amount meets the required prepayment threshold; if so it confirms the linked quotation. |
| NR-U89-030 | Order confirmation from a payment transaction requires exactly one linked quotation, the quotation must be in draft or sent state, and the payment amount must satisfy the prepayment requirement. |
| NR-U89-031 | The confirmation call is made with context flags that trigger the order confirmation email and include a signature reference. |
| NR-U89-032 | Confirming a quotation writes the state to the confirmed (sale) value, records the confirmation timestamp, then calls the internal confirm hook and optionally locks and emails the customer. |
| NR-U89-033 | The state transition from draft to confirmed records the current timestamp as the order confirmation date. |
| NR-U89-034 | The confirmation email is only sent when the confirmation action is called with the send-email context flag; it uses a website-specific email template if configured. |
| NR-U89-035 | When a sales order with storable products is confirmed, the stock procurement engine is invoked to generate the delivery order. |
| NR-U89-036 | The stock rule engine receives procurement requests for each order line of type storable goods, creates the stock references, and calls the routing engine with the quantity and values. |
| NR-U89-037 | The routing engine creates stock picking and stock move records according to the product's configured routes (customer delivery, make-to-order, buy, manufacture). |
| NR-U89-038 | After procurement records are created, any new draft pickings are immediately confirmed (not just created) to trigger availability checking and scheduler processing. |
| NR-U89-039 | The eCommerce override of order confirmation runs the confirmation as administrator and ensures the salesperson is assigned at this point, not earlier (to avoid unnecessary notifications on draft carts). |
| NR-U89-040 | The order confirmation email template can be customised per website; if a website-specific template is configured it takes precedence over the system default. |
| NR-U89-041 | Product templates published on the website inherit a multi-website publication mixin that provides both a stored publication flag and a computed visibility field scoped to the current website context. |
| NR-U89-042 | Product visibility in the shop is controlled by the stored publication flag; the computed website-visibility field reflects whether the product is published AND belongs to (or is unscoped from) the current website. |
| NR-U89-043 | A product assigned to a specific website is visible only on that website even if its publication flag is true; unscoped products (no website assignment) appear on all websites when published. |
| NR-U89-044 | The shop product query applies a published filter for public visitors and omits it for internal users, giving staff a preview of unpublished products. |
| NR-U89-045 | The pricelist applied to a new cart is taken from the session-cached pricelist at cart creation time. |
| NR-U89-046 | The session pricelist is determined from the visitor's partner default pricelist, filtered to those available on the website; GeoIP country is used to further filter eligible pricelists. |
| NR-U89-047 | For carts linked to a website, pricelist recomputation applies the visitor's detected country code for GeoIP-based pricelist selection. |
| NR-U89-048 | The website has a customer-accounts setting with three values: optional login (default), disabled accounts (guest-only mode), and mandatory login (no guest checkout). |
| NR-U89-049 | When guest checkout is disabled (mandatory login), public visitors accessing the checkout page are redirected to the login page with a return URL back to checkout. |
| NR-U89-050 | An anonymous (guest) cart is identified by its customer being the website's public user; this distinction is used in address-validation and cart-lifecycle logic. |
| NR-U89-051 | The visitor tracking model records product page views for analytics purposes but does not directly link to the active cart; the cart link is maintained exclusively through the session. |
| NR-U89-052 | Visitor-to-cart association is session-based only; the visitor model tracks browsing behaviour (pages, products viewed) independently from purchase intent. |
| NR-U89-053 | Payment transactions are linked to sales orders through a many-to-many relationship stored in a dedicated relation table; this allows one transaction to cover multiple orders (though full checkout supports only one). |
| NR-U89-054 | A background scheduled job retries post-processing for transactions where the client-side redirect did not complete successfully; it processes transactions up to four days old. |
| NR-U89-055 | The base payment module's post-processing does nothing except mark the transaction as post-processed; all meaningful post-processing (order confirmation, invoicing) comes from module-level overrides. |
| NR-U89-056 | Automatic invoice generation after payment is controlled by a system configuration parameter; when enabled, confirmed orders receive invoices immediately upon transaction post-processing. |
| NR-U89-057 | Invoice generation distinguishes between fully paid orders (which get a final invoice) and partially paid orders (which get a down payment invoice for the captured amount). |
| NR-U89-058 | Free orders (no payment required) bypass the transaction flow entirely and are confirmed through a direct call that includes the send-email flag. |
| NR-U89-059 | The confirmation amount threshold is determined by a prepayment percentage or fixed amount configured on the order; the check compares the cumulative paid amount to this threshold. |
| NR-U89-060 | For payment providers that support manual capture (two-step: authorize then capture), the quotation is confirmed at the authorization stage, before full capture. |
| NR-U89-061 | A cart is considered ready to proceed to payment only when it contains at least one order line and no zero-priced products (when zero-price sales are restricted). |
| NR-U89-062 | Before payment, an additional validation checks that physical orders have a delivery method selected and that the selected method is still compatible with the delivery address. |
| NR-U89-063 | A cart is considered abandoned when it has been idle (no update) for longer than the configured abandonment delay, the customer has a known email address, no transaction error exists, and the customer has not completed another order in the window. |
