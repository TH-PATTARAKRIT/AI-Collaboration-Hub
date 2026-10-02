# U54 neutral knowledge — payment provider configuration, tokens, captures, refunds; product labels, catalogues, packaging

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit: U54 | Source revision: 19.0.post20260921 | Date: 2026-10-02

---

## Payment Provider Configuration

[N-U54-001] A payment provider record holds the configuration for a single payment gateway or acquirer. It has a status with three values — disabled, enabled, and test — and a separate publication flag that controls whether customers can see it on the website. When the provider is disabled or in test mode it is automatically hidden from customers.

[N-U54-002] The publication flag and the status flag are separate. Tokens that were saved while a provider was active remain in the system even when the provider is unpublished, but they are only shown to customers on account management screens rather than on checkout.

[N-U54-003] Each provider belongs to a company. A multi-company installation can have separate provider records for each top-level company. When the provider module is installed the system automatically creates a copy of the main provider record for every top-level company that does not already have one.

[N-U54-004] A provider record lists the payment methods it supports. Changing the provider status to disabled can automatically deactivate the payment methods that are only linked to that provider. Enabling a provider activates its default payment methods.

[N-U54-005] A provider can be configured to allow customers to save their payment details for future purchases. This is controlled by a dedicated flag. A separate flag controls whether express checkout options such as wallet-based payments are available.

[N-U54-006] A provider can be configured to hold funds rather than settle them immediately. When this option is active the system captures money from the customer only when the merchant explicitly approves the charge, typically at shipment.

[N-U54-007] A provider stores four separate message templates displayed at different stages of the payment journey: before the payment, while it is pending, when it is authorised, when it is completed, and when it is cancelled. Each message is stored as rich text and can be translated.

[N-U54-008] A provider has four template references that determine which form is shown to the customer depending on the payment method being used: one for flows that redirect to a third-party page, one for forms rendered inline on the checkout page, one for payments made using a saved token, and one for express wallet flows.

[N-U54-009] A provider can restrict its availability by country, by currency, and by a maximum payment amount. Leaving any of these restrictions blank makes the provider available to all countries, all currencies, or any amount respectively. Country and currency restrictions are evaluated at the time the customer selects a payment method.

[N-U54-010] When the provider status changes from test or enabled to any other value, the system warns the operator about the number of saved payment tokens that will be archived as a result.

[N-U54-011] The feature capabilities of a provider — whether it supports tokenisation, manual capture, refunds, and express checkout — are declared as computed fields whose base values indicate no support. Individual provider modules set these fields to the appropriate level when the module is installed.

[N-U54-012] The system maintains a background scheduled task that handles deferred payment confirmations. This task is automatically enabled when at least one provider is active and disabled when no active providers remain, saving processing overhead.

[N-U54-013] Provider modules can declare that certain configuration fields are mandatory whenever the provider is in a live or test state. The system validates these fields when the provider record is saved.

[N-U54-014] When a provider is removed by uninstalling its module, the system resets its status, clears its code, unpublishes it, and removes all references to its form templates so the record remains but is inert.

[N-U54-015] All outgoing requests from the payment system to external gateways time out after ten seconds. A failed request raises a user-visible error with the gateway's error message.

[N-U54-016] The gateway selector evaluates five conditions to determine which providers are available for a given payment session: company match, customer country, payment amount ceiling, currency support, and whether saving a payment method is required. Each eliminated provider is logged with a reason.

[N-U54-017] For tokenisation validation flows — used to verify a payment method without charging the customer — the system uses a configurable validation amount that defaults to zero and a validation currency selected from the intersection of what the provider and the chosen payment method both support.

[N-U54-018] Providers can be set up to redirect the customer to a third-party page or to render a form inline. The base implementation renders a form inline by default. Providers that need redirection override the relevant method and return a different answer.

[N-U54-019] All API communication from the payment module uses a structured helper that builds the request, logs both the outgoing request and the incoming response, and converts HTTP errors into user-readable validation errors.

