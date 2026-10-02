# U68 Neutral Knowledge — POS Payment Providers + PEPPOL Response + Mondial Relay

---

## [N-U68-001] PEPPOL Business Response Record

WHAT: The system stores one business-level response record for each incoming or outgoing PEPPOL acknowledgement or rejection. Each record is tied to a specific invoice and automatically removed if the invoice is deleted.

WHY: Maintaining a persistent log of all responses sent and received allows auditors and accounts-payable staff to prove which party acknowledged, approved, or rejected an invoice and when.

BUSINESS RULE: A response record belongs to exactly one invoice and exactly one company.

---

## [N-U68-002] PEPPOL Response Code Vocabulary

WHAT: Seven standardised response codes exist for PEPPOL business-level responses. The three that the system actively uses for outbound sending are: Acknowledgement (received), Approval (accepted for payment), and Rejection. The remaining four — In Process, Under Query, Conditionally Accepted, and Paid — are accepted inbound but not generated outbound.

WHY: These codes are defined by the PEPPOL Invoice Response transaction standard. Using standard codes ensures interoperability with any PEPPOL-compliant trading partner.

BUSINESS RULE: Only Acknowledgement, Approval, and Rejection are mandatory to implement under the PEPPOL BIS specification.

---

## [N-U68-003] PEPPOL Response Lifecycle States

WHAT: Every response record passes through up to four states: Pending Reception (just created, awaiting confirmation from the access point), Done (delivered successfully), Error (access point returned a non-recoverable error), and Not Serviced (the recipient does not support this document type).

WHY: The lifecycle state allows the system to distinguish between responses in transit and those that have been delivered or permanently failed, enabling accurate dashboard display and retry decisions.

BUSINESS RULE: Only Done responses are considered authoritative for determining an invoice's overall PEPPOL status.

---

## [N-U68-004] Sending a PEPPOL Response to a Trading Partner

WHAT: To respond to a received invoice the user's PEPPOL proxy account calls an API endpoint on the intermediary service, passing the original message UUIDs, a status code, and optional clarification reasons. The intermediary relays the response to the sender's access point.

WHY: Buyers are required under PEPPOL BIS to acknowledge receipt and optionally approve or reject invoices so that suppliers know the document arrived and whether it will be paid.

BUSINESS RULE: At least one rejection reason must be provided whenever a rejection response is sent.

---

## [N-U68-005] Rejection Workflow for PEPPOL Invoices

WHAT: When a user cancels a vendor bill that arrived via PEPPOL, a rejection wizard opens. The user must select at least one standardised rejection reason. They may also select suggested corrective actions for the supplier. Submitting the wizard sends the rejection response and then completes the bill cancellation.

WHY: Rejections must carry a coded reason so the supplier's system can route the invoice to the right queue (e.g., incorrect amount, wrong purchase order reference). The wizard enforces this requirement before allowing the cancellation to proceed.

BUSINESS RULE: A rejection without at least one reason category is refused at both the wizard level and the API call level.

---

## [N-U68-006] Parsing Incoming PEPPOL Application Responses

WHAT: Incoming ApplicationResponse documents are XML files conforming to the UBL ApplicationResponse 2.1 schema. The system extracts the overall response code from the DocumentResponse element and iterates all Status elements to build human-readable reason and action lists.

WHY: PEPPOL allows multiple status reasons and suggested actions in a single response, so a simple status code is insufficient. Structured extraction enables the full rejection detail to be shown in the invoice chatter.

BUSINESS RULE: Either a StatusReasonCode or a StatusReason text must be present; both together are recommended but not required.

---

## [N-U68-007] PEPPOL Clarification Reason and Action Codes

WHAT: Clarification records define coded reasons and suggested actions that suppliers use to understand why an invoice was rejected and what to do next. Reasons have list identifier OPStatusReason; actions have list identifier OPStatusAction.

WHY: Both codes and human-readable names are needed because some trading partners send only a code, others send only text. The system maps incoming codes to stored clarification records to display the canonical name.

---

## [N-U68-008] Chatter Logging for PEPPOL Response Events

WHAT: Every time a PEPPOL response reaches its final state a note is appended to the invoice chatter describing what happened: the invoice was received, accepted, or rejected, along with any rejection reasons and suggested actions formatted as a structured message.

WHY: Chatter logs are the primary audit trail for accounts payable staff who need to answer questions such as "did we acknowledge this invoice?" or "why was invoice X rejected?"

---

## [N-U68-009] Automatic Acknowledgement on Invoice Receipt

