# U20 — payment providers — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

> Clean-room layer for the Odoo 19 Community study. Plain business and process language only; each statement is tagged and linked to the technical evidence by its identifier.

## CAP-U20-01 Gateway add-on contract and provider lifecycle

### WHAT
- [N-U20-001] Each online payment gateway is delivered as its own add-on that plugs into one common payment engine. The add-on contributes a new provider type, its own credential settings, and a fixed set of behaviours the engine calls at defined moments.

### WHY
- [N-U20-002] A single engine gives every gateway the same transaction life cycle, the same tamper checks on amounts, the same post-payment accounting hand-off and the same availability filtering, so that adding a gateway does not require re-implementing payment accounting.

### BUSINESS RULE
- [N-U20-003] A gateway's own credential settings are mandatory only while its provider is in test or enabled mode; a disabled provider may be saved with empty credentials. The check runs on creation and on every update.
- [N-U20-005] The recurring job that finishes processing of confirmed payments is switched on only while at least one provider is not disabled, and is switched off again when the last one is disabled.
- [N-U20-009] To process an inbound payment message every gateway add-on must tell the engine how to find the matching transaction, how to read the amount and currency, how to translate the gateway status into the shared transaction states and how to extract data needed to save a payment method.
- [N-U20-011] Calls from the ERP to a gateway wait at most ten seconds; a refused connection, timeout or HTTP error is turned into a validation error that the calling step converts into a transaction error state with the gateway message.
- [N-U20-013] When a copy of the database is neutralized for testing, the engine forces every enabled provider back to disabled (test mode is kept) and each gateway add-on blanks its own credentials; one gateway replaces them with dummy values instead of blanks.

### STATE
- [N-U20-004] A provider is disabled, enabled or in test mode and starts disabled. Moving away from disabled switches on the gateway's default payment methods; moving to disabled switches off every payment method that no other active provider supports. Leaving the enabled or test mode archives all saved payment tokens of that provider.

### OPTIONALITY
- [N-U20-008] Optional capabilities (saving a payment method, two-step authorize-then-capture, refunds from the ERP, express checkout) are declared per gateway; by default a gateway declares none of them and refunds are unsupported.

### DEPENDENCY
- [N-U20-006] Installing a gateway add-on gives every top-level company its own provider record by copying the first one; uninstalling resets the provider to an unset type, disabled, unpublished and without its form templates. The add-on that supplies cash on delivery adds a further custom provider record.
- [N-U20-012] Every gateway add-on in scope depends on the payment engine only; none depends on accounting or sales directly, so the hand-off to invoices and orders comes from separate bridging add-ons.
- [N-U20-029] In the reference database all twenty-three gateway add-ons, the offline add-on and the demo add-on are installed even though only the demo provider (test mode) and the cash-on-delivery provider (enabled, supplied by the delivery add-on) are active; every other provider is disabled with empty credentials. A twenty-fifth provider placeholder belongs to a direct-debit add-on that is not part of the community source and is marked uninstallable.

### CONSTRAINT
- [N-U20-007] A provider that ships as master data cannot be deleted; the only supported ways to retire it are disabling it or uninstalling its add-on.
- [N-U20-010] If a gateway add-on does not read an amount from the message, the engine treats the amount as missing and puts the transaction into the error state; a gateway can bypass the amount check only by explicitly declaring that it has no amount to check.

### RISK
- [N-U20-014] Transaction creation from the shop front end does not itself re-check that the chosen provider is enabled, published and compatible with the amount, currency and country; the demo add-on adds such a check for its own provider only, which suggests the generic path relies on the front end offering only compatible providers.

### UNKNOWN
- [N-U20-015] Whether any deployment-level control (reverse proxy, firewall allow-list) restricts who can reach the gateway callback addresses is not determinable from source.

## CAP-U20-02 Initiating an online payment through a gateway

### WHAT
- [N-U20-016] When a customer pays online the engine creates a draft transaction and each gateway add-on prepares the outbound step: a signed redirect form, a hosted payment session created by a server call, an embedded-form session, a saved-token charge, or a server-created order or charge request.

### WHY
- [N-U20-017] The shop must hand the gateway the exact amount, currency, order reference and customer details so the gateway can later report back a result that is traceable to one shop transaction.

