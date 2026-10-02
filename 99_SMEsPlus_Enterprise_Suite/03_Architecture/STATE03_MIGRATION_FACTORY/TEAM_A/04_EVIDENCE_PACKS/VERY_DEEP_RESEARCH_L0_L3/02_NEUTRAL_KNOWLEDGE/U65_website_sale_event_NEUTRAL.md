# U65 — Website Sale, Event and Mass Mailing — Neutral Knowledge
**Pack:** VERY_DEEP_RESEARCH_L0_L3 | **Unit:** U65 | **Prepared:** 2026-10-02

This file contains plain-language business descriptions. Technical identifiers, file extensions, code keywords, and dotted model names are excluded.

---

## [N-U65-001] Product Visibility in the Online Shop

WHAT: A product must be explicitly published before it appears in the online shop. Once published, the system records the exact date and time of publication. Unpublished products are automatically hidden from the shop listing for customers, though internal staff can still access them.

WHY: Businesses need to control when a new product becomes purchasable. The publication date supports date-stamped reporting and lets businesses track how long a product has been live.

BUSINESS RULE: Any product that is not actively published is invisible to customers and cannot be added to a cart. Products with zero price are also blocked from cart addition when the store operator has enabled the "prevent zero price sale" setting.

STATE: Publication is a toggle on the product record. Setting it activates shop visibility and stamps a timestamp. Clearing it hides the product without deleting it.

---

## [N-U65-002] Pricing and Discount Logic in the Shop

WHAT: The price shown to a customer in the shop is determined by the active pricelist assigned to that customer's session. The pricelist may apply percentage discounts, formula-based adjustments, or fixed prices. When a pricelist rule qualifies for strikethrough display, a "before-discount" price is shown alongside the reduced price.

WHY: Businesses use pricelists to manage different customer tiers (retail, wholesale, promotion), and displaying the original price alongside the discount encourages purchase.

BUSINESS RULE: Pricelist items that use a percentage rule or a formula with an explicit discount against the catalogue price qualify for strikethrough display on the product and shop pages. The comparison price field (a manually entered higher price) is suppressed when a pricelist is active, to avoid confusing double discounting.

STATE: Price computation happens at page load per product-pricelist combination. The result includes both the effective price and, if applicable, the pre-discount price.

---

## [N-U65-003] Product Catalogue Organisation

WHAT: Each product can be assigned to one or more eCommerce categories, and has a sequence number that controls where it appears in the shop grid. Assigning a category automatically publishes the product. Variant URLs include the variant's attribute selections as query parameters.

WHY: Categories let customers browse by topic. Display sequence lets store owners curate the order of products on the page. Consistent variant URLs support sharing and bookmarking specific configurations.

BUSINESS RULE: New products default to a sequence higher than all existing products so they appear at the end of the grid until manually repositioned. Products gain GiST trigram database indexes on their names and descriptions to support fast fuzzy search.

STATE: Category assignments and sequence values are stored on the product record.

---

## [N-U65-004] Shopping Cart Mechanics

WHAT: The cart is a draft order held in the customer's session. Adding a product either increments an existing matching line or creates a new one. Updating a line quantity replaces the quantity entirely. Delivery and display-only lines are excluded from the visual cart. Combo products require all component slots to be filled before the line is accepted.

WHY: A session-based cart allows anonymous customers to shop without signing in. Line merging prevents duplicate entries for the same product. Quantity warnings let the customer know when stock limits are reached.

BUSINESS RULE: Only whole-number quantities are allowed in the cart by default. Optional and linked products (accessory items, combo components) are added as child lines linked to the parent. If a combo component is unavailable, the entire combo line is removed.

STATE: The cart is a draft order that can be abandoned or confirmed. Warnings from stock or quantity constraints are stored per line.

---

## [N-U65-005] Checkout Flow and Order Progression

WHAT: The checkout page validates the cart state before showing address and delivery options. The system checks that the order exists, is in draft, and has at least one item. When the cart contains only service products, the delivery step is automatically skipped. An abandoned cart is flagged when a draft order remains inactive beyond a configurable time limit.

WHY: A validated checkout prevents partial orders and user confusion. Skipping the delivery step for services removes unnecessary friction. Abandoned cart detection enables recovery email campaigns.

BUSINESS RULE: The cart must be in draft and non-empty to proceed to checkout. Orders older than the configured abandonment window with a real customer (not the public guest user) and at least one product line are marked as abandoned. A shipping error is raised when no delivery method is available for the destination address.

