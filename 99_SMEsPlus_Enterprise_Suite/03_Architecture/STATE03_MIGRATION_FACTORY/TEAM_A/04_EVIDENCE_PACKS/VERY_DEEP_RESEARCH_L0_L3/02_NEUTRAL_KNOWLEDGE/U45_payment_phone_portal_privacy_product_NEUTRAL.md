# U45 neutral knowledge — payments, phone numbers, ratings, personal-data lookup and product configuration

> Neutral knowledge layer. Derived from Odoo 19 Community source study; status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Statements describe what a business system must do and why.

## CAP-U45-01 Online payment initiation and signed payment links

### WHAT
- A public payment page lets a customer start an online payment from a shared link. [N-U45-001]
- After paying, the customer is sent to a confirmation page. [N-U45-007]
- A public endpoint creates the payment attempt. [N-U45-008]
- A single routine builds the payment attempt from the customer's request. [N-U45-011]
- Payment links are signed with a secret-keyed hash over contact, amount and currency. [N-U45-022]
- A staff user can generate a payment link for an amount and contact. [N-U45-025]
- Signed-in users have a page to manage saved methods. [N-U45-029]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- A payment link that carries a partner but an invalid signature is treated as not existing. [N-U45-002]
- A signed-in payer is always attributed to their own contact; a different contact in the link is only flagged. [N-U45-003]
- An anonymous visitor is attributed to the contact named in the link. [N-U45-004]
- The payment attempt is accepted only if the signature matches the contact, amount and currency. [N-U45-009]
- A payment method is saved only if provider and method both allow it and the customer asks or it is mandatory. [N-U45-012]
- A saved method can be used only by its owning company contact group. [N-U45-013]
- A card-saving check uses amounts defined by the provider, not by the customer. [N-U45-014]
- The confirmation address carries a signature tied to the payment attempt. [N-U45-018]
- The confirmation page is shown only to someone holding a valid signature for that payment. [N-U45-019]
- Signature checks use a timing-safe comparison. [N-U45-023]
- A user may remove only their own or their company's saved payment methods. [N-U45-028]

### STATE
- The new payment attempt is remembered for the visitor so its outcome can be shown. [N-U45-017]

### OPTIONALITY
- Saved-method payments are charged at once unless a caller defers the charge. [N-U45-016]

### DEPENDENCY
- Contacts show how many saved payment methods they have. [N-U45-027]

### CONSTRAINT
- The currency of a payment must exist and be active. [N-U45-005]
- Only a fixed list of inputs is accepted from the customer when creating a payment. [N-U45-010]
- Numeric inputs from the customer are validated before use. [N-U45-020]
- A payer may only pay in a company they are allowed to deal with. [N-U45-021]

### RISK
- Whoever holds a valid payment link can see the payer's saved payment methods on the form. [N-U45-006]
- The post-payment redirect destination is supplied by the customer and stored. [N-U45-015]
- The link generator takes its source record from request context and trusts the model named there. [N-U45-024]
- A signed payment link does not bind the business document, so it could in principle settle a different one with the same amount. [N-U45-026]

### UNKNOWN
- None recorded at this depth.

## CAP-U45-02 Payment attempt lifecycle, amount validation and background completion

### WHAT
- Incoming provider notifications are processed in a fixed order: validate amount, update state, save method. [N-U45-035]
- A successful payment may save the method for reuse when asked. [N-U45-040]
- The customer's browser polls for the payment outcome and the server retries on concurrency conflicts. [N-U45-050]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- A provider notification is matched to a payment attempt by its reference and provider type. [N-U45-036]
- Amounts are compared in the currency's smallest unit, rounding down. [N-U45-038]
- A notification in a different currency than the payment attempt moves it to error. [N-U45-039]
- A state change request that is not allowed is ignored with a log entry, and a real change re-queues post-processing. [N-U45-046]
- The background payment job runs only while some provider is enabled or in test. [N-U45-053]