### BUSINESS RULE
- [N-U20-018] Redirect-style gateways receive the merchant reference, amount, currency and return and callback addresses either as a form signed with a shared secret or through a server call that returns a hosted checkout address.
- [N-U20-019] Embedded gateways create the payment session on the server first and give the browser only a short-lived client token; the browser then completes card entry directly with the gateway.
- [N-U20-020] A saved-payment-method charge is sent from the server immediately when the transaction is created; any failure puts the transaction into error with the gateway message.
- [N-U20-021] Several gateways limit the format or length of the merchant reference, so the engine regenerates the reference with a timestamped short prefix for them (alphanumeric only for one, at most 35, 30 or 20 characters for others, digits plus a separator letter for one).
- [N-U20-022] Payment-creating server calls to several gateways carry an idempotency key derived from the database identity, the transaction reference and the call scope so that a repeated call does not charge twice.
- [N-U20-023] The customer's name, language, email, address, phone and country are copied onto the transaction at creation and sent to gateways as billing data, so later edits to the customer record do not change what the gateway was told.
- [N-U20-024] For browser-initiated steps in direct-payment gateways the shop signs the request values; for some it signs reference, amount, currency and customer, for others only reference and customer, relying on the server-held transaction amount.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-025] One gateway builds its payment-session request as XML text by concatenating customer-supplied values (name, email, city, zip) without escaping, so special characters in customer data can alter the request.
- [N-U20-026] One gateway's direct card payment step lets the browser supply the amount to be charged and does not require the signed access token, while the later amount check reads an echoed order amount rather than the charged amount; this may allow under-payment (confirmation requires runtime test).
- [N-U20-027] For one gateway the follow-up step after strong customer authentication and the return step accept a transaction reference from the browser without a signed token, and the return step silently switches the transaction to the redirect flow.

### UNKNOWN
- [N-U20-028] Front-end scripts and page templates of each gateway were not read except where named in claims; the exact browser behaviour of embedded forms is therefore not described.

## CAP-U20-03 Gateway notifications, return handling and forgery and replay protection

### WHAT
- [N-U20-030] After the customer pays, each gateway reports the outcome in two ways: the customer's browser is sent back to a shop address, and the gateway posts a server-to-server notification. Both public addresses are reachable without a login, so the shop must prove the message is genuine before changing a transaction.

### WHY
- [N-U20-031] An unauthenticated message that can mark a transaction confirmed would allow goods to be released and invoices to be settled without money having moved; forgery and replay protection is therefore the most security-critical part of every gateway add-on.

### BUSINESS RULE
- [N-U20-032] Three authentication families exist: a payload signed with a shared secret (the majority); a static shared token sent in a request header (two gateways); and no authentication of the message at all, followed by the shop asking the gateway directly, with its own credentials, what the real status of the payment is (several gateways, and the return step of others).
- [N-U20-033] When the transaction named in a message cannot be found, the shop acknowledges the message and changes nothing; verification is only performed once a transaction is located.
- [N-U20-034] For signed families a missing signature or a wrong signature stops processing with a forbidden response; a missing secret is refused outright by two gateways and in the others ends in an unhandled error that leaves the transaction unchanged; the comparison of the received and expected values is done in constant time for every gateway that compares a secret.
- [N-U20-035] Only one gateway add-on bounds the age of a notification (ten minutes); all others have no timestamp or one-time check and rely on the transaction state machine, which ignores a message that repeats the current state and refuses transitions that are not allowed from the current state.
- [N-U20-036] Where the shop pulls the payment from the gateway, the result is trusted only if it is tied to the transaction: some add-ons compare the gateway's merchant reference with the shop reference or fetch by the reference or gateway id stored on the transaction.
- [N-U20-037] Most callbacks answer with a success acknowledgement even when processing raised a handled error, so the gateway does not retry endlessly; unhandled errors (including forbidden responses) are returned to the gateway.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-038] Two gateways (Flutterwave and Xendit) authenticate the notification only by a static token in a header that does not depend on the message content; anyone who learns the token can forge any notification, and the token is not rotated per message.
- [N-U20-039] The Korean gateway Toss Payments skips verification for expired and aborted notifications, still stores the secret carried in such a notification on the transaction, and treats unknown statuses as errors; because an errored transaction may later be confirmed, a person who knows a transaction reference and its amount could forge two notifications (an aborted one carrying a chosen secret, then a done one carrying the same secret) and obtain a confirmed payment without paying. Requires runtime confirmation.
- [N-U20-040] For DPO the shop looks up the transaction from the reference in the return address, confirms a gateway payment id from the same address, merges the gateway answer into the data, but never checks that the gateway answer refers to the same reference; one genuine payment id might therefore be used to confirm several transactions of equal amount. Requires runtime confirmation.
- [N-U20-041] For Razorpay redirect returns the signature covers only the gateway order and payment ids, the amount is not checked in that path, and the description used to tie the payment to the shop reference is supplied by the browser script; confirmation may be possible for a different transaction. Requires runtime confirmation.
- [N-U20-042] For PayPal a notification whose origin check cannot be completed because the verification call itself fails is treated as a payment error and sets the referenced transaction to error, so an unauthenticated message naming a known reference could cancel an in-progress payment (a later genuine confirmation can still succeed because error to confirmed is allowed).
- [N-U20-043] For Adyen the lookup logic for capture, cancellation and refund notifications can create child transactions before the signature has been verified; the request is rolled back when the verification then fails, but the order of operations is the reverse of what is normally required.
- [N-U20-044] Several gateway protocols dictate weak constructions: SHA-1 digests (Buckaroo, AsiaPay default), a secret prefix hash with no field delimiters (Nuvei), plain SHA-256 over phrase-wrapped text (APS, ECPay) rather than keyed message authentication codes; these are vendor-defined but reduce assurance.
- [N-U20-045] The offline-payment address (wire transfer and cash on delivery) and the demo address accept a reference from any caller and move the matching transaction to pending (offline) or to any simulated state (demo); there is no authentication on either.

