# U66 — Neutral Knowledge: IoT, POS Restaurant, Mass Mailing Extensions

**Unit:** U66  
**Research date:** 2026-10-02  

---

## [N-U66-001] IoT Box Image Build Tools

WHAT: A non-installable module containing shell scripts and configuration files used to produce a deployable operating system image for the IoT Box hardware device.

WHY: The IoT Box device needs a purpose-built embedded system image; this module provides the tooling to assemble that image but does not add any Odoo application logic.

BUSINESS RULE: This module is explicitly marked as non-installable, meaning it is never deployed to a running Odoo database — its use is limited to offline build processes.

STATE: Build-time utility only.

---

## [N-U66-002] Hardware Proxy Framework

WHAT: A non-installable driver framework that runs on the IoT Box, providing the web server and communication layer that allows the Odoo POS and other Odoo applications to communicate with physical hardware peripherals.

WHY: Hardware devices such as printers, scales, and payment terminals must communicate through a local proxy because browser security prevents direct hardware access from web pages.

BUSINESS RULE: The framework itself contains no device-specific logic; actual device support requires separate driver modules that register themselves automatically.

STATE: Runtime on IoT Box device only; never installed in a standard Odoo database.

---

## [N-U66-003] IoT Driver Base Type

WHAT: A base type and registration mechanism that every hardware device driver inherits from. Each driver runs as a background thread, maintains device identity information, and dispatches named commands to registered handler methods.

WHY: Running each device as its own thread allows simultaneous operation of many hardware peripherals without blocking. The action deduplication cache prevents problems caused by duplicate command deliveries.

BUSINESS RULE: Printer and payment terminal devices manage their own event notifications; all other device types notify through the central event manager automatically.

STATE: Core framework; always active when the IoT Box is running.

---

## [N-U66-004] IoT Interface Layer

WHAT: An abstract interface type that polls the operating system for newly connected or removed hardware devices on a specific bus type (USB or serial), then matches each device to an appropriate driver.

WHY: Hardware can be connected or disconnected at any time; the polling loop detects these changes and starts or stops the corresponding driver threads.

BUSINESS RULE: Unsupported devices (those with no matching driver) are tracked in a separate registry and reported to the Odoo backend so users know what is connected even if not fully supported.

STATE: One interface instance runs per connection type.

---

## [N-U66-005] IoT Printer Driver Base

WHAT: An abstract base type for receipt and label printers, providing shared logic for formatting receipts as raster or column-mode images in ESC-POS or Star protocols, printing status pages, and triggering cash drawer openings.

WHY: Most POS printers use one of two widely-adopted command protocols. Sharing the formatting and cashbox logic avoids duplication across platform-specific driver implementations.

BUSINESS RULE: The printer name may contain embedded configuration tokens (for example, a scale percentage or image column mode flag) that control image rendering without requiring a separate configuration interface.

STATE: Abstract; must be extended for each operating system platform.

---

## [N-U66-006] IoT Box Cloud Pairing

WHAT: A background connection manager that registers the IoT Box with a Odoo-operated cloud proxy to obtain a short-lived pairing code, then polls the proxy until a database administrator enters the code and associates the IoT Box with an Odoo database.

WHY: The IoT Box cannot be given a fixed database URL at manufacturing time; cloud-mediated pairing allows zero-configuration deployment in customer environments.

BUSINESS RULE: The polling interval grows gradually from roughly 15 seconds to roughly 40 seconds to avoid overloading the proxy service. Pairing codes expire if unused.

STATE: Active only when no Odoo server URL is currently configured on the device.

---

## [N-U66-007] IoT Event Notification

WHAT: A central event manager that receives state-change notifications from any device driver and distributes them to waiting long-poll sessions and WebRTC connections.

WHY: The POS interface needs to be notified immediately when a device (such as a card reader or scale) has new data. Long-polling and WebRTC provide two transport options for different deployment setups.

BUSINESS RULE: Each device event includes a timestamp and device identifier; sessions subscribe by device identifier or device type.

STATE: Always running when the IoT Box service is active.

---

## [N-U66-008] Restaurant Floor and Table Management

WHAT: A set of models that represent the physical layout of a restaurant: floors (rooms), tables on those floors, and their visual properties (position, size, shape, color). These models are loaded into the POS session so the cashier can interact with a graphical floor plan.

WHY: Restaurant operators need to assign orders to specific tables, track how many guests are seated, and view the status of all tables at a glance without navigating complex menus.

BUSINESS RULE: A floor cannot be deleted while an open POS session references it. A default floor and table are created automatically when a restaurant POS configuration is first set up. Floor modifications are also blocked while a session is open.

STATE: Active in any POS configuration with the restaurant module enabled.

---

