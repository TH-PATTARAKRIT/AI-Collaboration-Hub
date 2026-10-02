# U45 — payment, phone, portal, privacy and product families (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U45
- Modules: payment, payment_custom, phone_validation, portal_rating, privacy_lookup, product, product_email_template, product_matrix
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: source evidence is not runtime proof (RT flags); no business data read from the database; prior evidence U12, U20, U03, U21, U02, U22 not redone. Security observations are INFERENCE and flagged RT where they need execution to confirm. No statutory claims are made.

## CAP-U45-01 Online payment initiation and signed payment links

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A customer (or a logged-in user) pays an amount in a currency through a provider, reached from a signed link; the system builds a payment attempt and sends the customer to a confirmation page. Staff can generate signed links through a wizard.

### D2 Architecture, data and object relationships
payment.provider, payment.method, payment.token, payment.transaction (landing_route, tokenize, operation), res.partner (token count); HMAC helper in payment/utils.py; payment.link.wizard (transient) producing /payment/pay URLs; session-held monitored transaction.

### D3 Source, technical and workflow logic
Controller /payment/pay validates the HMAC when partner_id is present, resolves partner (own partner for logged-in users), checks currency, reads compatible providers, methods and tokens in sudo, renders the form. /payment/transaction (jsonrpc) re-checks the HMAC over partner/amount/currency, whitelists kwargs, calls _create_transaction which decides tokenisation, validates token ownership, creates the tx in sudo, charges immediately for token flows, and registers the tx for monitoring. _update_landing_route appends tx_id and a recomputed access token. /payment/confirmation re-verifies the HMAC against the stored tx.

State diagram:
- (link) -> form shown [valid access token or no partner]
- (link) -> NotFound [partner given and invalid token]
- form -> draft transaction [/payment/transaction]
- draft -> confirmation page [landing_route]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Link -> form -> transaction -> confirmation with signed route. |
| 2 | Reversal / cancel / negative path | Invalid token: NotFound on form, Forbidden on transaction; token of another commercial partner: AccessError. |
| 3 | Multi-company / data scope | Company passed in link; _can_partner_pay_in_company; providers have company rule. |
| 4 | Side effects and cross-module triggers | Monitored tx stored in session; token charge immediate unless delay_token_charge; cron picks up later. |
| 5 | Configuration and optionality | Providers published/enabled; tokenisation flags on provider and method; delay_token_charge context. |
| 6 | Validation and constraints | HMAC; kwargs whitelist; currency active; int/float casts. |
| 7 | Roles and permissions | Public routes; token archive route requires user; link wizard has staff ACL; no explicit group on link generation observed beyond ACL. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — initiation itself is user-driven (post-processing is CAP-02). |
| 9 | Exception and failure behaviour | Invalid inputs -> ValidationError/Forbidden/NotFound. |
| 10 | Accounting, audit and security implications | HMAC binds partner, amount, currency only; saved tokens exposed to link bearer; landing_route client-supplied. See claims flagged RT. |

### DB reconciliation (configuration only)
Dump: payment_transaction 0 rows; payment_token 0 rows; 1 custom provider enabled and published, 1 demo provider in test, 23 providers with empty code disabled; ACL rows L2-13 match the CSV; rules: provider company, transaction company, token user and company, capture wizard.

### Unknown / runtime list
- Runtime behaviour of redirect to arbitrary landing_route values; whether the framework front-end validates landing_route; checkout flows of consuming modules (sale, account_payment) not studied here.
- All claims flagged RT in the table below.

## CAP-U45-02 Payment attempt lifecycle, amount validation and background completion

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A payment attempt moves through draft, pending, authorized, done, cancelled or error as provider notifications arrive; amounts and currencies are checked; completed attempts are post-processed in the browser poll and by a background job.

### D2 Architecture, data and object relationships
payment.transaction (state, operation, is_post_processed, is_live, parent/child), provider notification handling, post-processing controller, cron on payment.transaction.

### D3 Source, technical and workflow logic
_process: _validate_amount -> _apply_updates -> _tokenize. State setters guard allowed source states; _update_state logs and ignores wrong-state requests, resets is_post_processed on a real change. /payment/status/poll post-processes the monitored tx and retries on DB conflicts. _cron_post_process retries within 4 days and commits per tx. _post_process in base only flags the tx.

State diagram:
- draft -> pending [_set_pending]
- draft -> authorized [_set_authorized]
- pending -> authorized [_set_authorized]
- draft|pending|authorized|error -> done [_set_done]
- draft|pending|authorized -> cancel [_set_canceled]
- draft|pending|authorized -> error [_set_error]
- done -> post-processed [_post_process via poll or cron]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Notification -> validate -> state change -> tokenise -> post-process. |
| 2 | Reversal / cancel / negative path | Cancel/error setters from non-final states; wrong-state requests ignored with warning; amount/currency mismatch -> error. |
| 3 | Multi-company / data scope | Transaction company rule; cron runs as root user across companies. |
| 4 | Side effects and cross-module triggers | Source tx state updated from child tx; tokens created; business effects from overrides in other modules. |
| 5 | Configuration and optionality | Provider can opt out of amount validation; cron active only when a provider is enabled/test. |
| 6 | Validation and constraints | State machine guards; authorized-state constraint; token must be active. |
| 7 | Roles and permissions | Poll route is public with session-held id; model ACL read/write for staff per DB. |
| 8 | Scheduled / automated behaviour | Cron every 10 minutes, 4-day window, commit per transaction. |
| 9 | Exception and failure behaviour | Poll route rolls back and returns retry on concurrency errors. |
| 10 | Accounting, audit and security implications | SENSITIVE_KEYS empty; reconciliation effects are in account_payment (not studied). |

### DB reconciliation (configuration only)
Dump: post-process cron active, 10 minutes; no transactions; cron declared inactive in XML and toggled by provider create/write.

### Unknown / runtime list
- Content of runtime logs; interaction with account_payment post-processing; provider-specific notification parsing.
- All claims flagged RT in the table below.

## CAP-U45-03 Capture, void and refund of payments

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
An authorized payment can be captured (fully or partially) or voided; a completed payment can be refunded. Each follow-up is recorded as a child payment attempt.

### D2 Architecture, data and object relationships
payment.transaction (child transactions with R- and P- reference prefixes), payment.capture.wizard (transient), provider capability flags.

### D3 Source, technical and workflow logic
action_capture checks write rights, opens the wizard if a provider supports partial capture, otherwise captures in sudo. Wizard action_capture loops over authorized sources, captures min(remaining, amount), voids remainder when asked, running _capture/_void in sudo. action_void only on authorized; action_refund only on done with no amount cap in base. _create_child_transaction negates refund amounts.

State diagram:
- authorized -> done [capture of child tx]
- authorized -> cancel [void]
- done -> refund child created [action_refund]
- child draft -> error [ValidationError in _capture/_void/_refund]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Authorize -> capture -> done; or void. |
| 2 | Reversal / cancel / negative path | Void for remaining amount; refund child with negative amount; failures recorded as error. |
| 3 | Multi-company / data scope | Capture wizard rule; transaction company rule. |
| 4 | Side effects and cross-module triggers | Child tx created; provider API call via overrides. |
| 5 | Configuration and optionality | Partial capture only for providers that support it; void-after-capture option. |
| 6 | Validation and constraints | Amount between 0 and available; non-partial providers must capture fully; provider not disabled. |
| 7 | Roles and permissions | Model write check in action_capture; wizard itself has no rights check; wizard ACL per DB. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — manual user actions. |
| 9 | Exception and failure behaviour | Provider errors -> child tx error state, not exception. |
| 10 | Accounting, audit and security implications | No engine cap on refund amount; wizard runs _capture in sudo. |

### DB reconciliation (configuration only)
Dump: capture wizard rule present; no transactions to exercise the flows.

### Unknown / runtime list
- Provider-specific refund limits; accounting reversal done by account_payment; whether the capture wizard is reachable by users without write right on the transaction.
- All claims flagged RT in the table below.

## CAP-U45-04 Saved payment methods, providers and payment-method configuration

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Administrators enable providers and payment methods; customers may save methods as tokens for reuse and remove them. Disabling a provider or method archives dependent tokens.

### D2 Architecture, data and object relationships
payment.provider (state, is_published, company), payment.method (is_primary, brand links), payment.token (partner, provider_ref, payment_details, active), onboarding wizard.

### D3 Source, technical and workflow logic
provider create/write toggle the cron and archive tokens/methods on state change; _get_compatible_providers filters by state, publication, country, amount, currency, tokenisation, express checkout; token write forbids unarchiving with inactive method or disabled provider; archiving calls _handle_archiving in sudo.