STATE: The current checkout step and last order id are tracked in the session. Delivery methods are resolved and set on the order at checkout time.

---

## [N-U65-006] Payment Transaction and Validation

WHAT: A payment transaction is created for the order amount and linked to the order. A database lock is held during transaction creation to prevent two simultaneous payments. Saved payment tokens are suppressed for express checkout. After the payment provider responds, the system validates the transaction state; zero-amount orders are confirmed directly without a provider.

WHY: The row lock prevents double charges when a customer clicks Pay twice. Suppressing tokens in express checkout avoids unintended recurring charges. Zero-amount orders need a confirmation path that does not require a payment provider.

BUSINESS RULE: The submitted payment amount must match the order total at the moment of transaction creation. If the amounts differ (cart updated while payment page was open), a validation error is returned. If the order was already paid, a user-facing error prevents a second charge. After successful validation, the cart session is cleared and the customer is redirected to the confirmation page.

STATE: The active transaction id is stored in the session. Confirmed payment triggers cart session cleanup.

---

## [N-U65-007] Order Confirmation and Stock Dispatch

WHAT: When a cart is confirmed, the responsible salesperson is assigned automatically. A confirmation email is sent. Connected warehouse management then launches stock reservation and procurement orders for all storable products. The order's company defaults to the website's company when not otherwise specified.

WHY: Automatic salesperson assignment ensures follow-up accountability without manual work. Stock rules ensure physical fulfilment begins immediately after the customer pays.

BUSINESS RULE: The salesperson assignment uses elevated permissions internally so the confirmation notification is sent from the system bot rather than the customer or public user. Stock rules are triggered for all confirmed lines, creating the necessary warehouse movements.

STATE: The order moves from draft to confirmed (sale) state, at which point it is no longer editable as a cart.

---

## [N-U65-008] Address Autocomplete for Checkout

WHAT: The checkout address form can provide Google Places suggestions as the customer types, reducing entry errors and speeding up completion.

WHY: Accurate address entry reduces failed deliveries and reduces customer support calls about wrong addresses.

BUSINESS RULE: The Google Places API key is stored per website so each storefront can use its own key. A safe Boolean check lets templates show or hide the autocomplete feature without exposing the raw key. For internal users (employees), the key can be drawn from a shared company configuration.

STATE: The API key is a site-level configuration value set by the store administrator.

---

## [N-U65-009] Click and Collect (In-Store Pickup)

WHAT: Customers can choose to collect their order from a physical store location. Each warehouse can define opening hours. When a pickup location is selected, the order's fulfilment warehouse and fiscal position are fixed to that location's data.

WHY: Click and collect increases store footfall and provides customers an alternative to home delivery. Fixing the warehouse ensures stock is reserved from the correct location. Fixing the fiscal position ensures the correct tax treatment for the pickup region.

BUSINESS RULE: The warehouse is computed from the pickup location data and not recomputed if the carrier remains in-store. Switching to a non-in-store carrier triggers recomputation of both warehouse and fiscal position. Geocoordinates for warehouses are fetched once and cached; failed geocoding writes sentinel values to prevent repeated API calls.

STATE: Pickup location data is stored on the order alongside the carrier. Opening hours are a resource calendar linked to the warehouse record.

---

## [N-U65-010] Gelato Print-on-Demand Integration

WHAT: Products connected to the Gelato print-on-demand service must have all print images defined before they can be published to the shop. When a product sync with Gelato adds new images, the product is automatically unpublished for review. Carts cannot mix Gelato products with non-Gelato storable products because they require separate fulfilment streams. Express checkout is disabled for orders containing Gelato products.

WHY: Gelato products require specific print-ready artwork. Auto-unpublishing on sync prevents customers from ordering with incomplete or outdated artwork. Mixed-cart blocking ensures each order can be routed to a single fulfilment provider.

BUSINESS RULE: A Gelato product cannot be published unless all required print images are present. A Gelato product in a cart blocks express checkout, requiring the full checkout flow.

STATE: The product's published state is managed automatically by sync events. Cart validation enforces single-fulfilment-type rules at line addition time.

---

## [N-U65-011] Coupons, Promotions and Loyalty on the Website

WHAT: Loyalty and promotion programs can be flagged as available on the website. Coupon codes can be distributed via URLs; when a customer opens their cart, the code from the URL is auto-applied. Qualifying rewards for programs with a single reward are claimed automatically without customer action.

WHY: Automated coupon application reduces friction for promotional campaigns. Auto-claiming rewards keeps the customer experience seamless. The website flag prevents internal-only programs (such as B2B contracts) from leaking onto the public shop.