### STATE
- A payment attempt is draft, pending, authorized, done, cancelled or in error. [N-U45-030]
- A payment attempt is of a kind: online by redirect, online direct, saved method, validation, offline or refund. [N-U45-031]
- Each payment attempt records whether it was made against a live or test provider. [N-U45-034]
- A draft payment may become pending. [N-U45-041]
- A draft or pending payment may become authorized. [N-U45-042]
- A payment may be completed from draft, pending, authorized or error. [N-U45-043]
- A payment may be cancelled before completion. [N-U45-044]
- A payment may fail into error before completion. [N-U45-045]

### OPTIONALITY
- Amount verification can be skipped for card checks or providers that opt out. [N-U45-037]
- A background job retries finishing payments for four days. [N-U45-048]
- The background job is switched on only when at least one provider is active. [N-U45-052]

### DEPENDENCY
- Follow-up payments such as refunds update the original payment's status. [N-U45-047]
- Business effects of a completed payment come from other modules; the base only marks it handled. [N-U45-049]

### CONSTRAINT
- An authorized-but-not-captured state exists only for providers supporting delayed capture. [N-U45-032]
- A payment cannot use an archived saved method. [N-U45-033]

### RISK
- The payment shown to a visitor is looked up by a session-held id with elevated rights. [N-U45-051]
- No sensitive notification fields are masked by default in payment logs. [N-U45-054]

### UNKNOWN
- What data lands in payment logs at runtime is unconfirmed. [N-U45-055]

## CAP-U45-03 Capture, void and refund of payments

### WHAT
- An authorized payment can be captured in full or partially. [N-U45-056]
- Captures, voids and refunds are recorded as follow-up payments linked to the original. [N-U45-060]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- Capturing requires write permission on the payment. [N-U45-057]
- Only an authorized payment can be voided, for the amount not yet captured. [N-U45-058]
- A failed capture is recorded as an error rather than raised. [N-U45-062]
- The capture dialog is restricted by an ownership rule. [N-U45-067]

### STATE
- None recorded at this depth.

### OPTIONALITY
- None recorded at this depth.

### DEPENDENCY
- None recorded at this depth.

### CONSTRAINT
- Follow-up operations are blocked if the provider is switched off. [N-U45-061]
- A capture amount must be positive and not exceed the authorised amount. [N-U45-064]
- Providers without partial capture require capturing the full amount. [N-U45-066]

### RISK
- The engine itself does not cap a refund amount at the paid amount; limits rely on provider or caller. [N-U45-059]
- The capture dialog trusts record ids from request context. [N-U45-063]
- The capture dialog performs the capture with elevated rights without its own permission check. [N-U45-065]

### UNKNOWN
- None recorded at this depth.

## CAP-U45-04 Saved payment methods, providers and payment-method configuration

### WHAT
- An administrator can reset provider credentials. [N-U45-079]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- A saved method cannot be reactivated if its method or provider is off. [N-U45-068]
- When saving a method, tokens of the whole company group are offered. [N-U45-070]
- Saved methods are shown masked. [N-U45-071]
- Disabling a provider archives its saved methods and deactivates unsupported payment methods. [N-U45-073]
- Customers are offered only providers that are active, published and suited to country, amount and currency. [N-U45-074]
- Saved methods are visible to their owner and to their company. [N-U45-081]

### STATE
- None recorded at this depth.

### OPTIONALITY
- Validation amount defaults to zero unless a provider overrides it. [N-U45-076]
- Cloned test databases switch providers off. [N-U45-083]

### DEPENDENCY
- Adding a provider can switch the background job on. [N-U45-072]
- Access rights in the live configuration match the shipped definitions. [N-U45-082]
- Provider modules register and unregister themselves with the framework. [N-U45-084]

### CONSTRAINT
- A saved method cannot belong to the anonymous public contact. [N-U45-069]
- A provider's maximum amount is checked in company currency. [N-U45-075]
- A disabled provider cannot be published to customers. [N-U45-077]
- Seeded provider records cannot be deleted. [N-U45-078]
- A provider cannot change company once it has payments. [N-U45-080]

### RISK
- None recorded at this depth.

### UNKNOWN
- None recorded at this depth.

## CAP-U45-05 Offline bank-transfer payment