### UNKNOWN
- [N-U20-046] Actual behaviour of each gateway's sandbox and live servers (retries, ordering, signature header format changes, secret rotation) is not determinable from source and needs runtime observation.

## CAP-U20-04 Amount and currency validation and state translation

### WHAT
- [N-U20-047] Before a gateway message may change a transaction, the engine compares the amount and currency in the message with those of the shop transaction and then translates the gateway's own status vocabulary into the shop's states (draft, pending, authorized, confirmed, canceled, error).

### WHY
- [N-U20-048] Under-payment, wrong-currency payment and replay of a cheaper payment against a dearer order are the principal fraud routes against a shop that trusts gateway messages, so amount equality is the last line of defence once authenticity is established.

### BUSINESS RULE
- [N-U20-049] The transaction amount is rounded down to the gateway's currency precision and must equal the amount in the message (refunds are compared as negatives); the currency code in the message must equal the transaction currency. A missing amount or currency, an amount difference or a currency difference puts the transaction into error with an explanatory message and stops further processing of that message.
- [N-U20-050] Validation transactions (zero or token-setup amounts) are never amount-checked; gateways may also opt out explicitly. Opt-outs exist for offline payment, the demo gateway, Authorize.Net (when the detail lookup fails), Adyen (redirect, 3-D Secure challenge and refused answers), Razorpay (redirect return) and Nuvei (empty cancel message).
- [N-U20-053] Gateways whose minor-unit precision differs from the standard currency tables supply their own precision (Stripe, Adyen, Mercado Pago, Nuvei, Xendit); the engine uses it both for converting and for rounding down the shop amount.
- [N-U20-057] State messages shown to the customer and written to the chatter come from the provider's configured messages (pending, authorized, done, cancelled) with defaults; an empty configured message suppresses the notice.

### STATE
- [N-U20-055] Each gateway maps its codes as follows: success codes become confirmed; in-progress or review codes become pending; an authorization held for later capture becomes authorized only where manual capture is supported; cancellation, expiry or decline becomes canceled or error depending on the gateway; any unknown code becomes error with the code in the message.
- [N-U20-056] DPO treats both its authorized and its paid result codes as confirmed, so a card pre-authorization is booked as paid; Mollie reports authorized although its provider does not declare manual capture, which the engine's state check would reject at runtime.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-051] Five gateways (AsiaPay, Authorize.Net, ECPay, PayU, Toss Payments) take the expected currency from the shop's own configuration or constant rather than from the message, so a currency difference in the message is not detected there; this is acceptable only because each of those accounts is limited to a single currency.
- [N-U20-052] For Authorize.Net the amount check is skipped whenever the follow-up transaction-detail request returns an error, so the payment is accepted on the basis of the immediate response alone.
- [N-U20-054] For Xendit every supported currency including the Thai baht is declared to have zero decimals: the shop truncates the amount to whole baht when sending it and when checking it, so a fractional satang amount is silently under-collected yet the transaction is recorded as paid in full.