WHAT: As soon as a PEPPOL invoice finishes processing (all required fields extracted, document stored), the system automatically sends an Acknowledgement response back to the supplier without any user action. Posting the vendor bill sends an Approval response.

WHY: Automatic acknowledgement is a PEPPOL requirement. It confirms to the supplier that the document was received and is being processed, preventing unnecessary resubmissions.

BUSINESS RULE: Acknowledgement is sent automatically; Approval requires the user to post (validate) the bill.

---

## [N-U68-010] Error Handling for PEPPOL Response Delivery

WHAT: When the access point intermediary cannot immediately confirm delivery it returns a "not ready" code, and the response remains in Pending state to be retried. A "not supported" code permanently marks the response as not serviceable. Any other error marks it as errored and logs the error detail on the invoice.

WHY: Distinguishing transient from permanent errors prevents endless retries for responses that will never succeed and alerts staff to permanent delivery failures.

---

## [N-U68-011] Invoice PEPPOL Status Display

WHAT: An invoice has an overall PEPPOL status visible in the interface: Received (buyer acknowledged), Approved (buyer accepted for payment), or Rejected. Rejection takes precedence over all other statuses when any finalised response is a rejection.

WHY: Suppliers need a clear indication of the invoice's fate at a glance rather than having to inspect individual response records.

BUSINESS RULE: Rejection outranks Approval and Paid; Approval and Paid outrank Acknowledgement.

---

## [N-U68-012] Partner Response-Capability Check

WHAT: Before the system attempts to send any PEPPOL response to a trading partner, it verifies that the partner has been validated in the PEPPOL network and that their participant record advertises support for the Invoice Response document type. Partners who do not advertise this capability will not receive responses.

WHY: Not all PEPPOL participants support the full Invoice Response specification. Sending responses to participants who have not registered for the service would result in delivery failures.

---

## [N-U68-013] Module Registration of Supported Document Types

WHAT: The PEPPOL response module registers its ApplicationResponse document type URN with the company's document type registry. When a purchase journal is configured, the system automatically synchronises this registration with the access point intermediary so that incoming response documents are routed to this installation.

WHY: Removing or adding the purchase journal triggers a re-registration event to ensure the access point only routes document types the installation is ready to handle.

---

## [N-U68-014] Mercado Pago POS Integration Overview

WHAT: The Mercado Pago POS module integrates with the Mercado Pago Point Smart card terminal via the Mercado Pago Point Integration API. Each payment method stores a production bearer token, a webhook secret key, and the terminal's serial number, which is automatically resolved to a full device identifier.

WHY: The Point Smart terminal requires server-side payment intent management; the browser-based POS frontend delegates all API calls to the server to protect the bearer token.

BUSINESS RULE: Configuration is restricted to POS managers. Terminal lookup occurs automatically when the serial number or bearer token is saved.

---

## [N-U68-015] Mercado Pago Terminal Device Resolution and PDV Mode

WHAT: When configuration is saved the system calls the Mercado Pago devices list endpoint to locate the full device ID by matching the entered serial number as a substring. A debug utility allows an operator to force the terminal into PDV (Point of Sale) mode via a dedicated API call.

WHY: The full device ID is required for all subsequent payment intent operations. PDV mode ensures the terminal routes transactions through the correct Mercado Pago integration pathway.

---

## [N-U68-016] Mercado Pago Payment Intent Lifecycle

WHAT: A payment is managed through four server-side methods: creating a payment intent on the device, polling its status, checking the final payment record, and cancelling an outstanding intent. All calls are made over HTTPS to the Mercado Pago REST gateway with a 10-second timeout and Bearer token authorisation.

WHY: The payment terminal handles the customer interaction; the server tracks the intent lifecycle to synchronise POS order state with terminal state.

---

## [N-U68-017] Mercado Pago Webhook Security

WHAT: Mercado Pago sends asynchronous payment notifications to a public endpoint. The notification carries an X-Signature header containing a timestamp and HMAC-SHA256 value. The server reconstructs the signed template and compares digests using constant-time comparison before trusting the payload. Valid notifications trigger a bus event to the open POS session.

WHY: Without signature verification any external party could inject false payment confirmations. The webhook endpoint carries no session authentication, so cryptographic verification is the only security layer.

BUSINESS RULE: Notifications whose payment reference field does not match the expected pattern of session identifier, method identifier, and order UUID are discarded silently.

---

## [N-U68-018] Mollie POS Terminal Integration Overview

WHAT: The Mollie POS module extends a standard Odoo payment method to link to an existing Mollie payment provider account and a specific Mollie terminal device identifier. Payment operations use the Mollie Payments API with the method set to pointofsale.