### WHAT
- Installing the offline-transfer module registers a manual bank-transfer provider. [N-U45-085]
- A ready-made transfer provider record is shipped. [N-U45-088]
- A public endpoint lets the customer confirm an offline payment. [N-U45-095]
- The transfer form posts the payment reference to the confirmation endpoint. [N-U45-099]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- Instructions shown after choosing a transfer are regenerated for transfer providers. [N-U45-091]
- A transfer provider always has pending-payment instructions. [N-U45-094]
- The transfer reference shown to the customer prefers the invoice reference, then the order reference, then the payment reference. [N-U45-100]
- Offline payments are not amount-checked on confirmation. [N-U45-101]

### STATE
- Choosing offline payment leaves the payment pending until funds are reconciled. [N-U45-102]

### OPTIONALITY
- The bank-transfer method ships switched off and supports no saving, express checkout, capture or refund. [N-U45-087]
- A transfer provider can show a payment QR code. [N-U45-090]
- No received-notification log is written for offline payments. [N-U45-103]

### DEPENDENCY
- The offline provider is paired with a bank-transfer payment method. [N-U45-086]
- The provider's default methods follow its mode. [N-U45-093]

### CONSTRAINT
- An offline provider must declare its mode. [N-U45-089]

### RISK
- Bank account labels are written into customer-facing instructions as markup. [N-U45-092]
- The offline confirmation endpoint is public and not protected against cross-site requests. [N-U45-096]
- Client-supplied data selects the payment attempt that is moved to pending. [N-U45-097]
- Anyone who knows the reference of a draft offline payment may be able to move it to pending. [N-U45-098]

### UNKNOWN
- The exact customer-facing wording and layout at runtime is unconfirmed. [N-U45-104]

## CAP-U45-06 Phone number normalisation and blacklist

### WHAT
- Numbers are parsed against a country, with a second pass to apply local rule corrections. [N-U45-105]
- A confirmation dialog collects an optional reason before unblocking a number. [N-U45-123]
- A normalised copy of each number is stored for quick matching. [N-U45-124]
- Contacts can be searched by blacklisted status. [N-U45-127]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- A number that is impossible is rejected with a reason. [N-U45-106]
- A number entered with a 00 prefix or without a plus sign is retried as international. [N-U45-107]
- A number that looks possible but fails validity is rejected. [N-U45-108]
- A number is shown in national style only when it belongs to the reference country. [N-U45-109]
- Number formatting uses the contact's country, else the company's country. [N-U45-111]
- Country is inferred from the record, else from linked contacts. [N-U45-112]
- Adding an already listed number reactivates it instead of duplicating. [N-U45-115]
- Editing a blacklisted number re-normalises it. [N-U45-117]
- Searching the blacklist normalises the typed number. [N-U45-118]
- Every blacklist change can carry a reason that is kept as history. [N-U45-120]
- Changes to blacklist entries are tracked. [N-U45-121]
- Only the system administrator can read or change the blacklist directly. [N-U45-122]
- The first usable number among mobile and phone is the one normalised. [N-U45-125]
- Opening the unblock dialog requires write right on the blacklist. [N-U45-132]
- Closing a portal account can also block the person's phone numbers. [N-U45-133]
- Typing a phone on a contact reformats it internationally in the form. [N-U45-134]

### STATE
- Removing a number archives its entry; unknown numbers get an inactive entry. [N-U45-119]

### OPTIONALITY
- Formatting problems can be tolerated or surfaced depending on the caller. [N-U45-113]
- Search speed depends on database indexes created at install. [N-U45-130]

### DEPENDENCY
- None recorded at this depth.

### CONSTRAINT
- A number may appear on the blacklist only once. [N-U45-114]
- Only valid numbers can be blacklisted. [N-U45-116]
- A phone search needs at least three characters. [N-U45-128]
- Local number-rule corrections apply only to older versions of the external phone library. [N-U45-135]

### RISK
- Without the external phone library, numbers are not validated or normalised at all. [N-U45-110]
- When a contact has two numbers, the blacklist flag reflects only one normalised number. [N-U45-126]
- Phone search runs raw SQL over many records; input values are bound but the search is not subject to record rules. [N-U45-129]
- Blacklist add and remove helpers act with elevated rights; callers must enforce permission. [N-U45-131]

### UNKNOWN
- Which countries get corrected number rules from local patches is unconfirmed. [N-U45-136]

## CAP-U45-07 Customer-portal ratings and publisher replies