BUSINESS RULE: Only loyalty programs with the website-available flag are applied to web cart orders. Programs with multiple reward options require the customer to select a reward rather than auto-claiming. Dismissed auto-rewards are tracked per order so they are not repeatedly offered.

STATE: The pending coupon code is held in the session until the cart is loaded. Discount lines are applied as order lines on the sale order.

---

## [N-U65-012] Kit Product Availability

WHAT: When the shop includes products that are assembled from components (kits), available quantity is computed by exploding the kit's recipe and checking how much component stock remains after accounting for all kit lines already in the cart.

WHY: A simple product-level stock check is insufficient for kits because components may be shared across multiple kit products. The cross-kit calculation prevents the shop from displaying availability that would lead to fulfilment failures.

BUSINESS RULE: The kit availability calculation uses the full bill-of-materials recipe to find each component and its required quantity per kit. The maximum number of kits that can be sold is limited by the most-constrained component. Components shared between multiple kit types in the same cart are deducted accordingly.

STATE: Availability is computed on demand per cart state. The calculation does not modify any stock record.

---

## [N-U65-013] Course Sales via the Shop

WHAT: Online courses can be sold through the shop by linking a course to a purchasable product. When a customer buys the product, they are automatically enrolled in the course on order confirmation. Only one copy of a course can be purchased per cart.

WHY: Selling courses through the existing shop reuses the checkout, payment and order infrastructure without requiring a separate purchase system. Automatic enrolment on confirmation ensures no manual steps are needed to grant access.

BUSINESS RULE: A course product is limited to a quantity of one per cart line. On order confirmation, the buyer's partner is added as a member of every course channel linked to purchased products. Course products may have a zero price without triggering the zero-price block, enabling free courses.

STATE: Enrolment is granted at confirmation time. Revenues per course are tracked via the sales report.

---

## [N-U65-014] Stock Availability Display

WHAT: The shop can show customers when a product is low in stock or sold out. A configurable threshold determines when the low-stock indicator appears. A separate setting controls whether customers can purchase a product that has no stock.

WHY: Transparency about availability manages customer expectations and reduces post-order disappointment. Preventing out-of-stock purchases avoids fulfilment failures for businesses that cannot backorder.

BUSINESS RULE: A product is considered sold out only when all its variants have zero free stock and the out-of-stock orders setting is disabled. Stock availability is checked at line update time; exceeding available quantity sets a warning on the cart line. Availability is scoped to the shop's configured warehouse.

STATE: Stock levels are live data from the warehouse. Warnings are stored on cart lines and cleared on subsequent updates.

---

## [N-U65-015] Event Registration on the Website

WHAT: Events can be published to the website. Customers register by selecting tickets and providing attendee details. The system verifies seat availability before creating registrations. A recaptcha check protects the confirmation endpoint. Registrations are linked to the website visitor record for tracking.

WHY: Online event registration eliminates manual sign-up sheets and prevents overbooking. Visitor linking enables event-triggered marketing actions.

BUSINESS RULE: Seat availability is checked at both the form display step (to show accurate counts) and again at confirmation submission (to catch concurrent registrations). Per-order ticket limits are enforced. Failed captcha redirects back to the registration page with an error code rather than silently dropping the submission.

STATE: Registrations are created as draft attendee records. The registration success page is accessible only to the visitor who created the records.

---

## [N-U65-016] Event Booth Registration and Sale

WHAT: Events can offer booth spaces for exhibitors. Booths are presented on a dedicated sub-page. Customers select booths, fill in contact details, and complete a registration. Paid booths are processed through the standard shop checkout. Each booth occupies exactly one order line and cannot be quantity-adjusted. Booths may be offered at zero price without triggering the zero-price sale restriction.

WHY: Booth registration through the event website keeps all event management in one system. Using the standard checkout for paid booths reuses existing payment infrastructure.

BUSINESS RULE: The booth sub-menu appears only when the event type or explicit toggle enables it. Only one booth product may appear per cart line; duplicates replace rather than accumulate. When an event is duplicated, booth menus are re-parented under the new event's navigation structure.

STATE: Selected booths are held in a pending state on the order line until payment is confirmed.

---

## [N-U65-017] CRM Lead Creation from Event Registrations

WHAT: Attending an event can automatically create a CRM sales lead. When the registration came through the website, the lead is enriched with the website visitor record and the visitor's language. Registration form answers are appended to the lead description.