WHY: Linking to an existing payment provider avoids duplicating API key management; the provider record is the single source of truth for the Mollie API key.

---

## [N-U68-019] Mollie Payment and Refund Operations

WHAT: Creating a payment generates a Mollie Payments API request specifying the terminal, currency, amount, and a signed webhook URL. Refunds are issued via the Mollie refunds sub-resource. Pending payments can be cancelled via the DELETE payments endpoint. The webhook URL is signed with a 27-hour expiry to cover Mollie's retry window.

WHY: Mollie terminals require a redirect URL and a webhook URL at creation time. The signed webhook prevents replay attacks and forgery during the retry window.

---

## [N-U68-020] Mollie Webhook Processing

WHAT: Mollie delivers payment status changes to a public webhook endpoint. The handler verifies the signed payload, fetches the current payment state from Mollie, and pushes a bus notification to the affected POS session. For successful payments the notification includes card type, number, and brand.

WHY: Terminal payments are asynchronous; the POS frontend must be notified of the outcome by server push rather than polling.

---

## [N-U68-021] Pine Labs POS Terminal Overview

WHAT: Pine Labs is a cloud-based payment terminal integration for India and Malaysia. It is available only for companies whose currency is Indian Rupees. The terminal is identified by a merchant ID, store ID, client ID, and a security token issued by Pine Labs.

WHY: Pine Labs operates a proprietary cloud API accessible only within India and Malaysia by default; a proxy endpoint can be configured for use elsewhere.

---

## [N-U68-022] Pine Labs Payment Operations

WHAT: Three operations are supported: initiating a transaction (UploadBilledTransaction), checking its status (GetCloudBasedTxnStatus), and cancelling it (CancelTransactionForced). Each call bundles the merchant credentials with the operation-specific parameters. A transaction auto-cancels at the terminal after a configurable timeout (default 10 minutes).

WHY: Cloud-based terminal integration requires server-side polling to determine whether a transaction completed, was declined, or timed out.

BUSINESS RULE: Only response code 0 with message APPROVED indicates a successful payment or cancellation. Response code 1001 means the transaction is still pending.

---

## [N-U68-023] Pine Labs Transaction Reference Tracking

WHAT: The Plutus Transaction Reference ID returned by Pine Labs on payment initiation is stored on the POS payment record. This identifier is required to perform refunds or voids after the session has closed.

WHY: Refund APIs require the original transaction reference to identify the transaction on the Pine Labs side.

---

## [N-U68-024] Pine Labs URL and Environment Selection

WHAT: The Pine Labs service URL is chosen based on a test mode flag and an optional proxy endpoint setting. Test mode points to the Pine Labs UAT testing environment. A configurable proxy allows the service to be reached from outside India and Malaysia.

WHY: The production Pine Labs API is network-restricted to Indian and Malaysian IP ranges, making a proxy necessary for cloud-hosted deployments.

---

## [N-U68-025] Pine Labs Self-Order Kiosk Integration

WHAT: When Pine Labs is used in unattended kiosk mode, the kiosk initiates the payment at the total order amount converted to paisa (multiply by 100), polls for status, and on approval automatically records the payment and marks the order as paid. A cancellation endpoint allows the customer to abort the transaction.

WHY: The kiosk has no operator to manually confirm payment, so the server must handle the full payment lifecycle autonomously and communicate the result to the customer display.

---

## [N-U68-026] QFPay POS Terminal Overview

WHAT: QFPay is a payment terminal solution available for Hong Kong dollar transactions only. It supports nine payment schemes including major credit card networks, WeChat Pay, Alipay, PayMe, UnionPay, FPS, and Octopus. The terminal is reached by its IP address configured on the payment method.

WHY: QFPay specialises in Asian payment methods popular in Hong Kong. The HKD-only constraint reflects the provider's regional focus.

---

## [N-U68-027] QFPay Request Signing

WHAT: Before sending a transaction request to the QFPay terminal the server signs the payload using AES-128-CBC encryption. The payload is sorted and formatted, an MD5 digest is computed by concatenating the formatted payload with the POS key, and then the full payload with digest is encrypted with a constant initialisation vector.

WHY: QFPay requires request encryption to prevent interception of transaction data on the local network between the POS server and the terminal device.

---

## [N-U68-028] QFPay Asynchronous Notification Handling

WHAT: QFPay sends asynchronous payment and refund notifications to a public endpoint. The trade number in the notification encodes the payment UUID, session ID, and payment method ID, separated by double dashes. The handler verifies the MD5 signature against the notification key, stores the raw response, and pushes a bus event to the POS frontend.

WHY: QFPay terminal interactions are asynchronous; the POS session must be notified of completion by server push.