State diagram:
- token active -> archived [provider disabled / method archived / user archive]
- provider disabled -> enabled|test [admin]
- provider published -> unpublished [action_toggle_is_published]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Enable provider -> methods activated -> customer saves token -> reuse. |
| 2 | Reversal / cancel / negative path | Archive token; disable provider archives tokens; delete blocked for master data. |
| 3 | Multi-company / data scope | Provider company rule; company change blocked once transactions exist. |
| 4 | Side effects and cross-module triggers | Cron toggled; methods activated/deactivated. |
| 5 | Configuration and optionality | State, published flag, tokenisation and capture flags. |
| 6 | Validation and constraints | Token never public partner; manual capture support check on method/provider. |
| 7 | Roles and permissions | ACL for system and users per DB; token user rule. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — no schedule specific to configuration. |
| 9 | Exception and failure behaviour | Writes refusing unarchive raise ValidationError/UserError. |
| 10 | Accounting, audit and security implications | Token display masked; token ownership by commercial partner. |

### DB reconciliation (configuration only)
Dump: 232 payment methods of which 2 active; 1 custom provider enabled; token table empty.

### Unknown / runtime list
- Per-provider onboarding contracts (provider modules not in this unit); payment_method write path partly summarised.
- All claims flagged RT in the table below.

## CAP-U45-05 Offline bank-transfer payment

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A customer chooses a manual bank transfer; the attempt becomes pending with instructions and a reference; staff reconcile funds later.

### D2 Architecture, data and object relationships
payment_custom provider code custom, mode wire_transfer, payment.transaction override, pending_msg, public process route.

### D3 Source, technical and workflow logic
Form posts the reference to /payment/custom/process (public, POST, csrf off) which sudo-processes the data: _search_by_reference then _apply_updates sets pending; amount check skipped; communication reference prefers invoice, order, then tx reference. action_recompute_pending_msg writes bank account labels into pending_msg.

State diagram:
- draft -> pending [customer submits process route]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Choose transfer -> pending -> staff reconcile outside the module. |
| 2 | Reversal / cancel / negative path | No automated cancel path in this module; engine cancel applies. |
| 3 | Multi-company / data scope | Provider company rule applies. |
| 4 | Side effects and cross-module triggers | Pending message includes journal bank accounts if account_payment installed. |
| 5 | Configuration and optionality | Method inactive by default; provider can be switched; qr_code option. |
| 6 | Validation and constraints | custom_mode required for custom provider. |
| 7 | Roles and permissions | Public route; no ACL for visitor; provider ACL as payment. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — no schedule specific to this module. |
| 9 | Exception and failure behaviour | Unknown reference -> engine logs warning. |
| 10 | Accounting, audit and security implications | Public csrf-off route moves draft tx to pending knowing the reference (INFERENCE, RT); bank account labels become HTML. |

### DB reconciliation (configuration only)
Dump: custom provider enabled and published; module installed; no transactions.

### Unknown / runtime list
- Whether the redirect form is the only way to reach the route; runtime effect of reference guessing; reconciliation in account_payment.
- All claims flagged RT in the table below.

## CAP-U45-06 Phone number normalisation and blacklist

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Numbers are normalised to an international standard form and stored for matching; a blacklist prevents unwanted messaging; users can add or remove numbers with a reason.

### D2 Architecture, data and object relationships
phone.blacklist (number unique, active, tracked), mail.thread.phone mixin (phone_sanitized stored, flags, search field), base helpers (_phone_format), tools using external phonenumbers library, res.users portal deactivation hook, remove wizard.

### D3 Source, technical and workflow logic
_phone_format picks country from the record, linked partner, else company country, then formats via the library (E164 by default). Blacklist create sanitises, dedupes, reactivates archived, skips existing. Mixin computes phone_sanitized from the first formatting number field, reads blacklist in sudo, searches via raw SQL with regexp normalisation; init creates indexes.

State diagram:
- not listed -> listed [add / create]
- listed -> archived [remove]
- archived -> listed [add reactivates]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Add number -> sanitised -> listed -> messaging excluded. |
| 2 | Reversal / cancel / negative path | Remove with reason archives; unknown numbers get inactive entries. |
| 3 | Multi-company / data scope | Blacklist has no company field observed; global list. |
| 4 | Side effects and cross-module triggers | Portal account deletion can blacklist numbers; messages posted as notes. |
| 5 | Configuration and optionality | External library required for validation; fallback returns numbers unchanged. |
| 6 | Validation and constraints | Unique number; invalid numbers rejected when library present. |
| 7 | Roles and permissions | Blacklist ACL none for all, full for system; unblock dialog checks write right. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — no scheduled behaviour. |
| 9 | Exception and failure behaviour | Invalid numbers -> UserError with reason; search under 3 characters -> UserError. |
| 10 | Accounting, audit and security implications | Blacklist is a privacy and consent control; sudo helpers; raw SQL search ignores record rules. |

### DB reconciliation (configuration only)
Dump: module installed; phone_blacklist 0 rows; ACL 3 rows as CSV.

### Unknown / runtime list
- All formatting outcomes are RT because the external library is absent on the host; behaviour of metadata patches by version; consumers (SMS, marketing) are separate modules.
- All claims flagged RT in the table below.

## CAP-U45-07 Customer-portal ratings and publisher replies

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Ratings appear inside portal conversations with statistics, and authorised staff can publish a reply to a rating.

### D2 Architecture, data and object relationships
rating.rating extended with publisher_comment/id/datetime; mail.message portal formatting; portal chatter filters; front-end patches.

### D3 Source, technical and workflow logic
Portal message format optionally adds rating info read in sudo; rating create/write stamp publisher and time when a comment is set after a rights check (website editor group or write access on the rated record). Controller /website/rating/comment writes under the caller's rules.

State diagram:
- rating -> rating with reply [comment published]
- rating with reply -> rating [comment blanked, check skipped]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Customer rates -> staff replies -> portal shows reply. |
| 2 | Reversal / cancel / negative path | Blank comment clears reply without extra check. |
| 3 | Multi-company / data scope | No company logic in module. |
| 4 | Side effects and cross-module triggers | Messages shown with rating, statistics via sudo call. |
| 5 | Configuration and optionality | Rating include option; website editor group optional. |
| 6 | Validation and constraints | Rating 0 to 5 constraint is in the base rating module. |
| 7 | Roles and permissions | Internal users can write ratings; portal and public no access (rating module ACL). |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — no schedule. |
| 9 | Exception and failure behaviour | Invisible rating -> error dict. |
| 10 | Accounting, audit and security implications | Reply attribution (who, when) automatic; read in sudo. |

### DB reconciliation (configuration only)
Dump: rating_rating 0 rows; website installed so the editor group exists.

### Unknown / runtime list
- Front-end rendering not verified; record rules on rating not found; behaviour with portal users replying.
- All claims flagged RT in the table below.

## CAP-U45-08 Personal-data lookup, archive, delete and audit log

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A system administrator searches all stored data for a person by email and name, archives or deletes found records, and a masked audit entry is kept.

### D2 Architecture, data and object relationships
privacy.lookup.wizard and line (transient), privacy.log (masked name/email, execution details, found records).

### D3 Source, technical and workflow logic
_get_query builds one UNION ALL SQL over partners, users, authored messages and every stored table with email or partner references, excluding transient, virtual and listed models. Lines show a link only if the viewer can read the record. Archive and delete run in sudo and write execution details; _post_log creates or updates the log when details exist.

State diagram:
- found -> archived [is_active toggled]
- archived -> found [is_active toggled]
- found|archived -> deleted [action_unlink]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Open from contact -> lookup -> archive or delete -> log. |
| 2 | Reversal / cancel / negative path | Unarchive via toggle; deletion not reversible. |
| 3 | Multi-company / data scope | Query ignores record rules and company filters. |
| 4 | Side effects and cross-module triggers | Deleting cascades per model rules; messages by authors included. |
| 5 | Configuration and optionality | Wizard retained 24 hours; models excluded by blacklist hook. |
| 6 | Validation and constraints | Valid email required. |
| 7 | Roles and permissions | System group only for wizard and log. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — manual tool. |
| 9 | Exception and failure behaviour | Already unlinked raises UserError. |
| 10 | Accounting, audit and security implications | Log masks name/email but only written after action; log can be deleted by system group; lookup reads are not logged. |

### DB reconciliation (configuration only)
Dump: privacy_log 0 rows; 4 server actions.

### Unknown / runtime list
- Effect of deleting records with constraints at runtime; cross-module referential effects; whether views hide actions from non-system users.
- All claims flagged RT in the table below.

## CAP-U45-09 Product option configuration and variant grid

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Products carry option groups and values that generate variants and price surcharges; a grid lets users enter quantities across combinations; a bulk wizard updates values across products.

### D2 Architecture, data and object relationships
product.template.attribute.line, product.template.attribute.value, product.attribute.value, update wizard, product_matrix grid methods and JS dialog.

### D3 Source, technical and workflow logic
Line create/write/unlink keep value records and variants in sync (reactivate, archive fall-back). Value records forbid manual variant links, unique per product. Grid builds header from the first option line and rows from the cartesian product of the others with possibility flags and converted extra prices.