### WHAT
- A publisher's answer to a rating is shown with avatar, name and date. [N-U45-140]
- A signed-in user can publish a reply to a rating from the portal. [N-U45-146]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- A reply is stamped automatically with the replying person and time. [N-U45-142]
- A reply to a rating needs website editor status or write rights on the rated item. [N-U45-143]
- An invisible rating yields a polite error. [N-U45-147]
- Messages that only carry a rating count as non-empty. [N-U45-148]
- Internal staff can edit any rating; customers and visitors have no direct access. [N-U45-151]
- Deleting a rating also deletes the related conversation message. [N-U45-153]

### STATE
- A rating can carry one reply from the publisher with who and when. [N-U45-141]

### OPTIONALITY
- Rating details appear in portal conversations only when requested. [N-U45-137]
- Conversations can be filtered by rating value. [N-U45-149]

### DEPENDENCY
- Aggregate rating statistics are shown if the record supports them. [N-U45-139]
- This capability appears automatically when portal and rating are installed. [N-U45-150]

### CONSTRAINT
- Users without rights on the rated item cannot reply. [N-U45-144]
- A rating value must be between zero and five. [N-U45-152]

### RISK
- Rating data for visible messages is read with elevated rights. [N-U45-138]
- Removing a reply bypasses the extra permission check. [N-U45-145]

### UNKNOWN
- Whether staff are limited to certain ratings by ownership or company is unconfirmed. [N-U45-154]

## CAP-U45-08 Personal-data lookup, archive, delete and audit log

### WHAT
- From a contact an administrator can start a search for all data about that person. [N-U45-155]
- The search starts from contacts matching the email or name. [N-U45-157]
- User accounts are included by login or linked contact. [N-U45-158]
- Messages written by the person are included. [N-U45-159]
- All found records can be deleted in one step. [N-U45-169]
- All found records can be archived in one step. [N-U45-170]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- Some record kinds are excluded because they are handled elsewhere or removed automatically. [N-U45-160]
- Temporary and virtual records are not searched. [N-U45-161]
- Every business record kind with an email field is searched by email and name. [N-U45-162]
- Records referring to the person are found except those deleted automatically with the contact. [N-U45-163]
- Found records the viewer cannot open are listed without a link. [N-U45-166]
- An audit entry is written only once an archive or delete action has taken place. [N-U45-171]
- The audit entry lists record kinds, counts and ids. [N-U45-172]
- The audit entry stores only masked name and email. [N-U45-174]
- Common public mail domains remain readable in the audit entry. [N-U45-175]
- Audit entries are always masked at creation. [N-U45-177]
- Only the system administrator uses the lookup and sees the audit. [N-U45-178]

### STATE
- A found record can be archived or restored from the lookup. [N-U45-167]

### OPTIONALITY
- Search results are kept only temporarily. [N-U45-173]

### DEPENDENCY
- The tool is wired into list and form actions; no usage recorded in the sample dataset. [N-U45-180]

### CONSTRAINT
- The lookup needs a valid email address. [N-U45-156]

### RISK
- The search covers all companies' data regardless of access rules. [N-U45-164]
- Wildcard characters typed in the name widen the match unexpectedly. [N-U45-165]
- The lookup deletes found records with elevated rights and no per-record permission check. [N-U45-168]
- A malformed email in the audit entry is not rejected cleanly. [N-U45-176]
- The audit trail can be erased by the same administrators who perform deletions. [N-U45-179]

### UNKNOWN
- None recorded at this depth.

## CAP-U45-09 Product option configuration and variant grid

