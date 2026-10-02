# U63 neutral knowledge — payment gateway provider implementations

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit: U63 | Date: 2026-10-02 | Source revision: 19.0.post20260921 (Odoo 19 Community only)

---

[N-U63-001] Each payment gateway provider integration follows a common pattern: the system creates a payment record on the provider's server, redirects the customer to the provider's hosted payment page, and on return the system processes the outcome via a dedicated return web address. The customer never directly submits card details to the Odoo server in this flow.

[N-U63-002] Provider credential fields are split by sensitivity. Public identifiers such as merchant codes and public keys are stored with standard access, while secret keys, API secrets, and webhook signing secrets are restricted to the system administrator group and are not visible to regular users.

[N-U63-003] Each provider module stores its API base address in a dedicated method that returns different addresses for test and production environments. Switching the provider between test and enabled states automatically uses the appropriate address without any manual configuration.

[N-U63-004] Transaction references are extracted differently by each provider, reflecting how each provider carries the original order reference back in its notification. The extraction logic is isolated in a dedicated method that handles only the provider-specific field name.

[N-U63-005] All providers map their own status codes or status strings to five common Odoo transaction outcomes: pending, authorized, done (successful), cancelled, and error. The mapping is defined as a constant dictionary in each provider module so it can be inspected without reading executable logic.

[N-U63-006] Every provider that receives server-to-server payment notifications performs a security check before updating any transaction state. The most common approach is to verify a cryptographic signature: the provider computes a digest over the notification payload using a shared secret, embeds it in the notification, and the Odoo handler recomputes and compares the digest. Three providers instead re-fetch the payment status from the provider API to confirm authenticity rather than verifying an inbound digest. All comparisons use constant-time string functions to prevent timing-based attacks.

[N-U63-007] Several providers enforce restrictions on the currencies or countries they support. ECPay accepts only Taiwanese New Dollar. Toss Payments accepts only Korean Won. Paymob derives its accepted currency from the merchant account country. These restrictions are enforced both by filtering the list of available currencies in the user interface and by programmatic validation that raises an error if a non-supported currency is configured.

[N-U63-008] All provider webhook notification addresses are configured to accept cross-origin server-to-server requests by disabling the built-in cross-site request forgery protection. This is architecturally necessary because the payment provider servers post notifications from outside the Odoo session, so no browser session token is present. The webhook handler authenticates each request through the provider-specific signature check instead of relying on the session protection mechanism.

[N-U63-009] Five of the sixteen providers declare support for storing card details for future use without re-entering payment information. These five also implement a dedicated method for initiating a payment using a stored card. Three providers additionally declare support for capturing a previously authorized payment in a separate step. Three providers declare support for initiating refunds programmatically.

[N-U63-010] Two providers route their API calls through an Odoo-hosted intermediary server rather than directly to the payment provider API. This design allows Odoo to centrally manage API versioning, authentication, and compatibility for those integrations.

[N-U63-011] PayPal uses an OAuth 2.0 authorization flow: the system obtains a short-lived access token from PayPal using the stored client credentials, caches the token with its expiry time, and renews it automatically when expired. Mercado Pago similarly uses an OAuth authorization callback route.

[N-U63-012] The Redsys integration requires a third-party cryptographic library to perform a legacy triple-key encryption step as part of signature computation. The module includes compatibility handling for two different versions of that library.

[N-U63-013] Each provider module lists the payment method codes that should be activated automatically when the provider is enabled. These default codes are defined as a constant set and cover the primary accepted payment instruments for each provider.

[N-U63-014] The return address routes where customers land after completing payment at the provider are registered with a public authorization level so no session or login is required. This is necessary because the customer is returning from an external site.

[N-U63-015] Several return routes set a flag that prevents Odoo from creating a new browser session when the customer arrives via a cross-origin redirect. Without this flag, some browsers that enforce strict same-site cookie rules would cause the customer session to be lost, preventing the transaction status from being updated in the browser.

[N-U63-016] Toss Payments performs an additional amount validation step on the success return: before confirming the payment with the provider, the system verifies that the amount parameter in the return URL matches the transaction amount stored in the database. This prevents a client-side tamper attack where the amount in the return URL is modified.

[N-U63-017] All sixteen provider modules use a specialized logger from the base payment framework rather than a standard logger. This logger automatically redacts sensitive field values from log output to prevent secret keys or card numbers from appearing in server logs.

[N-U63-018] The Stripe integration maintains a list of specific event types it is interested in receiving from the provider webhook channel. Events not on this list are silently acknowledged without processing. The event list covers payment progress, authorization for capture, success, failure, cancellation, refund creation, and refund updates.

[N-U63-019] Redsys encodes its outbound payment parameters as a Base64 string before transmitting them in the form submission, and the same encoded format is returned in the notification. The controller Base64-decodes the parameters before reading individual fields.

[N-U63-020] Nuvei has two separate signature verification paths: for normal payment notifications it verifies the provider-computed checksum field in the payload, but for error and cancellation return visits it verifies an Odoo-generated access token instead, since no payment data from the provider is available in those cases.

[N-U63-021] Iyzico generates a fresh random nonce value for each outbound API request and includes it in the authorization header. This nonce is incorporated into the request signature, making each signed request unique even if the payload is identical.

[N-U63-022] Paymob normalizes notification data before verifying the signature, because webhook callbacks arrive as a typed data structure while redirect returns arrive with all values as strings. The normalization step produces a unified format so the same signature computation works for both delivery channels.

[N-U63-023] Toss Payments skips webhook signature verification for a small set of status values representing expired or aborted payment events. For these events the system may not have the expected secret key stored, either because the payment was never initiated or because an API call failed before the secret was recorded.

[N-U63-024] The Worldline integration uses a different credential set for outbound API request signing and inbound webhook notification verification. The outbound requests use an API key and secret for the authorization header signature, while inbound webhook notifications are verified against a separate dedicated webhook key and secret.

[N-U63-025] Xendit uses a static webhook callback token stored on the provider record rather than a computed cryptographic signature over the notification content. The received token is compared to the stored value using a constant-time function. Card payments use a distinct direct flow: the card details are tokenized in the browser, and the payment is initiated via a JSON-RPC call to Odoo rather than a redirect to the provider.