State diagram:
- value active -> archived [unlink fallback]
- line active -> archived [write active False or unlink fallback]
- archived -> active [re-added]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Add option group -> values -> variants generated -> grid entry. |
| 2 | Reversal / cancel / negative path | Delete falls back to archive; savepoints protect. |
| 3 | Multi-company / data scope | Company-domain read for default-price flag; templates company rules. |
| 4 | Side effects and cross-module triggers | Variants recreated; documents print grid. |
| 5 | Configuration and optionality | Option display and variant creation mode; display_extra option. |
| 6 | Validation and constraints | Active line needs a value; value must match option; uniqueness. |
| 7 | Roles and permissions | Product ACL: read for users, write for create group; wizard for managers; grid has no own ACL. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE — no schedule. |
| 9 | Exception and failure behaviour | Savepoint failures become archiving silently. |
| 10 | Accounting, audit and security implications | Price surcharges drive document amounts; wizard overwrites custom surcharges. |

### DB reconciliation (configuration only)
Dump: product_attribute 0 rows; product_template 16; implication of variant group by internal users present; grid consumers for sales and purchase installed.

### Unknown / runtime list
- Variant deletion vs archive in real data; sale and purchase grid consumers; rest of product_template and product_product ranges.
- All claims flagged RT in the table below.

## CAP-U45-10 Product helper tools and product-linked invoice email

**Function-ID:** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Labels, price list reports and exports, a catalog for adding products to orders, document upload on products, and automatic emails per product when a customer invoice is confirmed.

### D2 Architecture, data and object relationships
product.label.layout wizard, report classes, pricelist report model and export controller, catalog mixin and controller, document controller, product_email_template additions on product.template and account.move.

### D3 Source, technical and workflow logic
Label wizard builds report data; report model searches under user rules. Pricelist export parses client JSON and recomputes data. Catalog controller trusts client res_model and order_id. Document upload restricts to product models. Invoice _post override sends one message per line having a template.

State diagram:
- invoice draft -> posted -> product emails sent [_post]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Print labels, export price lists, add from catalog, upload documents, send invoice emails. |
| 2 | Reversal / cancel / negative path | NOT APPLICABLE — helper tools; email cannot be recalled. |
| 3 | Multi-company / data scope | Catalog uses order company; document records company. |
| 4 | Side effects and cross-module triggers | Emails posted on invoice chatter. |
| 5 | Configuration and optionality | Template per product; label layouts. |
| 6 | Validation and constraints | Positive quantity; model gate; csv export unescaped. |
| 7 | Roles and permissions | Product ACL; invoicing groups see the template field. |
| 8 | Scheduled / automated behaviour | Invoice posting triggers email each time. |
| 9 | Exception and failure behaviour | Upload errors returned as text. |
| 10 | Accounting, audit and security implications | Repeat emails; csv formula risk; client-chosen model names. |

### DB reconciliation (configuration only)
Dump: product_email_template installed, 0 products with template, 2 views; product ACL and rules as noted; product_pricelist 1.

### Unknown / runtime list
- Rest of product models; mail delivery outcome; report templates and views not read.
- All claims flagged RT in the table below.

## MODULE STATUS TABLE

| Module | Matrix status before | Claims (U45) | Capabilities covered | Assessment |
|---|---|---|---|---|
| payment | PARTIAL | 85 | CAP-U45-01, CAP-U45-02, CAP-U45-03, CAP-U45-04, CAP-U45-05 | PARTIAL — provider-specific flows, payment_method internals, onboarding wizards, QWeb/JS front-end and views not read; framework controllers, transaction engine, wizards and security read |
| payment_custom | PARTIAL | 19 | CAP-U45-05 | L3-READY (source level; runtime behaviour RT) |
| phone_validation | PARTIAL | 32 | CAP-U45-06 | PARTIAL — external phonenumbers library absent so all formatting is RT; view XML and library patch bodies only partly read |
| portal_rating | PARTIAL | 14 | CAP-U45-07 | PARTIAL — front-end JS/XML templates only pointer-read; base rating module outside this row |
| privacy_lookup | PARTIAL | 26 | CAP-U45-08 | L3-READY (source level; runtime reach across other modules RT) |
| product | PARTIAL | 43 | CAP-U45-09, CAP-U45-10 | PARTIAL — attribute-line and value machinery, label/pricelist/catalog/document helpers read; remaining product_template, product_product, pricelist and view/report-template ranges not read in this unit |
| product_email_template | PARTIAL | 6 | CAP-U45-10 | L3-READY (source level; small module fully read; mail delivery RT) |
| product_matrix | PARTIAL | 9 | CAP-U45-09 | PARTIAL — Python, report template and JS dialog/hook read; static XML dialog templates and sale/purchase grid consumers not read |