### UNKNOWN
- [N-U20-058] The exact gateway code tables (for example full lists of response codes) were read only from the constants files; any gateway code not listed there is classified as an error and the real-world frequency of this is unknown.

## CAP-U20-05 Credential storage, access and logging

### WHAT
- [N-U20-059] Each gateway's credentials (API keys, signing secrets, webhook secrets, OAuth tokens, merchant ids) are stored as plain text fields on the provider record, together with the transaction and token data the gateway returns.

### WHY
- [N-U20-060] Whoever holds a gateway secret can move money or forge confirmations, so who can read or change these fields, and what appears in logs, determines the real exposure of the payment function.

### BUSINESS RULE
- [N-U20-061] Only the system administrator role may read or change provider records at model level, and a company rule limits visibility to the user's companies; transaction records are readable and writable by administrators and by the invoicing role, and saved tokens are readable by every internal, portal and public user but restricted by rule to the user's own partner.
- [N-U20-062] Most secret fields carry an additional field-level restriction to the administrator role (Stripe, Adyen, APS, AsiaPay, Authorize.Net, Buckaroo, DPO, ECPay, Flutterwave, Iyzico, Mercado Pago, Mollie, Nuvei, PayPal, PayU, Razorpay, Redsys, Toss, Xendit), and the form shows them as password fields.
- [N-U20-066] Saved payment methods hold only the gateway's reference and the last four digits (or account digits); card numbers are never stored by the shop, and each gateway's token fields are read-only.
- [N-U20-067] Copies of the database prepared for testing have all gateway credentials blanked and live providers disabled.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-063] Worldline's API key, API secret, webhook key and webhook secret, and Paymob's HMAC key and API key, are plain fields without the administrator-only restriction; because model access is already administrator-only the exposure is limited to code paths that read the provider as another user (for example server-side reads in sudo or exports), but the defence in depth present for other gateways is missing.
- [N-U20-064] The shared log mask lists only two sensitive keys (one added by Stripe, one by Toss); outbound request bodies are logged at information level and every gateway response body is logged in full; most callbacks log the complete notification including customer data; three onboarding flows and Authorize.Net use the standard logger without the payment mask.
- [N-U20-065] Credentials and OAuth tokens are stored unencrypted in the database; whether the deployment adds disk, backup or secret-store protection is not visible from source.

### UNKNOWN
- [N-U20-068] Whether the production database keeps credentials in these fields or injects them from a secret store is unknown; the restored database holds no credential values in any of the sixty-eight credential and identifier columns.

## CAP-U20-06 Capture, void, refund and saved payment methods

### WHAT
- [N-U20-069] Beyond the first payment, a gateway may support saving the payment method for later charges, authorizing now and capturing later (fully or partly), voiding an authorization and refunding from the ERP; each is exposed only for gateways that declare it.

### WHY
- [N-U20-070] Merchants need to take payment only when goods are ready to ship, return money for returned goods and charge subscriptions without the customer present; the engine must keep each partial capture or refund traceable to the original payment.

### BUSINESS RULE
- [N-U20-072] A capture, void or refund creates a child transaction of the original: refunds get a reference prefixed R and a negative amount, partial captures and voids a prefix P; the original moves to confirmed or canceled only when its children in final states add up to its amount.
- [N-U20-073] Stripe, Adyen and Razorpay create refund child transactions automatically when a refund started in the gateway's own dashboard is reported back; Adyen does the same for captures and voids started there.
- [N-U20-074] Only confirmed transactions can be refunded and only authorized ones captured or voided; every request to the gateway requires the provider not to be disabled.
- [N-U20-075] A payment method is saved only if the provider allows it, the method supports it and either the flow requires it or the customer asked for it; the browser cannot force it. A transaction paid with a token is charged immediately, and a token cannot be used by a different commercial partner.
- [N-U20-076] For Authorize.Net a refund of an unsettled payment is turned into a void (no refund transaction created for funds that never moved); a refund already made at the gateway is recorded as a confirmed refund.
- [N-U20-077] Razorpay cannot void from the ERP, and an off-session charge is refused while an earlier pending charge on the same token and document is less than 36 hours old.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- [N-U20-071] Support matrix: Stripe supports express checkout, full-only manual capture, partial refund and saving; Adyen supports partial capture, partial refund and saving; Authorize.Net supports full-only capture, full-only refund and saving; Razorpay supports full-only capture, partial refund and saving; Flutterwave, Mercado Pago, Worldline and Xendit support saving only; the demo gateway supports everything; all other gateways (APS, AsiaPay, Buckaroo, DPO, ECPay, Iyzico, Mollie, Nuvei, Paymob, PayPal, PayU, Redsys, Toss and the offline modes) support none and refunds must be made in the gateway's dashboard.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- Not applicable to this capability.

