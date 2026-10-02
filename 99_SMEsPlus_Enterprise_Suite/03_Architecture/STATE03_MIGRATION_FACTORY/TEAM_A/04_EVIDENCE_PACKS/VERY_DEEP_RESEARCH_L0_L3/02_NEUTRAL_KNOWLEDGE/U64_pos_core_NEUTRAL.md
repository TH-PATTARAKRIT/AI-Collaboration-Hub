# U64 — POS Core Neutral Knowledge
**Status:** DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

---

## [N-U64-001] Session Opening Gate

WHAT: A point-of-sale session acts as an operational gate that must be explicitly opened before any sales can be recorded. The system enforces that only one active session may exist per terminal configuration at a time, preventing conflicts. A rescue session variant exists for orphaned orders but is excluded from this uniqueness rule.

WHY: This design protects accounting integrity by tying all sales, payments, and journal entries to a single auditable session record. The system also validates that the session start date does not fall inside a locked accounting period before allowing it to open.

BUSINESS RULE: Exactly one non-rescue session may be open per terminal at any time. Opening a second session while one is active raises an error. The session starting date must not precede any active accounting lock date on the related journal's company.

---

## [N-U64-002] Session Closing Gate

WHAT: Closing a session is a two-stage process. First the operator signals intent to close, which moves the session to a closing-control state and verifies that no orders remain open. Second, the system validates the session by checking that all invoices are posted, then posts the accounting entry and marks the session as closed and posted.

WHY: The two-stage close ensures that no transactions are missed and that the accounting record produced is balanced and complete. Draft orders or unposted invoices left open at closing time indicate unfinished business that must be resolved before the books can be updated.

BUSINESS RULE: A session cannot be closed while any orders are still in draft status. A session cannot be closed while any linked invoice is in a non-posted state. If cash counting is enabled, a cash register count must be completed before the session can proceed to final close.

---

## [N-U64-003] Session Accounting Entry Creation

WHAT: At the moment of session close, the system automatically creates a single accounting journal entry that summarises all sales, taxes, cash movements, bank payments, and customer-account receivables recorded during the session. Cash counting differences are posted as a separate gain or loss line. All receivable lines from invoiced orders are then reconciled against matching lines in the closing entry.

WHY: Concentrating all POS activity into one journal entry per session minimises the number of accounting records while preserving full traceability back to individual orders. Automatic reconciliation eliminates the need for manual matching of invoice payments against session lines.

BUSINESS RULE: The closing journal entry is created against the POS-specific accounting journal configured on the terminal. If a cash difference exists at close, the configured profit or loss account on the cash journal must be set; if it is missing, the system raises an error rather than posting an unbalanced entry.

---

## [N-U64-004] Session Data Loading

WHAT: When the operator opens the POS application, the server assembles a complete data bundle covering product catalogue, pricing, taxes, payment methods, customers, fiscal positions, and other reference data, and sends it to the terminal in a single load operation.

WHY: Loading all required data upfront allows the terminal to function offline or with intermittent connectivity, since it carries all the information needed to process orders and compute totals without round-tripping to the server on every transaction.

BUSINESS RULE: Extension modules may add their own reference data to the initial bundle by registering additional model names and fields. If access rights prevent loading a particular model, that model is skipped silently and an empty list is returned for it rather than blocking the entire load.

---

## [N-U64-005] Session Notifications and Recovery

WHAT: When a session transitions to the closed state, all connected devices receive a real-time bus notification identifying the device and session. A rescue session can be created automatically to capture orders that arrived after a session was unexpectedly closed.

WHY: Real-time notification ensures that all open terminals are immediately aware that a session has ended and can stop accepting new orders. The rescue mechanism prevents order loss in edge cases where a session closes while transactions are still in flight.

BUSINESS RULE: Rescue sessions are flagged at creation and excluded from the single-session-per-terminal constraint. They follow a simplified closing path that calculates their cash balance from payments plus the opening balance without a full cash-count screen.

---

## [N-U64-006] Order Processing Flow

WHAT: Orders submitted from the terminal are validated and persisted on the server through a defined sequence: the session is verified to be open, the order record is created or updated, payments are recorded, and the order transitions to a paid state. If the original session is already closed when an order arrives, the system redirects the order to the next open session on the same terminal configuration.

WHY: Server-side processing ensures that all orders are persisted under a valid accounting context and that totals are computed authoritatively rather than relying solely on client calculations.

BUSINESS RULE: If no open session exists when an order arrives for a closed session, the system raises an error rather than creating an orphaned order. Once an order is marked as paid, it triggers stock movement creation and, if configured, invoice generation.

---