## CLAIMS

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U45-C001 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:38 | /payment/pay | FACT | payment installed | — | Public GET route for the payment form; access is gated by an HMAC access token when a partner id is supplied. | N-U45-001 |
| VDR-U45-C002 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:78 | raise NotFound | FACT | partner_id supplied | — | If a partner id is passed and the access token does not validate, the controller raises NotFound rather than Forbidden. | N-U45-002 |
| VDR-U45-C003 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:87 | partner_is_different | FACT | logged-in user | — | A logged-in user is always paid as their own partner; a differing partner id from the link only sets a flag (partner_is_different). | N-U45-003 |
| VDR-U45-C004 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:92 | browse(partner_id).exists() | FACT | anonymous visitor | — | Anonymous visitors use the partner browsed from the link id in sudo. | N-U45-004 |
| VDR-U45-C005 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:107 | currency | FACT | always | — | Currency is looked up and must exist and be active; otherwise the route refuses (NotFound). | N-U45-005 |
| VDR-U45-C006 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:128 | _get_available_tokens | FACT | always | — | Saved tokens of the partner are read in sudo to be offered on the form, even for a non-owner who holds a valid link. | N-U45-006 |
| VDR-U45-C007 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:159 | 'landing_route': '/payment/confirmation' | FACT | always | — | The default landing route in the payment context is /payment/confirmation. | N-U45-007 |
| VDR-U45-C008 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:258 | /payment/transaction | FACT | always | — | JSON-RPC public route that creates the transaction. | N-U45-008 |
| VDR-U45-C009 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:275 | check_access_token | FACT | always | — | check_access_token(access_token, partner_id, amount, currency_id) failing raises ValidationError->Forbidden. | N-U45-009 |
| VDR-U45-C010 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:481 | _validate_transaction_kwargs | FACT | always | — | A whitelist of kwargs (incl. landing_route and provider_id) is accepted from the client. | N-U45-010 |
| VDR-U45-C011 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:285 | def _create_transaction | FACT | always | — | _create_transaction orchestrates tokenisation, token ownership, validation amounts and sudo creation. | N-U45-011 |
| VDR-U45-C012 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:322 | tokenization_requested | INFERENCE | redirect or direct flow | — | Tokenize is set only if provider allows tokenization, the method supports it, and it is required or requested (L314-323). | N-U45-012 |
| VDR-U45-C013 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:331 | commercial_partner | FACT | token flow | — | Token flow compares the commercial partner of the token with the payer, else AccessError. | N-U45-013 |
| VDR-U45-C014 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:342 | is_validation | FACT | validation operation | — | For validation operations amount and currency come from the provider, not the client. | N-U45-014 |
| VDR-U45-C015 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:360 | 'landing_route': landing_route | FACT | always | — | The transaction is created in sudo and stores landing_route taken from the client request. | N-U45-015 |
| VDR-U45-C016 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:366 | delay_token_charge | FACT | token flow | — | Token flows are charged immediately unless context delay_token_charge is set. | N-U45-016 |
| VDR-U45-C017 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:370 | monitor_transaction | FACT | always | — | The new transaction is registered in the session for portal post-processing. | N-U45-017 |
| VDR-U45-C018 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:375 | def _update_landing_route | FACT | always | — | Appends tx_id and access_token (recomputed for validation) to the landing route. | N-U45-018 |
| VDR-U45-C019 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:394 | /payment/confirmation | FACT | always | — | Confirmation route verifies the HMAC against the transaction partner, amount and currency (L408-411). | N-U45-019 |
| VDR-U45-C020 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:436 | _cast_as_int | FACT | always | — | Helpers cast untrusted numeric inputs; failures become ValidationError. | N-U45-020 |
| VDR-U45-C021 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:466 | _can_partner_pay_in_company | FACT | always | — | Company-compatibility check for the payer. | N-U45-021 |
| VDR-U45-C022 | FUNCTION MAPPING REQUIRED | payment/utils.py:15 | def generate_access_token | FACT | always | — | HMAC over partner, amount, currency (joined by /) via hmac_tool with a superuser env. | N-U45-022 |
| VDR-U45-C023 | FUNCTION MAPPING REQUIRED | payment/utils.py:47 | consteq | FACT | always | — | check_access_token uses constant-time comparison. | N-U45-023 |
| VDR-U45-C024 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_link_wizard.py:22 | _get_default_payment_link_values | FACT | always | — | default_get uses context active_id/active_model and calls the hook on any model. | N-U45-024 |
| VDR-U45-C025 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_link_wizard.py:55 | def _compute_link | FACT | always | — | Builds /payment/pay with amount, access_token, currency_id, partner_id, company_id. | N-U45-025 |
| VDR-U45-C026 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_link_wizard.py:94 | access_token | INFERENCE | always | RT | The HMAC covers partner, amount and currency only (L94-98); company and reference are not bound, so a link could be re-used for another reference at the same amount. Needs runtime test. | N-U45-026 |
| VDR-U45-C027 | FUNCTION MAPPING REQUIRED | payment/models/res_partner.py:11 | payment_token_count | FACT | always | — | Partner has a count of saved tokens. | N-U45-027 |
| VDR-U45-C028 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:419 | /payment/archive_token | FACT | logged-in user | — | Archive-token route is restricted to the user's own or commercial partner tokens (L426-433). | N-U45-028 |
| VDR-U45-C029 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:193 | /my/payment_method | FACT | logged-in user | — | Authenticated route to manage saved methods. | N-U45-029 |
| VDR-U45-C030 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:67 | ('draft' | FACT | always | — | State selection draft, pending, authorized, done, cancel, error. | N-U45-030 |
| VDR-U45-C031 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:80 | online_redirect | FACT | always | — | Operation selection: online_redirect, online_direct, online_token, validation, offline, refund. | N-U45-031 |
| VDR-U45-C032 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:159 | _check_state_authorized_supported | FACT | always | — | Constraint: authorized state only for providers supporting manual capture. | N-U45-032 |
| VDR-U45-C033 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:171 | _check_token_is_active | FACT | always | — | Constraint: token on transaction must be active. | N-U45-033 |
| VDR-U45-C034 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:186 | is_live | FACT | always | — | create sets is_live = provider.state == 'enabled'. | N-U45-034 |
| VDR-U45-C035 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:738 | def _process | FACT | always | — | _process validates the amount, applies updates, then tokenizes when authorized or done. | N-U45-035 |
| VDR-U45-C036 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:759 | def _search_by_reference | FACT | always | — | Lookup by reference plus provider_code only (L774-776). | N-U45-036 |
| VDR-U45-C037 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:794 | def _validate_amount | FACT | always | — | Validation skipped for validation operations (L805) or when provider opts out (L809-810). | N-U45-037 |
| VDR-U45-C038 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:830 | rounding | FACT | always | — | Amount compared after rounding down with currency minor units (L829-837). | N-U45-038 |
| VDR-U45-C039 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:839 | currency | FACT | always | — | Currency mismatch between notification and transaction yields an error state. | N-U45-039 |
| VDR-U45-C040 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:876 | def _tokenize | FACT | tokenize flag | — | Creates a token from provider-extracted values; _extract_token_values returns {} by default (L902-913). | N-U45-040 |
| VDR-U45-C041 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:915 | def _set_pending | FACT | always | — | _set_pending allowed only from draft. | N-U45-041 |
| VDR-U45-C042 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:932 | def _set_authorized | FACT | always | — | _set_authorized from draft or pending. | N-U45-042 |
| VDR-U45-C043 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:949 | def _set_done | FACT | always | — | _set_done from draft, pending, authorized or error. | N-U45-043 |
| VDR-U45-C044 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:967 | def _set_canceled | FACT | always | — | _set_canceled from draft, pending, authorized. | N-U45-044 |
| VDR-U45-C045 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:985 | def _set_error | FACT | always | — | _set_error from draft, pending, authorized. | N-U45-045 |
| VDR-U45-C046 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1002 | def _update_state | FACT | always | — | Wrong-state requests are logged as a warning and ignored (L1041-1051); successful write resets is_post_processed (L1056). | N-U45-046 |
| VDR-U45-C047 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1060 | _update_source_transaction_state | FACT | child transaction | — | Child transactions propagate state to the source transaction. | N-U45-047 |
| VDR-U45-C048 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1082 | def _cron_post_process | FACT | always | — | Cron retries unprocessed transactions within 4 days (L1092) and commits per transaction (L1102). | N-U45-048 |
| VDR-U45-C049 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1112 | def _post_process | FACT | always | — | Base _post_process only flags is_post_processed; business effects are in overrides in other modules. | N-U45-049 |
| VDR-U45-C050 | FUNCTION MAPPING REQUIRED | payment/controllers/post_processing.py:41 | /payment/status/poll | FACT | always | — | Poll route post-processes the monitored tx; rolls back and raises 'retry' on OperationalError/IntegrityError (L56-60). | N-U45-050 |
| VDR-U45-C051 | FUNCTION MAPPING REQUIRED | payment/controllers/post_processing.py:84 | _get_monitored_transaction | FACT | always | — | Monitored transaction id lives in session and is read in sudo. | N-U45-051 |
| VDR-U45-C052 | FUNCTION MAPPING REQUIRED | payment/data/payment_cron.xml:8 | _cron_post_process | OBSERVATION | DB dump | — | Cron declared inactive, 10 min, user root; DB shows it active because a provider is not disabled. | N-U45-052 |
| VDR-U45-C053 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:396 | def _toggle_post_processing_cron | FACT | always | — | Cron active iff any provider is not disabled. | N-U45-053 |
| VDR-U45-C054 | FUNCTION MAPPING REQUIRED | payment/const.py:9 | SENSITIVE_KEYS | FACT | always | — | SENSITIVE_KEYS is an empty set in the base module. | N-U45-054 |
| VDR-U45-C055 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1162 | def _log_ | UNKNOWN | always | RT | Logging helpers L1162-1191 were read superficially; exact content of logged payloads is runtime-dependent. | N-U45-055 |
| VDR-U45-C056 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:266 | def action_capture | FACT | always | — | action_capture checks write rights (L273) then opens partial wizard if a provider supports partial, otherwise captures authorized txs in sudo (L290-294). | N-U45-056 |
| VDR-U45-C057 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:273 | check_rights_on_recordset | FACT | always | — | Rights check on recordset = check_access('write'). | N-U45-057 |
| VDR-U45-C058 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:296 | def action_void | FACT | authorized state | — | Only authorized txs; voids amount minus done captured children. | N-U45-058 |
| VDR-U45-C059 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:313 | def action_refund | FACT | done state | — | Only done txs; engine imposes no amount cap (L321-322). | N-U45-059 |
| VDR-U45-C060 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:699 | def _create_child_transaction | FACT | always | — | Refund prefix R-, amount negated (L715-718); P- prefix for partial capture or void. | N-U45-060 |
| VDR-U45-C061 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:687 | def _ensure_provider_is_not_disabled | FACT | always | — | Each of _capture/_void/_refund ensures the provider is not disabled. | N-U45-061 |
| VDR-U45-C062 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:591 | def _capture | FACT | always | — | On ValidationError the child tx is set to error. | N-U45-062 |
| VDR-U45-C063 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_capture_wizard.py:14 | active_ids | FACT | always | — | transaction_ids default from context active_ids (L12-16). | N-U45-063 |
| VDR-U45-C064 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_capture_wizard.py:81 | _compute_is_amount_to_capture_valid | FACT | always | — | Valid when 0 < amount <= available. | N-U45-064 |
| VDR-U45-C065 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_capture_wizard.py:131 | def action_capture | FACT | always | — | Loops authorized source txs, captures min(remaining, amount), voids remainder if requested, runs _capture/_void in sudo (L146, L155); wizard has no rights check. | N-U45-065 |
| VDR-U45-C066 | FUNCTION MAPPING REQUIRED | payment/wizards/payment_capture_wizard.py:87 | support_partial_capture | FACT | always | — | Non-partial providers require a full capture (constraint L111-127). | N-U45-066 |
| VDR-U45-C067 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:39 | payment_capture_wizard | FACT | always | — | Record rule on capture wizard. | N-U45-067 |
| VDR-U45-C068 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:76 | def write | FACT | always | — | Cannot unarchive tokens whose method is inactive or provider disabled; archiving calls _handle_archiving in sudo. | N-U45-068 |
| VDR-U45-C069 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:101 | _check_partner_is_never_public | FACT | always | — | Tokens may never belong to the public partner. | N-U45-069 |
| VDR-U45-C070 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:119 | def _get_available_tokens | FACT | always | — | Validation mode includes tokens of the commercial partner. | N-U45-070 |
| VDR-U45-C071 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:170 | padding | FACT | always | — | Display name pads with bullets to hide all but the last digits. | N-U45-071 |
| VDR-U45-C072 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:337 | def create | FACT | always | — | create toggles the post-processing cron. | N-U45-072 |
| VDR-U45-C073 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:344 | def write | FACT | always | — | write archives tokens when state moves away from non-disabled (L348-352), deactivates unsupported methods on disable, activates default methods on enable. | N-U45-073 |
| VDR-U45-C074 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:555 | def _get_compatible_providers | FACT | always | — | States enabled/test (L582); non-internal users see only published (L587-588); country, max amount, currency, tokenization, express checkout filters (L592-663). | N-U45-074 |
| VDR-U45-C075 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:624 | max_amount | FACT | always | — | Max amount compared in company currency (L608-625). | N-U45-075 |
| VDR-U45-C076 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:692 | def _get_validation_amount | FACT | always | — | _get_validation_amount returns 0.0 by default. | N-U45-076 |
| VDR-U45-C077 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:531 | def action_toggle_is_published | FACT | always | — | Cannot publish a disabled provider. | N-U45-077 |
| VDR-U45-C078 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:463 | def _unlink_except_master_data | FACT | always | — | Provider deletion guarded for master data. | N-U45-078 |
| VDR-U45-C079 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:503 | def action_reset_credentials | FACT | always | — | Resets credentials for the provider. | N-U45-079 |
| VDR-U45-C080 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:306 | company | FACT | always | — | Company change blocked when transactions exist (L306-318). | N-U45-080 |
| VDR-U45-C081 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:22 | payment_token | FACT | always | — | Token rules: user-owned rule and company rule. | N-U45-081 |
| VDR-U45-C082 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:4 | payment_provider | OBSERVATION | DB dump | — | ACL rows in the dump equal the CSV rows L2-13. | N-U45-082 |
| VDR-U45-C083 | FUNCTION MAPPING REQUIRED | payment/data/neutralize.sql:2 | payment_provider | FACT | neutralize run | — | Neutralization sets enabled providers to disabled. | N-U45-083 |
| VDR-U45-C084 | FUNCTION MAPPING REQUIRED | payment/__init__.py:9 | setup_provider | FACT | install | — | post_init_hook setup_provider and uninstall reset_payment_provider. | N-U45-084 |
| VDR-U45-C085 | FUNCTION MAPPING REQUIRED | payment_custom/__init__.py:10 | setup_provider | FACT | install | — | post_init hook registers provider code custom with custom_mode wire_transfer. | N-U45-085 |
| VDR-U45-C086 | FUNCTION MAPPING REQUIRED | payment_custom/const.py:5 | wire_transfer | FACT | always | — | Default payment method code for custom provider is wire_transfer. | N-U45-086 |
| VDR-U45-C087 | FUNCTION MAPPING REQUIRED | payment_custom/data/payment_method_data.xml:4 | wire_transfer | FACT | always | — | wire_transfer method inactive by default; no tokenization, express checkout, capture or refund support (L4-14). | N-U45-087 |
| VDR-U45-C088 | FUNCTION MAPPING REQUIRED | payment_custom/data/payment_provider_data.xml:4 | payment_provider_transfer | FACT | always | — | Configures payment.payment_provider_transfer as custom/wire_transfer (L4-19). | N-U45-088 |
| VDR-U45-C089 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:20 | custom_mode | FACT | provider code custom | — | custom_mode required when code is custom; CHECK constraint L12-15. | N-U45-089 |
| VDR-U45-C090 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:25 | qr_code | FACT | always | — | qr_code boolean on provider. | N-U45-090 |
| VDR-U45-C091 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:33 | pending_msg | FACT | wire_transfer mode | — | create clears pending_msg for wire_transfer so it is regenerated (L30-34). | N-U45-091 |
| VDR-U45-C092 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:45 | def action_recompute_pending_msg | FACT | account_payment installed | — | Builds HTML from journal bank accounts' display names into pending_msg (L45-62); only when account_payment installed. | N-U45-092 |
| VDR-U45-C093 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:36 | def _get_default_payment_method_codes | FACT | always | — | Default method codes by custom_mode. | N-U45-093 |
| VDR-U45-C094 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:80 | def _transfer_ensure_pending_msg_is_set | FACT | always | — | Ensures pending message exists for transfer providers. | N-U45-094 |
| VDR-U45-C095 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:14 | /payment/custom/process | FACT | always | — | _process_url '/payment/custom/process'. | N-U45-095 |
| VDR-U45-C096 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:16 | csrf=False | FACT | always | — | Route is public, POST, csrf=False. | N-U45-096 |
| VDR-U45-C097 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:19 | _process('custom', post) | FACT | always | — | Calls payment.transaction sudo()._process('custom', post) with client-supplied data; logs post data (L18); redirects to /payment/status. | N-U45-097 |
| VDR-U45-C098 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:775 | Domain('provider_code' | INFERENCE | custom provider | RT | Matching is by reference plus provider_code only (payment/models/payment_transaction.py:774-776), so anyone who knows a draft custom transaction reference can move it to pending. Needs runtime test. | N-U45-098 |
| VDR-U45-C099 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:15 | def _get_specific_rendering_values | FACT | always | — | Returns api_url and reference for the redirect form (L15-30). | N-U45-099 |
| VDR-U45-C100 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:32 | def _get_communication | FACT | always | — | Communication: invoice payment_reference, then sale order reference, then tx reference (L32-48). | N-U45-100 |
| VDR-U45-C101 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:50 | def _extract_amount_data | FACT | always | — | Returns None for custom, skipping amount validation. | N-U45-101 |
| VDR-U45-C102 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:56 | def _apply_updates | FACT | custom provider | — | _apply_updates sets the transaction pending (L56-64). | N-U45-102 |
| VDR-U45-C103 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:66 | def _log_received_message | FACT | custom provider | — | Received-message log is skipped for custom. | N-U45-103 |
| VDR-U45-C104 | FUNCTION MAPPING REQUIRED | payment_custom/views/payment_custom_templates.xml:27 | Finalize your payment | UNKNOWN | always | RT | Template wording shown when pending was seen but rendering output not verified. | N-U45-104 |
| VDR-U45-C105 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:17 | def phone_parse | FACT | phonenumbers installed | RT | Parses twice (second after international formatting to apply metadata patches) (L20-24). | N-U45-105 |
| VDR-U45-C106 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:30 | is_possible_number | FACT | phonenumbers installed | RT | Impossible numbers give specific errors: bad country prefix, too short, too long, otherwise generic (L30-55). | N-U45-106 |
| VDR-U45-C107 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:43 | removeprefix | FACT | phonenumbers installed | RT | TOO_LONG numbers starting 00 or lacking + are retried with a + prefix (L39-53). | N-U45-107 |
| VDR-U45-C108 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:56 | is_valid_number | FACT | phonenumbers installed | RT | Possible-but-invalid numbers are rejected as probable wrong prefix (L56-57). | N-U45-108 |
| VDR-U45-C109 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:61 | def phone_format | FACT | phonenumbers installed | RT | E164 and RFC3966 forced; INTERNATIONAL if requested or country differs; else NATIONAL (L83-90). | N-U45-109 |
| VDR-U45-C110 | FUNCTION MAPPING REQUIRED | phone_validation/tools/phone_validation.py:112 | except ImportError | FACT | phonenumbers absent | RT | Fallback phone_format returns number unchanged and phone_parse returns False; one info log (L117-125). | N-U45-110 |
| VDR-U45-C111 | FUNCTION MAPPING REQUIRED | phone_validation/models/models.py:53 | def _phone_format | FACT | always | — | Country falls back to the company country when no record country (L89-90); formats via _phone_format_number. | N-U45-111 |
| VDR-U45-C112 | FUNCTION MAPPING REQUIRED | phone_validation/models/models.py:23 | def _phone_get_country | FACT | always | — | Country from the record's country field, else the first country among related partners (L35-45). | N-U45-112 |
| VDR-U45-C113 | FUNCTION MAPPING REQUIRED | phone_validation/models/models.py:110 | raise_exception | FACT | always | — | UserError from formatting is swallowed to False unless raise_exception (L112-115). | N-U45-113 |
| VDR-U45-C114 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:18 | _unique_number | FACT | always | — | Unique constraint on number. | N-U45-114 |
| VDR-U45-C115 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:24 | def create | FACT | always | — | create sanitises numbers to E164, dedupes, reactivates archived entries, skips existing, preserves order (L30-59). | N-U45-115 |
| VDR-U45-C116 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:35 | _phone_format(number=value['number'], raise_exception=True) | FACT | always | — | Invalid numbers abort create with a wrapped UserError. | N-U45-116 |
| VDR-U45-C117 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:61 | def write | FACT | always | — | write re-sanitises a changed number. | N-U45-117 |
| VDR-U45-C118 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:70 | def _search_number | FACT | always | — | Search value is sanitised before comparing. | N-U45-118 |
| VDR-U45-C119 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:108 | def _remove | FACT | always | — | Removal archives existing entries, or creates inactive entries for unknown numbers (L112-127). | N-U45-119 |
| VDR-U45-C120 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:100 | mail.mt_note | FACT | always | — | Add and remove post a note message with the given reason (L98-101, L122-125). | N-U45-120 |
| VDR-U45-C121 | FUNCTION MAPPING REQUIRED | phone_validation/models/phone_blacklist.py:15 | tracking=True | FACT | always | — | Number and active are tracked. | N-U45-121 |
| VDR-U45-C122 | FUNCTION MAPPING REQUIRED | phone_validation/security/ir.model.access.csv:2 | access_phone_blacklist_all | FACT | always | — | Everyone: no access; system group: full on blacklist and its removal wizard. | N-U45-122 |
| VDR-U45-C123 | FUNCTION MAPPING REQUIRED | phone_validation/wizard/phone_blacklist_remove.py:14 | def action_unblacklist_apply | FACT | always | — | Wizard builds a reason message and calls _remove. | N-U45-123 |
| VDR-U45-C124 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:36 | phone_sanitized | FACT | always | — | phone_sanitized stored computed with compute_sudo for fast comparison. | N-U45-124 |
| VDR-U45-C125 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:173 | def _compute_phone_sanitized | FACT | always | — | Takes the first number field that formats successfully (L176-181). | N-U45-125 |
| VDR-U45-C126 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:184 | def _compute_blacklisted | INFERENCE | always | RT | Reads blacklist in sudo (L187); only one sanitized value per record, last field wins for phone_blacklisted (L197-198). | N-U45-126 |
| VDR-U45-C127 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:202 | def _search_phone_sanitized_blacklisted | FACT | always | — | Raw SQL join on phone_blacklist where active; supports in and not in only. | N-U45-127 |
| VDR-U45-C128 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:119 | _phone_search_min_length | FACT | always | — | Searching needs at least 3 characters or UserError (L119-120). | N-U45-128 |
| VDR-U45-C129 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:130 | REGEXP_REPLACE | FACT | always | — | Phone search strips punctuation via SQL regexp and matches +/00 variants; values are bound parameters while column names come from the model (L122-170). | N-U45-129 |
| VDR-U45-C130 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:70 | def init | FACT | always | — | init creates partial btree and trigram indexes on regex-normalised phone columns (L75-92). | N-U45-130 |
| VDR-U45-C131 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:242 | def _phone_set_blacklisted | FACT | always | — | Set/reset blacklisted run in sudo. | N-U45-131 |
| VDR-U45-C132 | FUNCTION MAPPING REQUIRED | phone_validation/models/mail_thread_phone.py:251 | has_access('write') | FACT | always | — | Unblacklist action checks write access then raises AccessError (L248-261). | N-U45-132 |
| VDR-U45-C133 | FUNCTION MAPPING REQUIRED | phone_validation/models/res_users.py:10 | def _deactivate_portal_user | FACT | request_blacklist flag | — | Deleting a portal account may blacklist the user's numbers, with a log message naming the deleter (L10-32). | N-U45-133 |
| VDR-U45-C134 | FUNCTION MAPPING REQUIRED | phone_validation/models/res_partner.py:11 | _onchange_phone_validation | FACT | form edit | — | Phone onchange reformats to INTERNATIONAL, keeping the original if formatting fails. | N-U45-134 |
| VDR-U45-C135 | FUNCTION MAPPING REQUIRED | phone_validation/lib/phonenumbers_patch/__init__.py:40 | register_region_loader('CI' | FACT | phonenumbers installed, old library version | RT | Region metadata loaders for several countries are registered only when the library version is older than a threshold; also a Brazilian monkey patch follows (L38-110). Effect depends on installed library version, absent on host. | N-U45-135 |
| VDR-U45-C136 | FUNCTION MAPPING REQUIRED | phone_validation/lib/phonenumbers_patch/__init__.py:70 | MONKEY PATCHING | UNKNOWN | phonenumbers installed | RT | Which countries end up with corrected number rules depends on the installed library version, which is not available on the host. | N-U45-136 |
| VDR-U45-C137 | FUNCTION MAPPING REQUIRED | portal_rating/models/mail_message.py:18 | rating_include | FACT | portal installed | — | Rating properties are added to message format only when option rating_include is passed. | N-U45-137 |
| VDR-U45-C138 | FUNCTION MAPPING REQUIRED | portal_rating/models/mail_message.py:34 | sudo().search_read | FACT | always | — | Ratings for the messages are read in sudo. | N-U45-138 |
| VDR-U45-C139 | FUNCTION MAPPING REQUIRED | portal_rating/models/mail_message.py:47 | rating_get_stats | FACT | model has rating_get_stats | — | Statistics added by sudo call when the record defines rating_get_stats (L47-48). | N-U45-139 |
| VDR-U45-C140 | FUNCTION MAPPING REQUIRED | portal_rating/models/mail_message.py:63 | publisher_avatar | FACT | always | — | Builds avatar URL, blanks missing comment, formats datetime (L62-67). | N-U45-140 |
| VDR-U45-C141 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:8 | publisher_comment | FACT | always | — | Adds publisher_comment, publisher_id, publisher_datetime; publisher fields readonly. | N-U45-141 |
| VDR-U45-C142 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:44 | def _synchronize_publisher_values | FACT | always | — | When a comment is set, checks rights and defaults datetime to now and publisher to current user's partner (L48-53). | N-U45-142 |
| VDR-U45-C143 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:32 | website.group_website_restricted_editor | FACT | website group exists | RT | Passes if user is website restricted editor; otherwise requires write access on the rated record (L32-42). | N-U45-143 |
| VDR-U45-C144 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:41 | Updating rating comment require write access | FACT | always | — | AccessError message when rights missing. | N-U45-144 |
| VDR-U45-C145 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:23 | def write | INFERENCE | comment blanked | RT | Check runs only when publisher_comment is truthy (L48), so blanking a comment skips the extra check; only model access rules apply. Needs runtime test. | N-U45-145 |
| VDR-U45-C146 | FUNCTION MAPPING REQUIRED | portal_rating/controllers/portal_rating.py:10 | /website/rating/comment | FACT | logged-in user | — | jsonrpc route auth=user searches rating under the caller's rules, then writes comment (L12-18). | N-U45-146 |
| VDR-U45-C147 | FUNCTION MAPPING REQUIRED | portal_rating/controllers/portal_rating.py:17 | Invalid rating | FACT | always | — | Returns an error dict (not exception) if the rating is not visible. | N-U45-147 |
| VDR-U45-C148 | FUNCTION MAPPING REQUIRED | portal_rating/controllers/portal_chatter.py:7 | rating_value | FACT | always | — | Non-empty message domain widened to include messages with rating_value. | N-U45-148 |
| VDR-U45-C149 | FUNCTION MAPPING REQUIRED | portal_rating/controllers/portal_chatter.py:12 | float(data['rating_value']) | FACT | rating filter | — | Optional filter on rating value, cast with float(). | N-U45-149 |
| VDR-U45-C150 | FUNCTION MAPPING REQUIRED | portal_rating/__manifest__.py:21 | auto_install | FACT | always | — | Bridge module auto-installs when portal and rating are present. | N-U45-150 |
| VDR-U45-C151 | FUNCTION MAPPING REQUIRED | rating/security/ir.model.access.csv:2 | access_rating_user | FACT | rating installed | — | Internal users have read, write and create (no delete) on ratings; public and portal have none; system has full (CSV L2-5). Discovered supporting module rating. | N-U45-151 |
| VDR-U45-C152 | FUNCTION MAPPING REQUIRED | rating/models/rating.py:57 | _rating_range | FACT | rating installed | — | Rating value constrained 0 to 5. | N-U45-152 |
| VDR-U45-C153 | FUNCTION MAPPING REQUIRED | rating/models/rating.py:142 | OPW-2181568 | FACT | rating installed | — | Deleting a rating also deletes its chatter message. | N-U45-153 |
| VDR-U45-C154 | FUNCTION MAPPING REQUIRED | rating/models/rating.py:134 | def write | UNKNOWN | rating installed | RT | Whether record rules restrict which ratings internal staff may edit is not confirmed; DB showed zero rating rows and no record rule was identified for rating records. | N-U45-154 |
| VDR-U45-C155 | FUNCTION MAPPING REQUIRED | privacy_lookup/models/res_partner.py:10 | def action_privacy_lookup | FACT | always | — | Contact action opens the lookup wizard prefilled with name and email. | N-U45-155 |
| VDR-U45-C156 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:49 | email_normalize | FACT | always | — | Invalid email raises UserError before querying (L50-51). | N-U45-156 |
| VDR-U45-C157 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:55 | WITH indirect_references | FACT | always | — | CTE selects partners matching normalised email or name ilike (L55-59). | N-U45-157 |
| VDR-U45-C158 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:71 | FROM res_users | FACT | always | — | Users matched on login ilike or linked partner email/name ilike (L72-78). | N-U45-158 |
| VDR-U45-C159 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:85 | FROM mail_message | FACT | always | — | Messages authored by matched partners are included (L85-86). | N-U45-159 |
| VDR-U45-C160 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:33 | def _get_query_models_blacklist | FACT | always | — | Skips res.partner, res.users, notifications, followers, channel members, messages. | N-U45-160 |
| VDR-U45-C161 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:105 | model._transient or not model._auto | FACT | always | — | Transient and non-table models skipped. | N-U45-161 |
| VDR-U45-C162 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:112 | 'email_from', 'company_email' | FACT | always | — | Scans stored fields email_normalized, email, email_from, company_email; matches rec_name char with name ilike (L112-130). | N-U45-162 |
| VDR-U45-C163 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:142 | field.ondelete != 'cascade' | FACT | always | — | Includes many2one to res.partner that are not ondelete cascade (L133-143). | N-U45-163 |
| VDR-U45-C164 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:168 | self.env.cr.execute(query) | FACT | always | — | Raw SQL executes across tables; no record rules or company filter in query. | N-U45-164 |
| VDR-U45-C165 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:157 | search([('model', '=', model_name)]).id | INFERENCE | always | RT | The ir.model search under caller; with ilike on name unescaped (L59, L78) a name with wildcard characters broadens matches. Needs runtime test. | N-U45-165 |
| VDR-U45-C166 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:257 | check_access('read') | FACT | always | — | Line resource_ref shown only if the user can read the record, otherwise None (L254-262). | N-U45-166 |
| VDR-U45-C167 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:289 | def _onchange_is_active | FACT | always | — | Archive toggle writes active in sudo and logs 'Archived/Unarchived' detail (L293-295). | N-U45-167 |
| VDR-U45-C168 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:297 | def action_unlink | FACT | always | — | Delete runs in sudo, records 'Deleted' detail, flags is_unlinked; refuses if already unlinked (L299-303). | N-U45-168 |
| VDR-U45-C169 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:312 | def action_unlink_all | FACT | always | — | Bulk delete loops all lines not yet unlinked. | N-U45-169 |
| VDR-U45-C170 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:305 | def action_archive_all | FACT | always | — | Bulk archive for lines with active flag and still active. | N-U45-170 |
| VDR-U45-C171 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:173 | def _post_log | FACT | always | — | Log created only when execution_details non-empty; otherwise updates existing log (L175-184). | N-U45-171 |
| VDR-U45-C172 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:193 | def _compute_records_description | FACT | always | — | Description lists models, counts and ids; technical names shown to debug-mode users (L201-205). | N-U45-172 |
| VDR-U45-C173 | FUNCTION MAPPING REQUIRED | privacy_lookup/wizard/privacy_lookup_wizard.py:15 | _transient_max_hours | FACT | always | — | Wizard and lines are transient, 24h retention. | N-U45-173 |
| VDR-U45-C174 | FUNCTION MAPPING REQUIRED | privacy_lookup/models/privacy_log.py:30 | def _anonymize_name | FACT | always | — | Name masked to initial plus asterisks per word (L35). | N-U45-174 |
| VDR-U45-C175 | FUNCTION MAPPING REQUIRED | privacy_lookup/models/privacy_log.py:41 | gmail.com | FACT | always | — | Common free-mail domains kept in clear; other domain labels masked except last (L41-44). | N-U45-175 |
| VDR-U45-C176 | FUNCTION MAPPING REQUIRED | privacy_lookup/models/privacy_log.py:46 | return UserError | FACT | always | — | _anonymize_email returns (does not raise) a UserError instance when label has no @ (L45-46); create would then store the exception object. | N-U45-176 |
| VDR-U45-C177 | FUNCTION MAPPING REQUIRED | privacy_lookup/models/privacy_log.py:24 | def create | FACT | always | — | create masks name and email on every log. | N-U45-177 |
| VDR-U45-C178 | FUNCTION MAPPING REQUIRED | privacy_lookup/security/ir.model.access.csv:4 | access_privacy_log | FACT | always | — | System group only: full on wizard and log; lines no delete (CSV L2-4). | N-U45-178 |
| VDR-U45-C179 | FUNCTION MAPPING REQUIRED | privacy_lookup/security/ir.model.access.csv:4 | access_privacy_log | INFERENCE | always | RT | System group holds unlink on the audit log, so the audit trail can be deleted by the same role that deletes data. | N-U45-179 |
| VDR-U45-C180 | FUNCTION MAPPING REQUIRED | privacy_lookup/data/ir_actions_server_data.xml:3 | ir.actions.server | OBSERVATION | DB dump | — | Four server actions in dump; 0 log rows. | N-U45-180 |
| VDR-U45-C181 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:61 | def _check_valid_values | FACT | always | — | Active attribute line must have at least one value, and every value must belong to the line's attribute (L60-78). | N-U45-181 |
| VDR-U45-C182 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:81 | def create | FACT | always | — | create reactivates an archived line of the same template and attribute instead of inserting (L98-109), then updates values and variants (L113-114). | N-U45-182 |
| VDR-U45-C183 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:129 | cannot move the attribute | FACT | always | — | write refuses changing template or attribute of an existing line (L125-145). | N-U45-183 |
| VDR-U45-C184 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:149 | Command.clear() | FACT | always | — | Archiving a line clears its values (L148-149). | N-U45-184 |
| VDR-U45-C185 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:160 | def unlink | FACT | always | — | unlink removes values first, deletes in savepoint, archives lines that cannot be deleted, then recreates variants (L174-191). | N-U45-185 |
| VDR-U45-C186 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:183 | except Exception | FACT | always | — | All exceptions are swallowed in unlink and turned into archiving (L183-186). | N-U45-186 |
| VDR-U45-C187 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:194 | def _update_product_template_attribute_values | FACT | always | — | Reconciles ptav with value_ids: unlink removed values, reactivate archived, create missing with price_extra = default_extra_price (L206-253); then creates variants (L254-255). | N-U45-187 |
| VDR-U45-C188 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:245 | default_extra_price | FACT | always | — | New per-product value takes the attribute value's default extra price. | N-U45-188 |
| VDR-U45-C189 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:260 | def _is_configurable | FACT | always | — | Configurable when 2+ values, multi display, or custom value. | N-U45-189 |
| VDR-U45-C190 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:50 | def _onchange_attribute_id | FACT | form edit | — | For no_variant attribute all values are prefilled; otherwise values are filtered to the attribute (L51-58). | N-U45-190 |
| VDR-U45-C191 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:66 | _attribute_value_unique | FACT | always | — | Unique per template, line and value (L66-69). | N-U45-191 |
| VDR-U45-C192 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:72 | def _check_valid_values | FACT | always | — | Active ptav's value must be in the line's value_ids (L71-81). | N-U45-192 |
| VDR-U45-C193 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:85 | ptav_product_variant_ids | FACT | always | — | create and write raise UserError if ptav_product_variant_ids is in vals (L83-116). | N-U45-193 |
| VDR-U45-C194 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:91 | def write | FACT | always | — | write blocks changing the value or product (L97-112) and recreates variants when exclusions change (L114-115). | N-U45-194 |
| VDR-U45-C195 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:118 | def unlink | FACT | always | — | unlink removes single-value lines from variants, deletes variants via _unlink_or_archive, and deletes each ptav in a savepoint falling back to ptav_active=False (L131-149). | N-U45-195 |
| VDR-U45-C196 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:24 | ptav_active | FACT | always | — | ptav_active flag marks archived values. | N-U45-196 |
| VDR-U45-C197 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:36 | price_extra | FACT | always | — | price_extra per product value (default from attribute value). | N-U45-197 |
| VDR-U45-C198 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:97 | def write | FACT | always | — | Cannot change an attribute value's attribute if used on products (L98-106); sequence change invalidates caches (L108-114). | N-U45-198 |
| VDR-U45-C199 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:128 | _unlink_except_used_on_product | FACT | always | — | Cannot delete a value used on products (L117-130). | N-U45-199 |
| VDR-U45-C200 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:81 | def _compute_default_extra_price_changed | FACT | always | — | Reads ptav in sudo with company domain (L83) to flag per-product prices differing from default. | N-U45-200 |
| VDR-U45-C201 | FUNCTION MAPPING REQUIRED | product/wizard/update_product_attribute_value.py:67 | def _update_extra_price_on_existing_products | FACT | wizard run | — | Overwrites price_extra with default_extra_price on existing per-product values (L67-73). | N-U45-201 |
| VDR-U45-C202 | FUNCTION MAPPING REQUIRED | product/wizard/update_product_attribute_value.py:59 | def _add_value_to_existing_attribute_lines | FACT | wizard run | — | Adds the new value to existing lines of other templates with a company filter (L59-65). | N-U45-202 |
| VDR-U45-C203 | FUNCTION MAPPING REQUIRED | product/wizard/update_product_attribute_value.py:52 | def action_confirm | FACT | wizard run | — | Confirm applies the chosen mode: add the value to existing products, or update the extra price on existing products (modes L13-18). | N-U45-203 |
| VDR-U45-C204 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:36 | access_update_product_attribute_value_manager | OBSERVATION | DB dump | — | Wizard ACL for product manager group (1,1,1,0); dump shows Create group 1110 and Administrator 1110 on the wizard model. | N-U45-204 |
| VDR-U45-C205 | FUNCTION MAPPING REQUIRED | product_matrix/models/product_template.py:11 | def _get_template_matrix | FACT | product_matrix installed | — | Builds grid using valid attribute lines; header from first line's active values; cartesian product of other lines fills rows (L16-34). | N-U45-205 |
| VDR-U45-C206 | FUNCTION MAPPING REQUIRED | product_matrix/models/product_template.py:48 | is_possible_combination | FACT | product_matrix installed | — | Each cell carries sorted ptav ids, qty 0 and is_possible_combination from _is_combination_possible (L46-54). | N-U45-206 |
| VDR-U45-C207 | FUNCTION MAPPING REQUIRED | product_matrix/models/product_template.py:66 | def _grid_header_cell | FACT | product_matrix installed | — | Header name joins values with ' • ' (L78); extra price is the sum of price_extra converted to target currency at today's date, only if display_extra (L80-84). | N-U45-207 |
| VDR-U45-C208 | FUNCTION MAPPING REQUIRED | product_matrix/data/res_groups.xml:5 | group_product_variant | OBSERVATION | DB dump | — | base.group_user implies product.group_product_variant; one implication row in dump. | N-U45-208 |
| VDR-U45-C209 | FUNCTION MAPPING REQUIRED | product_matrix/views/matrix_templates.xml:4 | get_report_matrixes | FACT | product_matrix installed | — | Report template iterates order.get_report_matrixes() and renders the table (L4-35). | N-U45-209 |
| VDR-U45-C210 | FUNCTION MAPPING REQUIRED | product_matrix/views/matrix_templates.xml:42 | catalog price | FACT | product_matrix installed | — | Extra price shown on the report is the catalog price, not pricelist price (comment L41-49). | N-U45-210 |
| VDR-U45-C211 | FUNCTION MAPPING REQUIRED | product_matrix/static/src/js/product_matrix_dialog.js:66 | _onConfirm | FACT | product_matrix installed | — | Only inputs whose value differs from original are sent as changes; quantity parseFloat with no client validation (L66-90). | N-U45-211 |
| VDR-U45-C212 | FUNCTION MAPPING REQUIRED | product_matrix/static/src/js/matrix_configurator_hook.js:23 | grid_product_tmpl_id | FACT | product_matrix installed | — | Opening sets grid_product_tmpl_id on the root record to fetch the grid; non-edit mode deletes the placeholder line (L22-48). | N-U45-212 |
| VDR-U45-C213 | FUNCTION MAPPING REQUIRED | product_matrix/__manifest__.py:12 | section_and_note | FACT | always | — | depends account for the section_and_note widget; the server-side grid consumers are other modules. | N-U45-213 |
| VDR-U45-C214 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:138 | _unlink_or_archive | UNKNOWN | always | RT | Behaviour of variant deletion versus archive when referenced by stock or orders depends on other installed modules and was not traced. | N-U45-214 |
| VDR-U45-C215 | FUNCTION MAPPING REQUIRED | product/wizard/product_label_layout.py:37 | def _prepare_report_data | FACT | always | — | Requires positive quantity (L38-39); template ids take precedence over product ids (L52-59); raises when no products (L59). | N-U45-215 |
| VDR-U45-C216 | FUNCTION MAPPING REQUIRED | product/wizard/product_label_layout.py:70 | def process | FACT | always | — | UserError if no report selected; builds report action with data (L73-75). | N-U45-216 |
| VDR-U45-C217 | FUNCTION MAPPING REQUIRED | product/report/product_label_report.py:10 | def _prepare_data | FACT | always | — | active_model comes from the data dict (L15-18); UserError for unknown model (L31); returns {} if no layout wizard (L33-34). | N-U45-217 |
| VDR-U45-C218 | FUNCTION MAPPING REQUIRED | product/report/product_label_report.py:46 | custom_barcodes | FACT | always | — | Custom barcodes per product handled (L46-50); search runs under user rules ordered by name desc (L40). | N-U45-218 |
| VDR-U45-C219 | FUNCTION MAPPING REQUIRED | product/report/product_pricelist_report.py:13 | @api.readonly | FACT | always | — | get_html is readonly model method (L13-17). | N-U45-219 |
| VDR-U45-C220 | FUNCTION MAPPING REQUIRED | product/report/product_pricelist_report.py:19 | def _get_report_data | FACT | always | — | Quantities default [1] (L20); falls back to first pricelist (L23-25); active_model and active_ids come from client data (L27-32). | N-U45-220 |
| VDR-U45-C221 | FUNCTION MAPPING REQUIRED | product/report/product_pricelist_report.py:58 | product_variant_count | FACT | always | — | Includes variant rows when variant count > 1 (L58-62). | N-U45-221 |
| VDR-U45-C222 | FUNCTION MAPPING REQUIRED | product/controllers/pricelist_report.py:15 | json.loads(report_data) | FACT | auth user | — | Export route parses client JSON then recomputes data; csv or xlsx (L15-27). | N-U45-222 |
| VDR-U45-C223 | FUNCTION MAPPING REQUIRED | product/controllers/pricelist_report.py:46 | writer.writerows(rows) | FACT | csv export | — | CSV rows written without formula-prefix escaping (L41-53). | N-U45-223 |
| VDR-U45-C224 | FUNCTION MAPPING REQUIRED | product/controllers/catalog.py:8 | /product/catalog/order_lines_info | FACT | auth user | — | jsonrpc readonly route; res_model and order_id from client; calls _get_product_catalog_order_line_info with company (L29-30). | N-U45-224 |
| VDR-U45-C225 | FUNCTION MAPPING REQUIRED | product/controllers/catalog.py:34 | update_order_line_info | FACT | auth user | — | Update route calls _update_order_line_info(product_id, quantity) (L34-48). | N-U45-225 |
| VDR-U45-C226 | FUNCTION MAPPING REQUIRED | product/models/product_catalog_mixin.py:143 | def _update_order_line_info | FACT | always | — | Base returns 0 (L143-153); real behaviour is in consuming modules. | N-U45-226 |
| VDR-U45-C227 | FUNCTION MAPPING REQUIRED | product/models/product_catalog_mixin.py:90 | def _get_product_catalog_order_line_info | FACT | always | — | Builds per-product info (L90-127). | N-U45-227 |
| VDR-U45-C228 | FUNCTION MAPPING REQUIRED | product/models/product_catalog_mixin.py:136 | def _is_readonly | FACT | always | — | Base readonly hook. | N-U45-228 |
| VDR-U45-C229 | FUNCTION MAPPING REQUIRED | product/controllers/product_document.py:14 | /product/document/upload | FACT | auth user | — | POST upload; model gate is_model_valid allows only product.product and product.template (L16, L48-49). | N-U45-229 |
| VDR-U45-C230 | FUNCTION MAPPING REQUIRED | product/controllers/product_document.py:21 | has_access('write') | INFERENCE | auth user | RT | has_access('write') is called on an empty recordset (record.browse()), which probably yields true regardless of the user's write right; needs runtime test. | N-U45-230 |
| VDR-U45-C231 | FUNCTION MAPPING REQUIRED | product/controllers/product_document.py:40 | str(e) | FACT | auth user | — | Errors during create are returned to the client as str(e) (L38-40). | N-U45-231 |
| VDR-U45-C232 | FUNCTION MAPPING REQUIRED | product/controllers/product_document.py:44 | get_additional_create_params | FACT | always | — | Hook methods for other modules (L43-49). | N-U45-232 |
| VDR-U45-C233 | FUNCTION MAPPING REQUIRED | product_email_template/models/product.py:13 | email_template_id | FACT | product_email_template installed | — | Adds email_template_id Many2one to mail.template on product.template. | N-U45-233 |
| VDR-U45-C234 | FUNCTION MAPPING REQUIRED | product_email_template/models/account_move.py:9 | def invoice_validate_send_email | FACT | product_email_template installed | — | If env.su switches to SUPERUSER_ID (L10-12); only out_invoice (L13); per invoice line with a template posts message_post_with_source (L15-22). | N-U45-234 |
| VDR-U45-C235 | FUNCTION MAPPING REQUIRED | product_email_template/models/account_move.py:25 | def _post | FACT | product_email_template installed | — | _post override calls the mail on posted moves (L25-29), every post including re-posts; no de-duplication, one message per line. | N-U45-235 |
| VDR-U45-C236 | FUNCTION MAPPING REQUIRED | product_email_template/models/account_move.py:20 | mail.mail_notification_light | FACT | product_email_template installed | — | Layout mail.mail_notification_light and subtype mail.mt_comment. | N-U45-236 |
| VDR-U45-C237 | FUNCTION MAPPING REQUIRED | product_email_template/views/product_views.xml:21 | account.group_account_invoice | FACT | product_email_template installed | — | Template field in invoicing page restricted to invoice and read-only accountant groups (L8-23). | N-U45-237 |
| VDR-U45-C238 | FUNCTION MAPPING REQUIRED | product_email_template/models/account_move.py:12 | SUPERUSER_ID | INFERENCE | product_email_template installed | RT | Runs mail as superuser when already elevated (L10-12); effective recipients depend on message_post_with_source and mail settings, not traced. Needs runtime test. | N-U45-238 |