### UNKNOWN
- [N-U20-078] Whether partial capture is correct in the engine when the sum of children differs by rounding (the comparison uses decimal rounding of the currency) is not tested here; behaviour of gateway-side expiry of authorizations is not modelled.

## CAP-U20-07 Availability, currencies, countries and Thailand relevance

### WHAT
- [N-U20-079] Which gateways and which payment methods the customer sees depends on the provider's mode, publication, company, the customer's country, the document currency, the amount and any currency restrictions the gateway add-on imposes.

### WHY
- [N-U20-080] Offering a gateway that cannot accept the currency or country, or exceeds a configured ceiling, produces failed payments late in the flow; filtering up front protects conversion and avoids orphaned transactions.

### BUSINESS RULE
- [N-U20-081] A provider is offered if it is enabled or in test mode, belongs to the company (or a parent), is published for non-internal users, supports the customer's country (empty means all), the maximum amount converted to company currency is not exceeded, the currency is in its list (empty means all), and tokenization or express checkout is supported when required.
- [N-U20-082] Gateway add-ons that publish a supported-currency list fill the provider's currency list only when it is a strict subset of all currencies; gateways with no such list leave it empty, which means the engine offers them for any currency and an unsupported currency fails only at the gateway.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- [N-U20-084] Thai baht is accepted by Mollie, PayPal, Razorpay and Xendit through explicit currency lists, by AsiaPay through its currency code table, and without restriction by Stripe, Adyen and Worldline; Buckaroo, Flutterwave, Iyzico, Nuvei, ECPay, PayU and Toss exclude it, and Redsys, APS, Authorize.Net, DPO, Mercado Pago and Paymob publish no list.
- [N-U20-085] Thai-specific payment methods in the shipped catalogue: PromptPay (Adyen, AsiaPay, Stripe, Xendit), TrueMoney (AsiaPay, Xendit), LINE Pay (AsiaPay, Xendit), Rabbit LINE Pay (AsiaPay), ShopeePay (Xendit), several Thai bank channels (AsiaPay, Xendit), Online Banking Thailand (Adyen) and Alipay Plus (Worldline); AsiaPay can be configured for the SiamPay brand, which serves Thailand.
- [N-U20-086] A Thai company can onboard to Stripe's connected-account flow only because Thailand appears in Stripe's supported-country set marked beta; the add-on does not itself restrict which countries may pay.

### CONSTRAINT
- [N-U20-083] AsiaPay, Authorize.Net, Paymob and Mercado Pago accept exactly one currency per account and reject enabling with several; ECPay (Taiwan dollar), Toss Payments (Korean won) and PayU (Indian rupee) are single-currency by constant.

### RISK
- Not applicable to this capability.

### UNKNOWN
- [N-U20-087] Source reading found no Thai domestic gateway add-on in the community edition (for example for a Thai acquirer); whether PromptPay QR via bank transfer or e-invoice integration exists elsewhere is outside this unit and unknown.
- [N-U20-088] In the restored database the company currency is Thai baht and only baht and US dollar are active, so gateways restricted to euro, Indian rupee, Taiwan dollar or Korean won could not be offered for baht documents; whether foreign-currency documents are used is unknown.

## CAP-U20-08 Offline payment modes (wire transfer and cash on delivery)

### WHAT
- [N-U20-089] The custom provider add-on offers payment modes that involve no online gateway. Wire transfer shows the customer the company's bank details and a payment reference; cash on delivery (added by the delivery add-on) records that the customer will pay the courier.

### WHY
- [N-U20-090] Many small businesses accept bank transfers or cash on delivery; the shop still needs an order or quotation state change and a traceable transaction so that finance can match the incoming money later.