WHY: Event registrations are a strong sales signal. Capturing the visitor and language enables personalised follow-up. Form answer data provides conversation context for the sales team.

BUSINESS RULE: Lead creation is governed by lead generation rules defined on the event type. The website extension adds visitor and language data to the lead values computed by the base lead rule logic.

STATE: Leads are created asynchronously when the lead generation rule triggers on registration state changes.

---

## [N-U65-018] Ticket Sales and Checkout Integration for Events

WHAT: When event tickets have a price, the registration flow adds them to the shop cart and routes the customer through the standard checkout. Free-ticket registrations bypass the cart entirely. On the confirmation page, the purchased events and attendee records are shown. At payment time, seat availability is re-verified to prevent overselling. Different ticket types and time slots each occupy a separate cart line.

WHY: Routing paid tickets through the shop cart reuses payment providers, address management, and order history. Re-verification at payment time catches concurrent bookings that passed the initial check.

BUSINESS RULE: A pricelist item with a minimum quantity setting does not apply to event ticket products, because each ticket is always quantity 1. When a paid-ticket order contains only zero-value tickets, the order is auto-confirmed without payment. Seat limits per order are enforced both at form submission and at payment.

STATE: Ticket registrations move from draft to confirmed when payment is processed or when the order is auto-confirmed for free tickets.

---

## [N-U65-019] Track Quizzes for Event Sessions

WHAT: Sessions within an event can have an associated quiz. Attendees submit answers and receive immediate feedback on correctness and points earned. Completed quizzes cannot be resubmitted unless the quiz is configured as repeatable or the user is an event manager.

WHY: Quizzes gamify learning within events and drive engagement. Immediate feedback improves the learning experience. The repeat restriction maintains the integrity of leaderboard scores.

BUSINESS RULE: Quiz points are recorded per visitor per track. Once marked complete, resubmission is blocked unless the quiz allows multiple attempts. Event managers can always reset quizzes for testing.

STATE: Completion status and point totals are stored on the visitor-track record, updated atomically on submission.

---

## [N-U65-020] Website Newsletter Subscription

WHAT: Website pages can include a subscription block that allows visitors to sign up for a mailing list. Existing subscribers see their status reflected immediately. Submitting the form creates a mailing contact and list subscription, or re-activates an opted-out one. The subscribed address is stored in the session so the form stays pre-filled on return visits.

WHY: In-page subscription blocks convert casual readers into addressable marketing contacts. Session persistence reduces friction for repeat visitors.

BUSINESS RULE: A recaptcha check gates the subscription endpoint to prevent bot submissions. If the contact already exists but has opted out, the opt-out is reversed rather than creating a duplicate record. Unsubscription is handled via a one-click endpoint in outgoing email, which sets the opt-out flag without requiring the customer to log in.

STATE: Subscription state is stored on the mailing contact record. The current email is stored in the session until cleared.

---

## [N-U65-021] Mass Mailing Test Coverage

WHAT: A dedicated test module verifies the core mass mailing behaviour, including that emails are sent with the correct author identity, link tracking works, and blacklist enforcement operates correctly.

WHY: Mass mailing involves sensitive behaviour around identity, deliverability, and opt-out compliance. Separate test coverage in a module that can install alongside other test fixtures allows thorough integration testing.

BUSINESS RULE: Test modules are hidden from the app list and categorised as testing utilities. They may define their own test data models without polluting the production schema.

STATE: Tests run post-install. They do not alter production configuration.

---

## [N-U65-022] Website Module Integration Tests

WHAT: A test module that depends on a broad set of website add-ons verifies that the combined installation works correctly. It tests image editing through the website builder with different user roles.

WHY: Individual modules may function correctly alone but fail when installed together. Cross-module integration tests catch regressions introduced by module interactions.

BUSINESS RULE: The test module is hidden and categorised as a test utility. It relies on a default theme being installed, reflecting a realistic website deployment.

STATE: Tests run after installation of all dependencies. They test live HTTP endpoints.

---

## [N-U65-023] Full eLearning Certification Flow Tests

WHAT: A test module exercises the complete end-to-end flow of purchasing a course, completing a certification survey, and receiving the course completion status.

WHY: The course purchase flow spans multiple modules. End-to-end UI tests confirm that the integration between shop, survey, and eLearning works correctly in a real browser session.

BUSINESS RULE: The test requires specific demo data including a survey with certification scoring and a course configured for paid enrolment.

STATE: Tests are tagged for post-install execution and run in a real browser against the installed Odoo instance.