### WHAT
- Changing the values of an option group creates, reactivates or removes per-product value records and regenerates variants. [N-U45-187]
- Each product option value can add a price surcharge. [N-U45-197]
- The system flags products whose surcharge differs from the option's default. [N-U45-200]
- A new option value can be added to all products already using that option. [N-U45-202]
- A grid of option combinations lets users enter quantities for many variants at once. [N-U45-205]
- The printed order shows variants as a table. [N-U45-209]
- Opening the grid requests its data from the document and discards a placeholder line when cancelled. [N-U45-212]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- Re-adding a previously removed option group reactivates it and keeps existing variants. [N-U45-182]
- Archiving an option group removes its values so it is clean if reactivated. [N-U45-184]
- Deleting an option group falls back to archiving when it is referenced elsewhere. [N-U45-185]
- A new option value starts with its default price surcharge. [N-U45-188]
- An option group is configurable by the buyer if it has several values, multiple choice, or allows custom entry. [N-U45-189]
- Changing exclusions on an option value regenerates affected variants. [N-U45-194]
- Removing an option value deletes it if unused, otherwise archives it. [N-U45-195]
- Product managers may apply bulk option changes. [N-U45-204]
- Combinations excluded by the product configuration are marked impossible in the grid. [N-U45-206]
- Grid headers show the surcharge converted to the document currency at today's rate. [N-U45-207]
- Only changed quantities in the grid are applied; entries are not validated in the browser. [N-U45-211]

### STATE
- Product option values have an active flag used to archive rather than delete. [N-U45-196]

### OPTIONALITY
- Picking an option that does not generate variants preselects all its values. [N-U45-190]
- The administrator chooses between adding the value to existing products or updating the surcharge on them. [N-U45-203]

### DEPENDENCY
- Every internal user gets the variants feature when the grid module is installed. [N-U45-208]
- The grid is a technical component; the sales and purchase grid features live in separate modules. [N-U45-213]

### CONSTRAINT
- An active option group needs at least one value, and each value must belong to its option group. [N-U45-181]
- An option group cannot be moved to another product or turned into another option. [N-U45-183]
- A product cannot hold the same option value twice. [N-U45-191]
- An active product option value must belong to its option group. [N-U45-192]
- Links between option values and variants cannot be set by hand. [N-U45-193]
- An option value cannot be moved to another option once used on products. [N-U45-198]
- An option value used on products cannot be deleted. [N-U45-199]

### RISK
- Any failure while deleting an option group silently becomes archiving, hiding the real cause. [N-U45-186]
- Applying the default surcharge overwrites any surcharge customised per product. [N-U45-201]
- Printed grid surcharges may differ from the actual priced amounts when price lists apply. [N-U45-210]

### UNKNOWN
- Which variants are archived versus deleted in real data is unconfirmed. [N-U45-214]

## CAP-U45-10 Product helper tools and product-linked invoice email

### WHAT
- Users can export a price list as spreadsheet or csv. [N-U45-222]
- Users can add products to an order from a catalog. [N-U45-225]
- The catalog shows each product's quantity, price and unit. [N-U45-227]
- A product can be linked to an email template. [N-U45-233]

### WHY
- None recorded at this depth.

### BUSINESS RULE
- Label printing needs a positive quantity and at least one product. [N-U45-215]
- Label data accepts only known product kinds. [N-U45-217]
- Labels use the user's visibility of products and may carry custom barcodes. [N-U45-218]
- The report expands variants only for products that have several. [N-U45-221]
- When a customer invoice is confirmed, each product's linked email is sent to the customer. [N-U45-234]
- Only accounting users see the invoice-email setting on a product. [N-U45-237]

### STATE
- None recorded at this depth.

### OPTIONALITY
- The price list report is read-only. [N-U45-219]
- A document may be made read-only in the catalog. [N-U45-228]
- The email uses a light layout and is sent as a comment. [N-U45-236]

### DEPENDENCY
- The catalog behaviour is implemented by the sales and purchase modules. [N-U45-226]
- Other modules extend document upload through hooks. [N-U45-232]

### CONSTRAINT
- A label layout must be chosen before printing. [N-U45-216]
- Documents can be attached only to products and product templates. [N-U45-229]

### RISK
- The price list report trusts client-supplied record kind and ids, restricted only by the viewer's own rights. [N-U45-220]
- Exported csv could execute formulas if a product name begins with a formula character. [N-U45-223]
- The catalog endpoint takes the document kind from the client; rights are those of the signed-in user. [N-U45-224]
- The write-permission check on upload may not actually test the target product. [N-U45-230]
- Internal error text is returned to the uploader. [N-U45-231]
- Repeated confirmation or duplicate lines can send the same email several times. [N-U45-235]

### UNKNOWN
- Who actually receives the email in practice is unconfirmed. [N-U45-238]