---

## Payment Tokens

[N-U54-020] A saved payment token represents a reference to a customer's payment details held by a gateway, not the actual card or bank details. The token record stores an opaque reference from the gateway, the payment method type, and the customer it belongs to.

[N-U54-021] Once a token is archived it cannot be reactivated if the provider that issued it is disabled or if the associated payment method is inactive. The system enforces this restriction when attempting to change the active status of a token.

[N-U54-022] A token cannot be assigned to the system's anonymous public visitor account. This constraint prevents unintentional storage of payment details against a shared user identity.

[N-U54-023] The display name shown to customers for a token is formatted as a short masked string of bullet characters followed by the last few digits of the payment details, trimmed or padded to a fixed maximum length. If no payment details are stored the creation date is shown instead.

[N-U54-024] Modules that link business documents such as subscriptions or rental contracts to a token can register those links for display on the token management screen, helping customers understand what a saved token is used for before archiving it.

---

## Manual Capture, Void, and Refund

[N-U54-025] When a payment is authorised but not yet captured, the system creates child transactions to represent subsequent capture, void, or refund operations. Each child transaction records the source transaction it was derived from, creating a traceable hierarchy of operations.

[N-U54-026] The state progression of a payment transaction follows defined rules. A pending state can only be reached from draft. An authorised state can be reached from draft or pending. A confirmed state can be reached from draft, pending, authorised, or error. A cancelled state can be reached from draft, pending, or authorised. An error state can be reached from draft, pending, or authorised.

[N-U54-027] A manual capture request creates a child transaction with a reference prefixed with the letter P followed by the original reference. A refund creates a child transaction with a reference prefixed with the letter R, and the amount is stored as a negative number to distinguish it from positive charges.

[N-U54-028] When all child transactions of a source transaction have reached a final state and their amounts sum to the source amount, the source transaction is automatically advanced to either confirmed or cancelled depending on whether any of the children were confirmed.

[N-U54-029] Providers that support partial capture must declare this capability at both the provider level and the payment method level. The capture wizard enforces this when restricting whether a partial amount can be entered.

[N-U54-030] The capture wizard shows the operator four computed amounts: the total authorised amount, the portion already captured, the portion already voided, and the maximum still available for capture. After confirming, the wizard distributes the capture amount across the selected source transactions in order and optionally voids any remaining balance.

[N-U54-031] The post-processing background task retries unprocessed transactions for up to four days after their last state change. Each transaction is processed individually, and a database error on one transaction causes only that transaction to be skipped and retried later.

[N-U54-032] When a completed payment is flagged for tokenisation the system extracts the token values from the payment response and creates a saved token record, then links the token to the transaction and clears the tokenisation request flag.

[N-U54-033] The live-transaction flag on a payment record is set at the time the transaction is created based on whether the provider is in the live-enabled state, not the test state. This allows historical records to indicate whether they were processed in production or during testing.

---

## Payment Link

[N-U54-034] The payment link generator is a wizard that builds a shareable URL pointing to the payment page. The URL includes the amount, currency, and customer identity along with a signed access token that prevents tampering. The wizard warns the operator if the amount is zero, negative, or exceeds the maximum payable amount.

[N-U54-035] The access token embedded in a payment link is computed from the partner identifier, the requested amount, and the currency, ensuring the link can only be used for that exact combination.

[N-U54-036] The wizard supports extension by modules that need to add extra parameters, change the base URL, or append an anchor fragment to the link.

---

## Product Catalogue Mixin

[N-U54-037] The product catalogue mixin is a reusable behaviour layer that any order-type model can inherit to allow users to browse and select products from a visual catalogue view. The mixin assumes the order model has a lines relationship whose counterpart model can provide per-product data.

[N-U54-038] The catalogue domain automatically excludes combination products and restricts to products belonging to the current company or shared across companies. The catalogue action opens a visual grid view and injects the identity of the calling order record into the context so that the catalogue panel can communicate back which products to add.