## [N-U64-007] Multi-Company Isolation

WHAT: Every order, payment, and stock movement is explicitly associated with the company that owns the terminal configuration. When an order does not carry a company identifier, the system automatically assigns the company from the terminal configuration.

WHY: Explicit company assignment prevents transactions from being accidentally recorded under the wrong legal entity in multi-company deployments. All downstream computations for taxes, currencies, and accounts then run within the correct company context.

BUSINESS RULE: An order's company is derived from its terminal configuration if not otherwise specified. All accounting computations for that order must run within that company's context to ensure correct tax rates, accounts, and currency conversions are applied.

---

## [N-U64-008] Payment Validation

WHAT: When an order is marked as paid, the server independently verifies that the sum of payments received equals the order total within the allowed rounding tolerance. The server also recalculates the amount paid from the payment records, overriding the value submitted by the terminal.

WHY: Server-side payment verification prevents underpayment or manipulation of payment amounts by the client. Recalculating the paid amount from individual payment records rather than trusting the client total is a fundamental integrity control.

BUSINESS RULE: An order cannot transition to paid status if the payment amount differs from the order total by more than the configured cash-rounding tolerance. When a customer receives change, a separate change payment record is created against the cash method to record the returned amount.

---

## [N-U64-009] Terminal Configuration

WHAT: Each terminal has a configuration record that specifies the warehouse operation type for stock movements, the pricelists available to cashiers, the company it belongs to, and the payment methods accepted. Constraints prevent configuration from including payment methods, journals, or pricelists belonging to a different company or currency.

WHY: Centralising terminal behaviour in a configuration record makes it possible to manage multiple terminals with distinct settings from a single administration interface. Company and currency constraints prevent misconfiguration that would produce cross-company accounting errors.

BUSINESS RULE: All payment methods on a terminal configuration must belong to the same company as the configuration. All available pricelists must share the same currency as the terminal. If no payment methods are configured, the terminal cannot open a session.

---

## [N-U64-010] Payment Methods

WHAT: A payment method connects a terminal to an accounting journal and governs how payments are recorded in the books. The method's accounting type (cash, bank, or customer account) is derived from the linked journal. When a method is configured to identify customers, each payment produces a separate journal entry per customer rather than being aggregated. The customer-account type skips journal entry creation entirely, recording the receivable as an open payable.

WHY: Flexible payment method configuration supports terminals that accept cash, card, or credit-account payments within the same session, with each method flowing to the appropriate accounting journal. Per-customer splitting provides the detail needed for customer statement reconciliation.

BUSINESS RULE: Only cash or bank journals may be linked to a payment method. A payment using a method not listed on the terminal configuration is rejected at save time. Payment amounts on settled orders are locked and cannot be modified after posting.

---

## [N-U64-011] Custom Tax Formula Support

WHAT: When the accounting module for Python-formula taxes is installed alongside the point-of-sale module, the tax records sent to the terminal at startup include additional formula information that allows the terminal to evaluate complex tax rules locally.

WHY: Some tax regimes require computed amounts that depend on variables beyond price and quantity. Including the formula data in the initial load allows the terminal to compute these amounts in the browser without server round-trips on every line.

BUSINESS RULE: Python-formula tax details are only included in the terminal data bundle when the custom-tax module is installed; the base terminal module provides standard rate-based tax computation only.

---

## [N-U64-012] UBL Export for POS Orders

WHAT: When the UBL electronic document module is installed, POS orders can be exported as structured UBL 2.1 XML documents. The export assembles supplier information, customer details, payment terms, tax totals, and line items into a standard electronic invoice format.

WHY: UBL 2.1 is a widely adopted standard for electronic invoices. Enabling UBL export from the POS allows merchants to satisfy electronic-invoicing requirements in jurisdictions that mandate machine-readable invoice formats.

BUSINESS RULE: The UBL export is validation-checked before output; any constraint violations prevent the document from being produced. The export produces a single document per POS order containing all line items, taxes, and monetary totals.

---

## [N-U64-013] Event Ticket Sales at the Terminal

WHAT: When the event-sales module is installed, event tickets can be sold directly at the point of sale. Each sale line can carry a specific ticket type, and a registration record is created in the events system for each ticket purchased. The registration status tracks whether the associated order was cancelled or is fully paid.

WHY: Integrating event registration into the point of sale allows venues to sell tickets at a physical counter using the same checkout process as any other product, without a separate ticketing system.

BUSINESS RULE: Deleting a POS order line that sold an event ticket cascades to delete the linked registration record. Registration status is derived from the order state: a cancelled order results in a cancelled registration; a zero-total order treats the ticket as complimentary.

---