### BUSINESS RULE
- [N-U20-091] Choosing an offline mode creates a draft transaction; the customer's browser then posts to a public address that moves it to pending without any amount check. Pending offline transactions send the quotation, set the order payment reference (custom providers) and, for cash on delivery, confirm the order automatically.
- [N-U20-092] The wire-transfer provider's pending message is regenerated from the bank accounts of the company's bank journals when accounting is installed; the communication to quote is the invoice payment reference, else the order reference, else the transaction reference.
- [N-U20-093] Cash on delivery is offered only on orders whose delivery method has the cash-on-delivery option ticked; if not ticked the provider is removed from the compatible list with an explicit reason. No delivery method in the restored database has the option ticked.
- [N-U20-096] Offline transactions never reach confirmed through the engine: confirming a payment received by transfer is done by registering a payment in accounting, not by the transaction.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- [N-U20-095] Wire transfer ships disabled with its payment method inactive; cash on delivery ships enabled and published with an active payment method as soon as the delivery add-on is installed, but is invisible unless a delivery method opts in.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U20-094] A custom mode may only be set on the custom provider type and the custom provider type requires a mode; wire transfer is the only mode the custom add-on knows, cash on delivery is added by the delivery add-on.

### RISK
- [N-U20-097] The offline processing address is open to any caller who knows or guesses a transaction reference; the effect is limited to moving a draft transaction to pending, but for cash on delivery that triggers automatic order confirmation. The engine's customer-facing creation step does not verify that the offline provider is enabled (see CAP-U20-01), so a disabled wire-transfer provider could still be driven by a crafted request.

### UNKNOWN
- [N-U20-098] How the bank-details message renders for multi-company and multi-bank journals, and whether the QR option has any effect in this edition, was not traced.

## CAP-U20-09 Demo gateway

### WHAT
- [N-U20-099] The demo add-on is a fake gateway that lets a tester walk through the whole payment and post-payment flow by choosing the outcome (confirmed, pending, canceled, error) on screen, including saved payment methods, authorize-capture, void and refund.

### WHY
- [N-U20-100] It allows demonstrations and integration testing of invoices, orders and accounting hand-offs without contacting any real gateway.

### BUSINESS RULE
- [N-U20-102] A public, unauthenticated address accepts a reference and a simulated state and applies it to the matching demo transaction; backend buttons on the transaction do the same for administrators. Amounts are never checked.

### STATE
- [N-U20-101] The demo provider may only be disabled or in test mode (never enabled); the shipped data sets it to test mode and published with the demo payment method, saving of payment methods and express checkout turned on.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-103] In the restored database the demo provider is in test mode, published and its payment method is active; a customer or anonymous visitor who sees it at checkout (published providers are shown to non-internal users) could complete a payment with no money moving, which would confirm orders and post payments. The demo add-on should not be installed, or the provider must be disabled, in any production database. Requires runtime confirmation of what the storefront and customer portal list.

### UNKNOWN
- [N-U20-104] Whether the demo provider appears on the customer portal payment page in this installation (it depends on sales and website add-ons that were not studied for this behaviour) is not confirmed.

## CAP-U20-10 External connectivity and merchant onboarding

### WHAT
- [N-U20-105] Every gateway add-on talks to external services over the internet: the gateway's own API, hosted checkout pages, and for four gateways (Stripe, Mercado Pago, Razorpay, PayU) an intermediary service run by the software vendor that carries out account connection and token refresh on the shop's behalf.

### WHY
- [N-U20-106] Connecting a merchant account through the vendor's onboarding service avoids manual key entry, but it also places the vendor's service in the trust path and requires outbound internet access and publicly reachable callback addresses.

### BUSINESS RULE
- [N-U20-108] Connection flows return to an authenticated shop address that checks a session-bound anti-forgery token before storing the credentials and enabling the provider; the credential write is performed as the logged-in user, so it needs the administrator role.
- [N-U20-109] The administrator can ask the shop to register its own callback at the gateway for Stripe, PayPal and Razorpay; the generated secret or webhook identifier is stored on the provider.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- [N-U20-107] Endpoints are chosen by provider mode: live or sandbox hosts per gateway, with prefixes configurable for Adyen and Paymob; the shop also hands the gateway its own public base address for return and callback URLs.

### CONSTRAINT
- Not applicable to this capability.

### RISK
- [N-U20-110] Callback addresses must be reachable from the gateway on the public internet; a shop on a private address or behind a login wall will never receive notifications and relies on the customer's return visit, which for several gateways does not confirm the payment.

### UNKNOWN
- [N-U20-111] All network behaviour (latency, error shapes, certificate failures, rate limits, the vendor intermediaries' availability and what they retain) is runtime-only and not determinable from source.