BUSINESS RULE: The notification key must be configured on the payment method or the notification is rejected.

---

## [N-U68-029] QFPay Self-Order Kiosk Integration

WHAT: In kiosk mode QFPay payment notifications are processed server-side. When a payment notification arrives with status indicating success, the order is automatically marked as paid and a success result is sent to the customer display. Failure statuses send a fail result.

WHY: Kiosk-based customer ordering has no human cashier to confirm payment; the backend must finalise the order on successful terminal confirmation.

---

## [N-U68-030] Razorpay POS Terminal Overview

WHAT: Razorpay (via the Ezetap terminal) is a payment terminal solution for India, constrained to Indian Rupee transactions. The terminal supports four payment modes: All, Card, UPI, and BHARATQR. Configuration requires a device serial number, a username, and an API key.

WHY: Razorpay's Ezetap terminal is a widely used POS device in India supporting both card and mobile payment methods.

---

## [N-U68-031] Razorpay Payment Status Lifecycle

WHAT: Payments are initiated via the p2padapter API, returning a request identifier. Status is polled using the same identifier. Terminal states are mapped: AUTHORIZED with the device-done code means payment complete; VOIDED or AUTHORIZED with refund code means reversed. FAILED or the device-cancelled code means the transaction did not complete. Refunds and voids use a separate payment API path.

WHY: The Ezetap terminal processes payments asynchronously and the server must poll until a terminal status indicates finality.

BUSINESS RULE: A completed payment must show both AUTHORIZED status and the device transaction-done message code.

---

## [N-U68-032] Razorpay Endpoint and Device Addressing

WHAT: The device is identified in all requests by combining the device serial number with the suffix indicating the Ezetap Android platform. Test mode and production mode each use separate Ezetap base URLs. A shared HTTP session object is reused across requests for connection efficiency.

WHY: Ezetap requires the platform suffix to route requests to the correct device handler on their gateway.

---

## [N-U68-033] Razorpay Self-Order Kiosk Integration

WHAT: In unattended kiosk ordering mode the payment request generates a unique reference ID incorporating a UUID, then calls the standard Razorpay make-payment routine. When the polled status returns AUTHORIZED, the kiosk controller adds the payment record to the order with full card and authorisation details and marks the order as paid.

WHY: Kiosk mode requires a fully server-side payment flow with no cashier involvement; the bus service notifies the customer display of the outcome.

---

## [N-U68-034] Mondial Relay Carrier and Pickup Point Validation

WHAT: At checkout the system enforces a mutual dependency: if the shipping address is a Mondial Relay pickup point then the delivery method must also be Mondial Relay, and vice versa. Violating either direction prevents payment.

WHY: Mondial Relay orders must be shipped to physical relay points and require their own label-generation service. Mixing a relay address with a standard delivery method (or the reverse) would produce an undeliverable shipment.

---

## [N-U68-035] Automatic Shipping Partner Reset for Mondial Relay

WHAT: For ecommerce orders, if the order has a relay point as the shipping address but the delivery carrier is changed to a non-Mondial Relay carrier, the shipping address is automatically reset to the buyer's primary address.

WHY: Keeping a relay address when switching to a different carrier would create an inconsistent state that would be caught (and blocked) at checkout. Resetting the address proactively prevents confusion.

---

## [N-U68-036] Relay Pickup Point Selection Endpoint

WHAT: When a customer selects a relay point on the checkout page, the selection data (relay ID, name, street, zip, city, country) is sent to a dedicated endpoint. The system validates that the selected country is permitted by the carrier, then finds or creates a relay partner record and assigns it as the shipping address.

WHY: Relay points are physical locations that must be stored as partner records (with a unique reference) so they can appear on shipping labels and be used in carrier API calls.

---

## [N-U68-037] Relay Partner Address Protection

WHAT: Relay point addresses are managed by the Mondial Relay network, not by the customer. The system blocks any attempt to edit a relay partner's address via the standard checkout address form. The delivery completeness check is also bypassed for relay partners.

WHY: Allowing a customer to edit a relay address would corrupt the carrier's location data and break label generation. The relay API is the authoritative source for address details.

---

## [N-U68-038] Order Summary Relay Widget Data

WHAT: When the active delivery carrier is Mondial Relay, the order summary includes data needed to render the relay-point selection map widget: the carrier brand, package type, customer postal code, customer country, allowed countries, and (if already selected) the current relay point reference formatted as a country-code and numeric reference pair.

WHY: The frontend widget needs carrier-specific parameters to query the Mondial Relay pickup-point lookup API and pre-select the currently chosen relay point on the map.