[N-U54-039] When the catalogue is opened, the system merges two sets of product information: data from existing order lines (showing the current quantity and any line-specific pricing) and data for products not yet on the order (showing the default type, unit of measure, and product code). Existing line data takes precedence in the merged result.

---

## Product Label Printing

[N-U54-040] The label layout wizard allows a user to configure and print product barcode or price labels. The user selects a paper format, specifies the number of copies, and optionally selects a pricelist to include on the label.

[N-U54-041] Five formats are supported: a format for Dymo label printers and four grid formats defined by column and row counts. Grid formats with price columns include the word indicating a price column in their name, which also determines whether price information is passed to the report template.

[N-U54-042] The wizard can operate on either product templates or individual product variants. When both are present, templates take priority over variants for determining the active model passed to the report.

---

## Combo Products

[N-U54-043] A combination product is a product record whose type is marked as a combo. It is composed of two or more named choice groups, each of which presents the customer with a set of options to select from.

[N-U54-044] Each choice group has a name, an optional company, a display order, and a set of individual product options. A choice group must contain at least one option and cannot contain duplicate products. Products of the combo type cannot be nested as options within another combo group.

[N-U54-045] Each option within a choice group links to a regular product variant. It displays the product's normal selling price and allows an additional surcharge price to be set for that option, defaulting to zero. The group computes a reference base price equal to the minimum selling price among all its options after converting to the combo's currency.

[N-U54-046] The base price of each choice group is used to prorate the overall combination product price across the groups. This ensures the total price presented to the customer remains consistent regardless of which option they choose within each group.

---

## Pricelists (Residual)

[N-U54-047] A pricelist record is associated with one or more country groups, allowing different prices to be applied automatically based on the customer's country. The system resolves which pricelist to apply to a partner by checking first for a pricelist stored directly on the partner record, then by matching the partner's country to a country group, then by reading a system-wide configuration parameter, and finally by selecting the first available active pricelist.

[N-U54-048] A pricelist rule can apply at four levels of specificity from most general to most specific: all products, a product category, a specific product template, or a specific product variant. When searching for the applicable rule, the system evaluates rules in order of specificity from most specific to most general and stops at the first matching rule.

[N-U54-049] Pricelist rules support three price calculation modes: a fixed amount, a percentage discount off a base price, and a formula that combines a percentage adjustment with optional rounding, an additional flat surcharge, and minimum and maximum margin constraints. The formula mode also supports using a different pricelist as the base price reference.

[N-U54-050] The system detects circular dependencies between pricelists — where pricelist A uses pricelist B as a base and pricelist B eventually uses pricelist A. A depth-first search with cycle detection raises a validation error if such a cycle is found.

[N-U54-051] When creating a pricelist rule by saving a product variant, the system automatically records the corresponding product template to ensure the rule is displayed correctly in the user interface and applied accurately during price computation.

---

## Supplier Pricing

[N-U54-052] A supplier price record stores the conditions under which a specific vendor sells a product: the minimum quantity required to obtain the price, the unit price, a percentage discount, the validity dates, a lead time in days, and vendor-specific name and code references. A discounted price is computed automatically from the unit price and the discount.

[N-U54-053] A supplier price record can apply to all variants of a product template or to a single specific variant. When a variant is specified, the template is automatically populated. The records are evaluated in priority order using a sequence number, with higher minimum quantities ranked before lower ones at the same sequence level.

---

## Product Documents

[N-U54-054] A product document is a file or link associated with a product, stored as an extension of the system's general attachment mechanism. All standard attachment properties — name, file content, external URL — are accessible directly on the document record through delegation.

[N-U54-055] When a product document record is deleted, its underlying attachment is also removed. When a product document is duplicated, the underlying attachment is copied separately using context flags that prevent unintended side effects during the copy operation.

[N-U54-056] If a product document references an external URL, the URL must use one of the standard web protocols. Invalid URLs are caught by an onchange validation before the record is saved.