## [N-U64-014] Employee Login to the Terminal

WHAT: When the HR integration is installed, employees (rather than system users) can log in to the terminal using a barcode or a PIN. The server transmits only hashed versions of these credentials to the terminal, never the originals. Each employee can be assigned one of three permission levels that determine which terminal functions they can access.

WHY: Using employee-level login allows unlimited staff members to transact on a single shared terminal while maintaining individual accountability. Hashing credentials before transmission protects them from interception or storage in browser memory.

BUSINESS RULE: SHA-1 hashed credentials are sent to the terminal at session open; the terminal compares hashes of what the employee types rather than contacting the server for each login. Employees cannot be deleted while they are linked to an active terminal session.

---

## [N-U64-015] Loyalty, Coupons, and Gift Cards

WHAT: When the loyalty module is installed, the terminal can apply loyalty programs, accept coupon codes, and redeem gift card balances during checkout. The server validates all point changes and coupon codes submitted with an order before allowing payment to proceed. A history of point additions and redemptions is recorded per loyalty card.

WHY: Server-side validation prevents the terminal from applying discounts that exceed available point balances or using coupon codes that have already been redeemed. The history trail provides an auditable record of all loyalty activity.

BUSINESS RULE: A coupon submitted with an order must exist in the database, must belong to an active program, and must have sufficient points for the redemption. New coupon codes must be unique across all existing loyalty cards. If any validation fails, the order is blocked with a specific error message.

---

## [N-U64-016] Manufacturing Kit Cost Tracking

WHAT: When the manufacturing module is installed, POS orders for products sold as kit bundles (phantom bills of materials) are tracked at the component level for stock and cost purposes. Stock movements are created for the individual kit components rather than the assembled product, and cost calculations sum the component costs proportionally.

WHY: Phantom kits are not physically assembled; their components are picked directly. Recording stock movements and costs at the component level keeps inventory records accurate and ensures that the gross margin reported for kit sales reflects actual component costs.

BUSINESS RULE: When a POS order line contains a kit product, the system explodes the bill of materials to identify components and creates stock movements for those components. The Anglo-Saxon cost for the line is computed by weighting each component's cost by its proportion in the kit.

---

## [N-U64-017] Online Payment at the Terminal

WHAT: When the online payment module is installed, payment methods of an online type can be configured on a terminal. These methods direct customers to a web payment page hosted by a payment provider. Online payments are accumulated in a separate receivable bucket during session close and reconciled against the account payment records created by the provider's confirmation.

WHY: Online payment methods allow customers to pay by credit card or digital wallet through a provider-hosted page, avoiding the need for physical card terminals for every station. Separating online receivables from cash and bank receivables keeps the closing entry clear about the origin of each payment.

BUSINESS RULE: An online payment method can specify which providers are accepted; if none are specified, all published and active providers are allowed. Customer identification may be required by certain providers, which is enforced at checkout.

---

## [N-U64-018] Repair Order Integration

WHAT: When the repair module is installed, sale order lines that originate from a repair order are flagged as repair lines. Stock movements for those lines are excluded from the normal POS stock-picking creation to avoid counting the same goods movement twice.

WHY: Repair orders generate their own stock movements when parts are consumed or products are returned. If the POS also created stock movements for the same lines, inventory records would be doubled. The exclusion flag ensures each physical movement is recorded exactly once.

BUSINESS RULE: A sale order line is marked as a repair line when at least one of its stock moves has an associated repair order. POS order line stock-picking creation skips lines whose linked sale order line carries this flag.

---

## [N-U64-019] Sale Order Fulfilment at the Terminal

WHAT: When the sales integration module is installed, POS order lines can reference originating sale orders. Paying a POS order that references sale orders automatically confirms those orders and updates their linked delivery records to reflect quantities settled through the POS. Invoices generated from such POS orders inherit the partner, payment terms, and shipping address from the originating sale order.

WHY: This integration allows merchants to accept advance orders through the sales module and fulfil them at the physical counter. It eliminates manual reconciliation between sales orders and counter receipts by automatically marking the sale order as confirmed and delivered when payment is taken.

BUSINESS RULE: Only sale orders in draft or sent status are confirmed when the linked POS order is paid. Invoice values inherit from the sale order's payment terms and addresses only when the relevant fields are populated on that sale order.

---

## [N-U64-020] Gross Margin Reporting for POS Orders

WHAT: When both the sales and margin reporting modules are installed, POS order data is included in the unified sales margin report. Each POS order line contributes a margin calculation based on its sale price minus its recorded cost, adjusted for currency exchange rates.