## [N-U66-009] Restaurant Order Table Assignment

WHAT: An extension of the POS order model that links each order to a specific table and tracks the number of guests. When a new order is opened for a table that already has a draft order, the system matches the existing order rather than creating a duplicate.

WHY: In a restaurant, one table typically has one active order throughout the meal. The deduplication logic prevents staff from accidentally creating multiple orders for the same table.

BUSINESS RULE: Table assignment and customer count are stored read-only on the order after creation.

STATE: Active when restaurant mode is enabled.

---

## [N-U66-010] Kitchen Course Management

WHAT: A model that groups order lines into sequenced courses and tracks whether each course has been sent (fired) to the kitchen, along with the firing timestamp. Order lines are individually linked to their course.

WHY: Multi-course meals require sending food preparation instructions to the kitchen in stages rather than all at once. The fired timestamp provides a record for order timing and kitchen display systems.

BUSINESS RULE: The firing timestamp is set automatically when a course is first marked as fired and cannot be reset.

STATE: Active when the restaurant module is enabled.

---

## [N-U66-011] Restaurant Adyen Tip Integration

WHAT: An extension of the standard Adyen payment integration that adds support for the American-style tip-after-payment workflow: the card is pre-authorized at the order amount, and the actual capture occurs later once the customer adds a tip.

WHY: In many markets, restaurant customers add a tip on the receipt after the meal rather than at the point of payment. This requires a separate capture step after authorization.

BUSINESS RULE: Two additional Adyen API endpoints (adjust authorization and capture) are activated. When tip-after-payment is not configured, Adyen payments are captured immediately at order completion.

STATE: Active when both the restaurant and Adyen modules are installed.

---

## [N-U66-012] Restaurant Stripe Tip Integration

WHAT: A JavaScript-only bridge module that enables tip-after-payment behavior for Stripe terminals in restaurant configurations.

WHY: Same business need as the Adyen restaurant module — restaurant customers in some markets add tips after authorization.

BUSINESS RULE: No server-side Python changes; all behavior is implemented in the browser-side POS application.

STATE: Auto-installs when both Stripe and restaurant modules are present.

---

## [N-U66-013] Restaurant Loyalty Bridge

WHAT: A JavaScript-only auto-install module that corrects POS loyalty program behavior in restaurant configurations.

WHY: When restaurant and loyalty features are both active, certain interactions require coordination that neither module handles independently.

BUSINESS RULE: No server-side Python changes; correction logic is entirely in the browser-side POS application.

STATE: Auto-installs when both restaurant and loyalty modules are present.

---

## [N-U66-014] Adyen Card Terminal Payment

WHAT: An integration that routes POS card payments through an Adyen physical payment terminal using the TAPI cloud protocol. The Odoo server acts as a proxy for all communication to avoid browser cross-origin restrictions.

WHY: Card terminals from Adyen use a cloud-based API that requires server-side authentication; browser-to-terminal direct communication is not possible due to CORS restrictions.

BUSINESS RULE: Every payment request is HMAC-signed with four identifiers; the callback validates this signature before accepting the response. Responses are buffered in a single field and broadcast via the POS notification bus.

STATE: Active when the Adyen module is installed and a terminal identifier is configured.

---

## [N-U66-015] Cashdro Automatic Cash Handling

WHAT: An integration that connects the POS to a Cashdro automatic cash dispensing and accepting machine using IP-based communication, with optional local network access mode.

WHY: Cashdro machines handle coin and banknote counting and dispensing automatically, reducing cashier errors and theft risk.

BUSINESS RULE: IP address, username, and password are stored directly on the payment method record and sent to the POS client for use in browser-to-device communication.

STATE: Active when the module is installed and credentials are configured.

---

## [N-U66-016] Cashmatic Automatic Cash Handling

WHAT: An integration connecting the POS to a Cashmatic automatic cash machine, following the same credential and local network access pattern as the Cashdro integration.

WHY: Different markets use different cash machine brands; parallel integration coverage supports broader hardware compatibility.

BUSINESS RULE: Same local network access flag and IP credential pattern as Cashdro; the two integrations are structurally identical.

STATE: Active when the module is installed.

---

## [N-U66-017] Glory Automatic Cash Handling

WHAT: An integration that connects the POS to a Glory automatic cash machine via WebSocket, using an IP address, username, and password stored on the payment method.

WHY: Glory machines are widely used in high-volume retail and restaurant environments for automated cash management.

BUSINESS RULE: Communication uses a WebSocket connection rather than HTTP, reflecting the Glory device's native protocol.

STATE: Active when the module is installed.

---

## [N-U66-018] DPO Pay Card and Mobile Money Terminal

WHAT: An integration for DPO Pay payment terminals used primarily in African markets, supporting both card payments and Mobile Money (M-Pesa and Airtel). The integration automatically refreshes the bearer token when it expires.

WHY: African markets often require support for mobile wallet payments alongside card terminals. DPO Pay provides a unified terminal solution for both payment types.

BUSINESS RULE: The bearer token is stored and auto-refreshed to keep the payment flow working without manual intervention. Chain-ID is an additional required header that identifies the merchant's network segment.

STATE: Active when the module is installed and credentials are configured.

---

## [N-U66-019] iMin ePOS Printer Integration

WHAT: An integration that enables iMin brand ePOS printers to work directly with the POS browser application without requiring an IoT Box intermediary.

WHY: iMin produces integrated POS terminals with built-in printers; their devices expose a JavaScript API that allows direct browser communication, eliminating the need for the IoT proxy.

BUSINESS RULE: A bundled third-party JavaScript library provides the device API. The cash drawer display is also enabled via a settings extension.

STATE: Active when the module is installed.

---

## [N-U66-020] Safaricom M-Pesa Payment Integration

WHAT: An integration for Safaricom M-Pesa payments in Kenya, supporting two modes: STK Push (a push notification sent to the customer's phone) and Lipa na M-Pesa (a till-number-based C2B payment with QR code support).

WHY: M-Pesa is the dominant payment method in Kenya and neighboring countries; POS support is essential for operators in those markets.

BUSINESS RULE: Business short codes are stored as "shortcode-tillnumber" pairs. C2B webhook URLs must be registered with Safaricom once per payment method at creation time. All callback payloads are signed with a time-limited hash to prevent replay attacks. A dedicated transaction model stores inbound C2B payments until they are matched to POS orders.

STATE: Active when the module is installed and credentials are configured.

---

## [N-U66-021] POS Order Discounts

WHAT: A module that allows cashiers to apply a configurable percentage discount to an entire POS order using a dedicated discount product. The discount percentage defaults to 10%.

WHY: Promotional and manual discounts are common in retail; a one-click discount button speeds up the checkout process.

BUSINESS RULE: A discount product must be configured before a session can be opened with the discount feature enabled. The discount product is always included in the product catalog loaded for the POS session. Discount lines in accounting entries are correctly identified by checking the linked POS order's discount product.

STATE: Active when the module is installed and discount product id is set.

---

## [N-U66-022] POS and Sale Order Loyalty Bridge

WHAT: A bridge module that extends sale order line data retrieval to include the loyalty reward identifier, enabling loyalty rewards created via sale orders to be visible and applicable in POS sessions.

WHY: Loyalty rewards may originate from e-commerce or sales orders; the bridge ensures those rewards are available when the customer completes their purchase at the POS.

BUSINESS RULE: The reward id field is appended to the sale order line fields returned to the POS client.

STATE: Auto-installs when both POS Sale and POS Loyalty modules are present.

---

## [N-U66-023] POS Event Ticket Sales

WHAT: A bridge module that updates event registration status based on the linked POS order state, so that selling an event ticket through the POS correctly marks the registration as sold.

WHY: Event registrations sold through the POS need to be reflected in the event management system so organizers can track attendance correctly.

BUSINESS RULE: A POS order in paid, done, or invoiced state marks the linked registration as sold and open; any other state keeps the registration in draft with to pay status.

STATE: Auto-installs when both POS Event and POS Sale modules are present.

---

## [N-U66-024] Self-Order Online Payment

WHAT: A bridge module enabling customers to pay for the record-order mobile orders using an online payment provider (such as a payment gateway), with automatic receipt delivery and payment status notifications after confirmation.

WHY: Mobile the record-ordering requires a customer-facing payment flow that works on the customer's device without cashier involvement.

BUSINESS RULE: The configured online payment method must have at least one published payment provider supporting the POS currency. After payment confirmation, the receipt is sent automatically and the POS session is notified.

STATE: Auto-installs when both online payment and the record-order modules are present.

---

## [N-U66-025] Self-Order Adyen Kiosk Payment

WHAT: An extension that enables Adyen physical terminals to accept payments from kiosk the record-order sessions. The kiosk builds and submits the Adyen payment request server-side; the callback identifies the correct the record-order order by ID.

WHY: Kiosk terminals require a fully automated payment flow with no cashier involvement; the server-side request submission handles authentication and CORS issues.

BUSINESS RULE: The the record order id is embedded in the Adyen SaleToAcquirerData metadata so the callback can locate the correct order when the terminal completes the payment.

STATE: Auto-installs when both Adyen and the record-order modules are present.

---

## [N-U66-026] Self-Order Stripe Kiosk Payment

WHAT: An extension enabling Stripe terminals to process payments for kiosk the record-order sessions, delegating to the existing Stripe payment intent mechanism.

WHY: Operators who use Stripe rather than Adyen also need kiosk terminal support for the record-order.

BUSINESS RULE: Same domain filtering pattern as the Adyen the record-order extension.

STATE: Auto-installs when both Stripe and the record-order modules are present.

---

## [N-U66-027] Self-Order Viva.com Kiosk Payment

WHAT: An extension enabling Viva.com terminals to process payments for kiosk the record-order sessions. Payments are initiated server-side; the kiosk polls a dedicated endpoint for payment status and the order is automatically finalized when payment succeeds.

WHY: Viva.com is a major payment provider in Southern Europe; kiosk operators using Viva terminals need the same unattended payment capability as Adyen and Stripe users.

BUSINESS RULE: Amount must be expressed in minor currency units (multiplied by currency decimal places). The session identifier is a composite of the order UUID and a random UUID hex to ensure uniqueness.

STATE: Auto-installs when both Viva.com and the record-order modules are present.

---

## [N-U66-028] Self-Order Kiosk CRM Sales Team

WHAT: A bridge module that automatically assigns a dedicated CRM sales team to the POS configuration when kiosk mode is enabled, used for attributing kiosk-sourced revenue in sales reporting.

WHY: Kiosk orders may need to be attributed separately from cashier-assisted orders for performance tracking and commission purposes.

BUSINESS RULE: The sales team is assigned only if no team is currently configured; an existing setting is never overridden.

STATE: Auto-installs when both POS Sale and the record-order modules are present.

---

## [N-U66-029] HR Restaurant Integration

WHAT: A JavaScript-only bridge module that coordinates employee login (clock-in) behavior with the restaurant floor plan view, ensuring that HR-related employee selection flows work correctly alongside the table management interface.

WHY: Restaurants typically require each waiter to log in individually; the HR module provides employee-based POS login, and this bridge ensures the floor plan screen behaves correctly after employee identification.

BUSINESS RULE: No server-side Python changes; all adaptations are implemented in the POS browser application.

STATE: Auto-installs when both POS HR and POS Restaurant modules are present.

---

## [N-U66-030] Mass Mailing CRM SMS Split-Variant Testing

WHAT: An extension that adds "Leads" as an available winner metric for SMS split-variant test campaigns, allowing marketers to determine the winning variant based on the number of CRM leads generated.

WHY: Lead generation is a key objective for B2B SMS campaigns; having a lead-count metric as a winner criterion aligns the campaign evaluation with business outcomes.

BUSINESS RULE: The selection option is added to the utm campaign model's ab testing sms winner selection field.

STATE: Auto-installs when both CRM and SMS mass mailing modules are present.

---

## [N-U66-031] Mass Mailing to Event Track Speakers

WHAT: A bridge module that enables mass email campaigns to be sent directly to event track speakers (presenters). An action button on the event form opens a pre-configured mass mailing targeting that event's non-cancelled tracks.

WHY: Conference and event organizers frequently need to communicate with all speakers in bulk; a dedicated action removes the need to manually set up the mailing each time.

BUSINESS RULE: The default domain for speaker mailings excludes tracks in cancelled stages. The mailing model is pre-set to event track.

STATE: Auto-installs when both website event track and mass mailing modules are present.

---

## [N-U66-032] Mass Mailing SMS to Event Track Speakers

WHAT: A bridge module that overrides the speaker mass mailing action to open the combined email and SMS mailing form, enabling operators to send SMS campaigns to event speakers alongside or instead of email campaigns.

WHY: SMS has higher open rates and is preferred for urgent communications; event organizers should be able to reach speakers via SMS when needed.

BUSINESS RULE: The override forces the mixed email and SMS form view rather than the default email-only view.

STATE: Auto-installs when mass mailing, mass mailing sms, sms, and website event track are all present.

---

## [N-U66-033] Mass Mailing Sale Order SMS Split-Variant Testing

WHAT: An extension that adds two sale-order-specific winner metrics for SMS split-variant test campaigns: number of quotations generated and total revenues invoiced.

WHY: Sales-focused SMS campaigns should be evaluated on commercial outcomes (quotations and revenue) rather than generic engagement metrics.

BUSINESS RULE: Both selection options are appended to the utm campaign model's existing SMS winner selection choices.

STATE: Auto-installs when both sales and SMS mass mailing modules are present.

---

## [N-U66-034] Mass Mailing Email Themes

WHAT: A data-only module that provides a library of professionally designed email templates and attached style resources for use in mass mailing campaigns.

WHY: Marketers need visually attractive email designs without requiring HTML or CSS skills; ready-made templates accelerate campaign creation.

BUSINESS RULE: No server-side Python model changes; all content is delivered via XML data files and static attachment records.

STATE: Auto-installs with the mass mailing module.