WHY: Including POS data in the margin report gives merchants a consolidated view of profitability across both counter sales and online or telephonic orders, using a consistent margin calculation methodology.

BUSINESS RULE: The margin calculation uses the order line's price subtotal and total cost fields; if the cost is null it is treated as zero. Currency conversion applies the session's exchange rate at the time of sale.

---

## [N-U64-021] Customer Self-Order Web Application

WHAT: When the customer web-ordering module is installed, customers can browse the menu and place orders from their own devices by scanning a QR code. Each terminal generates a unique access URL that includes a short token for access control. Customer-submitted orders are synchronised to the server and processed through the same order flow as cashier-placed orders.

WHY: Web-based customer ordering reduces staff workload by allowing customers to order independently, particularly useful in restaurant or cafe settings. The access token secures the menu URL without requiring the customer to create an account.

BUSINESS RULE: The web-order URL is regenerated whenever the access token changes. Table-specific QR codes embed the table identifier in the URL so that the order is automatically assigned to the correct table. Customer-submitted orders must pass the same session-validity checks as cashier-submitted orders.

---

## [N-U64-022] SMS Receipt Delivery

WHAT: When the SMS integration is installed, the terminal can send a text message receipt to the customer's phone number at the end of a transaction. The receipt content is drawn from a configurable SMS template associated with the terminal configuration.

WHY: SMS receipts offer customers a lightweight record of their purchase without requiring a printer or an email address, and they are useful in markets where smartphone use is widespread but email is less common.

BUSINESS RULE: SMS sending requires both the SMS feature to be enabled on the terminal configuration and a receipt template to be selected. If either is absent, the send action has no effect.

---

## [N-U64-023] POS Spreadsheet Dashboards

WHAT: Two pre-built spreadsheet dashboards are available for point-of-sale reporting: one for general POS-with-employee data and one specifically for restaurant operations. Both install automatically when their respective module dependencies are present and do not require manual dashboard setup.

WHY: Pre-built dashboards reduce the implementation effort required to get meaningful management reporting from a new POS installation. Auto-installation means operators get useful analytics immediately after enabling the related modules.

BUSINESS RULE: The POS employee dashboard installs when the HR employee-login module is active. The restaurant dashboard additionally requires the restaurant module. Neither dashboard contains configurable code; they are data-only definitions that are loaded at installation.

---

## [N-U64-024] eCommerce and eLearning Spreadsheet Dashboards

WHAT: Two additional pre-built spreadsheet dashboards cover eCommerce sales performance and eLearning course sales. Each installs automatically when the corresponding website module is present.

WHY: eCommerce and eLearning merchants need quick access to sales and enrolment metrics. Auto-installing dashboards alongside the operational modules ensures that reporting capability is available from the moment the store or course platform goes live.

BUSINESS RULE: The eCommerce dashboard requires the website sales module. The eLearning dashboard requires the website slides and sales integration module. Both are data-only configurations with no Python models of their own.

---

## [N-U64-025] Discuss Integration Testing

WHAT: A dedicated test module verifies that the messaging and chat features work correctly when all possible integration modules are simultaneously installed. The tests measure both functional correctness and database query counts under a full module stack.

WHY: Messaging features accumulate overrides from many modules. Testing only in isolation does not catch regressions that appear only when all modules interact. Query count tests enforce performance boundaries that protect system responsiveness at scale.

BUSINESS RULE: The test module depends on more than twenty other modules and is intended for post-installation validation only. It has no operational purpose and is excluded from standard user-facing module categories.

---

## [N-U64-026] Event Flow Integration Testing

WHAT: A dedicated test module validates the complete event lifecycle from creation through registration and payment, including eCommerce registration, lead generation, and SMS notifications, all operating together in the same database.

WHY: Event management involves coordination between several modules — registration, sales, CRM, and communication. End-to-end tests catch integration breakpoints that unit tests running in isolation would not detect.

BUSINESS RULE: The test module depends on event, booth management, CRM integration, sale integration, SMS, and a demonstration payment provider. It targets post-installation verification scenarios and is not a user-facing application module.

---

## [N-U64-027] Mail Performance Testing

WHAT: A dedicated test module benchmarks the email and messaging subsystem under realistic load conditions, including multi-company setups, mass-mailing, and SMS routing, measuring query counts and latency at each stage of message delivery.

WHY: The mail system is a foundational service used by nearly every module. Performance regressions in mail routing can slow the entire system. Dedicated benchmarks with known query-count thresholds provide early warning of performance degradation.

BUSINESS RULE: The test module depends on mail, the mail bot, portal, rating, mass mailing, and mass-mailing SMS integration. Tests run post-installation only and are tagged for performance suites rather than functional regression suites.
