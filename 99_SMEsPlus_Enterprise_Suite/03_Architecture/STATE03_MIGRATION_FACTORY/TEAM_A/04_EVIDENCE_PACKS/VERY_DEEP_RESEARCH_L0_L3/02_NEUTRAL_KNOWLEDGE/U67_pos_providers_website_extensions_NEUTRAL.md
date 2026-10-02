# Neutral Knowledge Pack U67 — POS Payment Providers & Website Sale Extensions
<!-- NEUTRAL KNOWLEDGE — STATE03 L0-L3 -->

**Unit:** U67  
**Produced:** 2026-10-02  

---

## [N-U67-001] Stripe POS Terminal Connection and Reader Management

WHAT: A POS Stripe payment method pairs with a physical card reader by storing the reader's serial number. When a transaction is initiated the system requests a short-lived connection token from the Stripe platform to authenticate the terminal SDK. The frontend SDK discovers available readers and connects to the one matching the stored serial number. A special sentinel value activates a simulated reader for development environments. Only one POS session may hold the SDK connection to a given reader at a time, so an existing connection to a different reader is disconnected before a new one is established.

WHY: Physical card readers require a verified device identity. The serial number pairing prevents one POS instance from accidentally commanding a reader that belongs to a different register or location.

BUSINESS RULE: POS users must hold the designated POS user security role to fetch connection tokens or initiate any terminal operation.

---

## [N-U67-002] Stripe Payment Intent and Amount Calculation

WHAT: Each card-present sale creates a payment intent through the Stripe platform using the card present payment method type with manual capture. The amount is converted from the Odoo monetary value by dividing by the currency rounding unit, producing the integer minor-unit amount required by the Stripe API. The payment intent is captured as a separate step, allowing the final captured amount to differ from the authorized amount when tips are added.

WHY: Card-present regulations in most markets require a two-step authorize-then-capture flow so that the final amount can be confirmed by the cardholder at the terminal before funds are moved.

BUSINESS RULE: The currency rounding value for the conversion step is carried in a context key, defaulting to 0.01 when not provided.

---

## [N-U67-003] Stripe Regional Payment Variants

WHAT: Payments processed in Australia with the AUD currency use a capture mode variant called manual preferred, which allows automatic capture when the terminal cannot reach the server. Payments in Canada with the CAD currency add the interac present payment method type to support Interac debit network transactions in addition to credit cards.

WHY: Regional card network requirements and regulatory constraints differ from standard Stripe Terminal behavior and must be explicitly opted into at the API level.

BUSINESS RULE: The override is applied only when both the currency name and the company country code match the target region simultaneously.

---

## [N-U67-004] Stripe Refund Processing

WHAT: A refund for a Stripe terminal transaction can be issued against either a payment intent or a charge record. The system distinguishes them by inspecting whether the stored transaction identifier begins with the letters "pi". The absolute value of the amount is sent so that negative values from credit notes are handled correctly.

WHY: Older Stripe transactions were identified by charge IDs while newer ones use payment intent IDs; both must be supported within the same refund path.

BUSINESS RULE: The refund API call is always wrapped in an exception handler so that validation errors are returned to the caller as a structured error dict rather than propagated as exceptions.

---

## [N-U67-005] Stripe Overcapture for Tips

WHAT: When a customer adds a tip after authorization the amount to be captured can exceed the originally authorized amount. The capture endpoint accepts an optional amount to capture parameter for this purpose. When no explicit amount is supplied the entire authorized amount is captured.

WHY: Tip adjustment is a standard POS hospitality requirement. Stripe Terminal supports overcapture within limits defined by the card network.

BUSINESS RULE: The overcapture amount is converted using the same currency rounding rule as the initial authorization.

---

## [N-U67-006] Stripe Terminal Serial Number Uniqueness

WHAT: Each physical Stripe terminal may be registered on at most one payment method at a time. A database-level constraint enforces this by rejecting any attempt to save a serial number that already exists on a different payment method record.

WHY: Assigning the same terminal to two payment methods would cause both methods to attempt to command the same physical device, producing conflicting instructions.

BUSINESS RULE: The constraint is evaluated only for non-empty serial number values; blank fields are exempt.

---

## [N-U67-007] Stripe Payment Provider Lookup

WHAT: The Stripe payment method locates the corresponding payment provider record by searching for a provider whose code equals the Stripe identifier, restricted to the current company. If no matching provider is found an error is raised immediately.

WHY: A single Odoo database may contain multiple companies each with their own Stripe account. The company-scoped lookup ensures that credentials from one company are never used to process transactions for another.

BUSINESS RULE: The provider lookup is always performed with elevated privileges to bypass record rules that might otherwise restrict access during a POS session.

---

## [N-U67-008] Viva.com POS Credential Storage

WHAT: A Viva.com payment method stores five configuration fields covering API credentials and terminal identity. Two fields (merchant ID and API key) are used for webhook management. Two fields (client ID and client secret) are used for the OAuth bearer token flow. One field (terminal ID) identifies the physical ECR terminal at the counter.

WHY: The Viva.com API separates administration credentials from POS runtime credentials. Webhook registration requires the merchant account pair while transaction execution requires the POS API pair.

BUSINESS RULE: All five credential fields must be populated before a payment method can be designated as a Viva.com terminal type; an error is raised otherwise.

---

## [N-U67-009] Viva.com Test Mode and Data Neutralization

WHAT: A test mode flag on the Viva.com payment method redirects all API calls to the demo subdomains of the Viva.com platform. A database neutralization script activates test mode on every existing payment method row automatically when applied, preventing any live transactions after a database copy or restore.

WHY: Production database copies used for development or testing must not be able to trigger real financial transactions. Enforcing test mode at the data layer provides a safety net even when application-level environment flags are absent.

BUSINESS RULE: The neutralization script sets the test mode flag unconditionally on all rows in the payment method table.

---

## [N-U67-010] Viva.com OAuth Bearer Token Acquisition

WHAT: The Viva.com ECR API requires a short-lived bearer token. The token is obtained by posting a client credentials grant to the Viva.com accounts endpoint using the payment method's client ID and client secret as HTTP Basic credentials. On success the token is stored on the payment method record for reuse. On failure a user-facing error message is raised.

WHY: OAuth client credentials is a machine-to-machine authentication flow that does not require user interaction. The stored token reduces round trips on subsequent calls within the same session.

BUSINESS RULE: If the token is missing or has expired the API call layer automatically re-fetches it rather than returning an error to the POS frontend.

---

## [N-U67-011] Viva.com ECR API Call Mechanism

WHAT: All Viva.com POS operations go through a single internal call method that prepends the base ECR v1 path to the endpoint fragment, attaches the current bearer token, and executes the HTTP action. If the response indicates invalid credentials the method refreshes the bearer token and retries the request once. A 200 response with an empty body is treated as a success indicator.

WHY: Centralizing the API call logic ensures that token refresh, error handling, and endpoint construction are consistent across all payment operations.

BUSINESS RULE: Any non-200 response is converted into a structured error dict containing the detail message from the Viva.com response body.

---

## [N-U67-012] Viva.com Payment Sale Request

WHAT: A sale transaction is initiated by posting to the ECR transactions:sale endpoint. The request payload is passed through from the POS frontend and includes the amount, currency, and terminal reference. Access is restricted to holders of the POS user security role.

WHY: The POS frontend constructs the transaction payload based on the order total and the selected payment method. The server-side method adds authentication and routing to the correct Viva.com endpoint.

BUSINESS RULE: Unauthorized callers receive an access error immediately before any network request is made.

---

## [N-U67-013] Viva.com Refund and Unreferenced Refund

WHAT: A refund can be processed in two ways: a referenced refund links back to the original session by including the parentSessionId, while an unreferenced refund stands alone. The system selects the endpoint automatically based on the presence of the parentSessionId field in the request data.

WHY: Viva.com separates these two flows for audit and chargeback purposes. Referenced refunds are preferred when the original transaction is available.

BUSINESS RULE: POS user role access is required for both refund variants.

---

## [N-U67-014] Viva.com Payment Cancellation

WHAT: An in-progress terminal payment session can be cancelled by sending a DELETE request to the session endpoint identified by the session ID and cash register ID. This instructs the terminal to abort the pending card interaction.

WHY: Cancellation is necessary when a customer changes their mind or a timeout occurs before the card is presented. The terminal must be explicitly released so it can accept the next transaction.

BUSINESS RULE: POS user role access is required to cancel a payment session.

---

## [N-U67-015] Viva.com Webhook Verification and Registration

WHAT: A webhook verification key is automatically retrieved from the Viva.com platform when the merchant credentials are saved. This key must be returned verbatim in the HTTP response body whenever the platform sends a verification ping to the configured webhook URL. The webhook URL embeds the company ID and the verification key as query parameters to allow routing to the correct payment method.

WHY: Viva.com requires that the merchant confirm ownership of the notification URL before activating event delivery. The platform sends a GET request and expects the key in the response.

BUSINESS RULE: Webhook key retrieval is skipped during automated testing to avoid external network calls.

---

## [N-U67-016] Viva.com Notification Processing

WHAT: When a payment notification arrives at the webhook endpoint the controller verifies the token parameter against all registered Viva.com payment methods for the company. Only EventTypeId 1796 (Transaction Payment Created) is processed. The terminal ID in the event payload is used to locate the correct payment method record, and the session ID is then retrieved and relayed to the POS channel.

WHY: A single webhook URL handles all terminals for a company, so the controller must route each notification to the specific payment method and POS session that initiated the transaction.

BUSINESS RULE: Unknown event type identifiers produce a warning log entry but do not return an error to the Viva.com platform, ensuring delivery acknowledgement is always sent.

---

## [N-U67-017] Viva.com Session ID Persistence for Refunds

WHAT: After a successful card transaction the Viva.com terminal session identifier is stored on the POS payment record. This persisted session ID is later used as the parentSessionId when initiating a referenced refund against the original transaction.

WHY: Viva.com referenced refunds require the original session identifier to link the credit back to the debit. Storing it on the payment record at the time of sale ensures it is available without querying the Viva.com platform again.

BUSINESS RULE: The session ID is stored as a character string because Viva.com session identifiers include alphanumeric characters.

---

## [N-U67-018] Viva.com HTTP Retry Policy

WHAT: HTTP sessions used for Viva.com API calls are configured with an automatic retry adapter that retries up to five times with exponential backoff using a factor of two seconds. Retries are triggered on HTTP status codes 202, 500, 502, 503, and 504. Status 202 is included because it indicates an asynchronous acceptance that may require polling.

WHY: Payment terminal APIs can experience transient failures due to network conditions or backend queue delays. Automatic retries improve reliability without requiring the POS operator to manually retry failed requests.

BUSINESS RULE: Retry behavior can be disabled by passing the should retry=False flag, which is used for polling operations that must reflect the current state rather than retry on cached responses.

---

## [N-U67-019] Viva.com Credential Completeness Validation

WHAT: A constraint fires whenever a payment method's terminal type is changed. If the terminal type is set to the Viva.com value the constraint checks that all five required credential fields are non-empty and raises an error if any is missing.

WHY: Incomplete credentials would cause every payment attempt to fail at runtime. Enforcing completeness at save time prevents the creation of a non-functional payment method.

BUSINESS RULE: The constraint applies at the model level and runs for all creation and update operations that affect the terminal type field.

---

## [N-U67-020] Event Sponsor and Exhibitor Model

WHAT: An event sponsor record represents a company or entity associated with an event for display purposes. Each sponsor belongs to a sponsorship level and carries contact information, logo, description, and a website URL. The record supports website publication and global website search. The URL pattern for an exhibitor's public page follows the structure of event slug followed by exhibitor slug.

WHY: Events need to acknowledge and promote their sponsors on the event website. Different levels of sponsorship receive different visual treatment and page space.

BUSINESS RULE: Sponsor contact fields are pre-populated from the linked partner record but can be overridden with event-specific values without changing the underlying partner.

---

## [N-U67-021] Exhibitor Type Classification

WHAT: Sponsors can be classified into three types that determine their visibility and treatment on the event website. A footer-logo-only sponsor appears only in the footer credits section. An exhibitor gets a full profile page. An online exhibitor also gets a profile page with additional live-session context for virtual events.

WHY: Large events host a mix of major exhibitors with booths and minor sponsors who only need logo visibility. The type field enables a single model to handle both scenarios.

BUSINESS RULE: Only exhibitor and online types appear in exhibitor listing pages; sponsor types are excluded from those pages at the domain filter level.

---

## [N-U67-022] Exhibitor Opening Hours

WHAT: Each exhibitor can define opening hours expressed as start and end times within the event timezone. A computed field determines in real time whether the exhibitor is currently within their opening window. The computation accounts for event start and end boundaries, preventing the exhibitor from appearing "open" before the event begins or after it ends.

WHY: Virtual exhibitors hosting live video calls need to signal to attendees whether staff are currently available at the virtual booth.

BUSINESS RULE: If either the start or end hour is absent the exhibitor is considered always open during the event's active period.

---

## [N-U67-023] Sponsor Level Ribbon Style

WHAT: Sponsor level records define a visual ribbon style that is overlaid on the sponsor logo or card on the event website. Available styles are no ribbon, Gold, Silver, or Bronze. The ribbon visually communicates the relative investment tier of each sponsor.

WHY: Event sponsors expect visible recognition commensurate with their sponsorship tier. Automated ribbon display removes the need for manual visual customization per sponsor.

BUSINESS RULE: The ribbon style is stored on the sponsor type record and applies uniformly to all sponsors at that level.

---

## [N-U67-024] Exhibitor Search and Listing Domain

WHAT: The exhibitor listing controller builds a base search domain that includes only exhibitor and online exhibitor types. When the visitor is not a member of the event registration desk group an additional published filter is added. A global website search integration also uses this same domain restriction so that full-text search results never surface unpublished exhibitor records to public visitors.

WHY: Draft or unpublished exhibitor profiles must not appear in public listings or search results until the event organizer explicitly publishes them.

BUSINESS RULE: Staff members with the registration desk role can see unpublished exhibitors to allow preview and review before publication.

---

## [N-U67-025] Exhibitor Menu Integration

WHAT: The event website menu system is extended with an exhibitor menu type. This allows the exhibitors page to appear as a primary navigation item in the event's website menu alongside other sections such as talks and agenda.

WHY: Event attendees need easy navigation to the exhibitors listing. The menu type extension integrates exhibitors into the existing event website navigation framework.

BUSINESS RULE: Deleting the exhibitor menu type cascades to remove the associated menu items, preventing orphaned navigation links.

---

## [N-U67-026] Booth Category Sponsor Configuration

WHAT: Each booth category can be configured to automatically create a sponsor record when someone books a booth of that category. The configuration includes a sponsorship level and an exhibitor type that are applied to the automatically created sponsor. When the auto-create flag is enabled and no sponsorship level is set, the system defaults to the highest-ranked available level.

WHY: Booth rental is a common mechanism for companies to participate as exhibitors. Automating the sponsor record creation eliminates a manual administrative step for event staff.

BUSINESS RULE: The exhibitor type choices available on the booth category are drawn from the same selection list as the sponsor model to ensure consistency.

---

## [N-U67-027] Booth Auto-Sponsor Creation

WHAT: When a booth booking is confirmed, if the booth category has the auto-sponsor flag enabled and a partner is associated with the booking, the system searches for an existing sponsor record that matches the partner, sponsorship level, exhibitor type, and event. If one exists it is linked to the booth; otherwise a new sponsor record is created using the booth registration data.

WHY: Multiple booths booked by the same company for the same event should share a single sponsor profile rather than creating duplicate exhibitor pages.

BUSINESS RULE: The sponsor creation step runs as part of the post-confirmation hook, ensuring that the sponsor exists only after the booth booking is fully confirmed.

---

## [N-U67-028] Booth Registration Sponsor Fields

WHAT: The booth registration data model captures optional sponsor profile information (name, email, phone, slogan, description, and logo image) that is submitted by the registrant during online booth booking. These fields are transferred to the booth record on confirmation and subsequently used to populate the automatically created sponsor profile. The registration controller also maps sponsor contact fields to the generic contact fields used for partner record lookup when the dedicated contact fields are absent.

WHY: Online booth registrants need to provide exhibitor profile information at the time of booking rather than requiring a separate data entry step by event staff.

BUSINESS RULE: All six sponsor profile fields are included in the booth confirmation field list, making them available for transfer to the booth and sponsor records.

---

## [N-U67-029] Event Track Model Structure

WHAT: An event track is a scheduled presentation, session, or content item within an event. Tracks are ordered by priority descending and then by date. The model integrates with website SEO metadata, the published content mixin, and the website searchable content framework. Two website navigation menu types (track listing and proposal submission) are registered as part of this module.

WHY: Events with a multi-session agenda need structured track records to power the agenda display, session detail pages, and speaker directories on the event website.

BUSINESS RULE: Each track must belong to a stage; stages control both Kanban workflow visibility and agenda display eligibility.

---

## [N-U67-030] Track Priority System

WHAT: Each track carries a priority level expressed as a four-value selection from Low to Highest, with Medium as the default. Priority is required and affects the sort order of tracks in listings and agenda views, with higher-priority tracks appearing first.

WHY: Keynote sessions and featured talks should appear prominently in agenda listings even when scheduled later in the day.

BUSINESS RULE: Priority is a required field and cannot be left empty.

---

## [N-U67-031] Track Time State Computation

WHAT: Five boolean state fields characterize a track's position in time relative to the current moment: live (currently running), soon (starting within 30 minutes), today (occurring on the current calendar date), upcoming (scheduled in the future), and done (ended). All computations use UTC-localized datetime values with microseconds stripped to produce clean second-granularity deltas. Numeric fields also track how many seconds remain before start or how many seconds have elapsed since start.

WHY: The event website and attendee notifications need to dynamically reflect the current state of each track without polling a backend service.

BUSINESS RULE: All time boundaries use UTC internally; timezone display conversion is handled by the frontend template layer.

---

## [N-U67-032] Track Visitor Wishlist and Reminder Management

WHAT: A junction model links each track to each website visitor who has interacted with it. Two Boolean flags on the junction record capture whether the visitor has wishlisted the track for a reminder and whether they have explicitly opted out of the reminder for a track that is wishlisted by default. A convenience flag on the track itself marks it as automatically wishlisted for all event attendees. Aggregated counts of wishlisted visitors are computed from the junction records.

WHY: Attendees at large events need a personal agenda of tracks they plan to attend. The wishlist drives pre-session reminder notifications.

BUSINESS RULE: Key tracks set as wishlisted by default can have their reminder suppressed for individual visitors via the blacklisted flag but cannot be un-favorited from the UI.

---

## [N-U67-033] Track Call-to-Action Magic Button

WHAT: A track can carry a configurable call-to-action button that appears over the video player during the live session. The button has a title, a target URL, and a delay in seconds after the session starts before it becomes visible. Corresponding computed time fields indicate whether the button is currently active.

WHY: Speakers often want to direct viewers to a registration form, survey, or external resource at a specific point during their presentation.

BUSINESS RULE: The button only appears when the website cta flag is enabled on the track and the delay period has elapsed from the track start time.

---

## [N-U67-034] Track Agenda Domain and Visibility

WHAT: The track listing controller uses a domain that selects tracks either published or belonging to stages flagged as visible in the agenda. This allows unpublished draft tracks to appear in the agenda skeleton while remaining hidden from the public detail pages. For non-staff visitors an additional published filter is applied on top.

WHY: Event organizers publish the agenda structure before all track detail pages are finalized. Showing the time slot with a placeholder title is better than hiding the slot entirely.

BUSINESS RULE: Staff with the registration desk role see all tracks in their agenda state regardless of publication status.

---

## [N-U67-035] YouTube Live Streaming Integration

WHAT: A track can be linked to a YouTube video by storing the video URL. The system automatically extracts the 11-character video ID from the URL using a regular expression. The replay flag indicates that the video is a post-event recording, which suppresses live-specific UI elements such as the chat pane and direct streaming indicators. The module summary describes support for streaming, participation, and YouTube integration.

WHY: Many online and hybrid events deliver session content through YouTube Live. Linking a YouTube video to a track bridges the Odoo event management data with the streaming platform.

BUSINESS RULE: The video ID extraction fails silently when the URL does not yield a valid 11-character match; the ID field is set to False in that case.

---

## [N-U67-036] YouTube Thumbnail Derivation

WHAT: When a track has a YouTube video ID but no locally stored website image, the track's image URL is derived from the YouTube thumbnail service using the maxresdefault quality level. This allows the track listing and detail pages to display a thumbnail without requiring the event organizer to upload a separate image.

WHY: YouTube generates high-resolution thumbnails automatically for all published videos. Reusing them reduces administrative effort.

BUSINESS RULE: A locally uploaded website image takes priority over the derived YouTube thumbnail.

---

## [N-U67-037] YouTube Chat Availability Logic

WHAT: The YouTube chat embed availability is computed from three conditions: the track must have a YouTube video URL, the replay flag must be off, and the track must currently be in the soon or live state. All three conditions must be true simultaneously for chat to be considered available.

WHY: YouTube chat is only functional when a live broadcast is running or imminent. Replays and scheduled future tracks do not support live chat interaction.

BUSINESS RULE: The availability is recomputed whenever the video URL, replay flag, or time state fields change.

---

## [N-U67-038] Track Next-Suggestion API

WHAT: A JSONRPC endpoint allows the frontend to retrieve one suggested next track to display after the current track ends. The suggestion is restricted to tracks from the same event that have a YouTube video URL set. The response includes the current track's name and thumbnail and the suggested track's name, speaker, and URL.

WHY: Keeping viewers engaged after one session ends by surfacing a relevant next session reduces drop-off and increases event content consumption.

BUSINESS RULE: The endpoint is publicly accessible without authentication, matching the public accessibility of the track detail pages.

---

## [N-U67-039] Widescreen Layout and Mobile Chat Detection

WHAT: The track detail page switches to a widescreen video layout when the track has a YouTube URL and is in a playable state (replay, soon, live, or done). On mobile devices (Android, iPad, iPhone detected via User-Agent) a flag suppresses the YouTube chat embed to match the YouTube platform's own restriction.

WHY: Widescreen layout dedicates more screen real estate to the video player. Hiding the chat embed on mobile reflects YouTube's restriction that chat cannot be embedded on mobile browsers.

BUSINESS RULE: The mobile detection is based on a simple User-Agent substring check; edge cases where the check misidentifies the device type are acceptable given that YouTube's own behavior would suppress the chat regardless.

---

## [N-U67-040] Quiz Integration in Live Tracks

WHAT: A bridge module connects the live track and quiz modules. When both are installed the next-track suggestion payload is extended with a flag indicating whether the current track has an associated quiz that the viewer has not yet completed. The module is installed automatically when its two parent modules are both present.

WHY: Quizzes embedded in live sessions can be surfaced at the point when the session ends and a next-track suggestion is shown, encouraging viewers to complete the quiz before moving on.

BUSINESS RULE: The quiz flag is only true when the track has a quiz record linked and the viewer has not yet completed it; a completed quiz suppresses the flag.

---

## [N-U67-041] Wishlist Product Model and Scoping

WHAT: A product wishlist record links a specific product variant to a website and optionally to a partner. The record captures the pricelist and price at the time the item was added. Each wishlist is scoped to a website, and deleting the website cascades to remove all its wishlist records. A unique constraint prevents the same product variant from appearing twice for the same partner.

WHY: Price-at-add-time capture lets the wishlist page show visitors whether the price has changed since they saved the item, supporting a comparison-shopping use case.

BUSINESS RULE: The website id field is required; guest session wishlists use the website but have no partner id until the guest logs in.

---

## [N-U67-042] Wishlist Guest and Authenticated Access

WHAT: Guest visitors' wishlist items are tracked by storing record IDs in the browser session. Authenticated users' wishlists are stored as database records linked to their partner. The current() method unifies both paths, returning wishlist items filtered to published and cart-eligible products. A separate endpoint returns only the list of product IDs for lightweight frontend state checks.

WHY: Allowing guests to use the wishlist without registering reduces friction and increases conversion. Merging the session wishlist into the partner account on login preserves items across sessions.

BUSINESS RULE: Items for unpublished products or products that cannot be added to the cart are filtered out of the current wishlist regardless of how they were added.

---

## [N-U67-043] Adding Items to the Wishlist

WHAT: The add-to-wishlist route is publicly accessible. It records the current pricelist, currency, website, and product price at the moment of addition. For guests the new record ID is appended to the session's wishlist ID list. For authenticated users the partner ID is included in the record.

WHY: Capturing the price at add-time enables the wishlist page to surface a price-drop indicator if the product's price has decreased since the item was saved.

BUSINESS RULE: The route accepts only a single product ID per call; batch additions require multiple calls.

---

## [N-U67-044] Wishlist Session Migration on Login

WHAT: When a user successfully authenticates, any wishlist items stored in the browser session are checked against the user's existing partner wishlist. Items whose product already exists in the partner wishlist are deleted from the session as duplicates. The remaining session items are reassigned to the partner account. The session key is then cleared.

WHY: A shopper who added items before logging in should find those items in their account wishlist after login, not lose them or see duplicates.

BUSINESS RULE: The migration runs synchronously as part of the credential verification flow so that the wishlist is merged before the user's first authenticated page load.

---

## [N-U67-045] Wishlist Garbage Collection

WHAT: A scheduled autovacuum method periodically deletes wishlist records that have no partner (guest records) and were created more than five weeks ago. This prevents long-lived browser sessions or abandoned shopping sessions from accumulating stale records indefinitely.

WHY: Guest wishlist records are created without authentication and may never be claimed by a logged-in user. Without periodic cleanup these records would accumulate without bound.

BUSINESS RULE: The cleanup window is five weeks by default but can be overridden by passing a different week count through keyword arguments.

---

## [N-U67-046] Wishlist Item Removal

WHAT: The remove-from-wishlist route accepts a wishlist record ID. For guest users it verifies that the ID appears in the current session's list before deleting, preventing removal of items that belong to other sessions. For authenticated users the record is deleted directly using the user's access rights.

WHY: Access control on removal prevents a guest session from deleting wishlist items that were saved by a different visitor or a logged-in user.

BUSINESS RULE: The route is publicly accessible to support guest wishlist management without requiring login.

---

## [N-U67-047] Wishlist Transfer Hook on Login

WHAT: The session wishlist migration is triggered as a side effect of the standard credential check method rather than as a separate controller action. This ensures that the migration occurs for every authentication path, including direct API calls, without requiring the authentication controller to be modified.

WHY: Hooking into credential verification rather than the login controller covers all authentication entry points uniformly.

BUSINESS RULE: The migration only runs when the browser session contains a wishlist ids key, making it a no-op for users who have no session wishlist.

---

## [N-U67-048] Wishlist Stock Notification

WHAT: A bridge module between the wishlist and stock modules adds a stock notification flag to each wishlist item. The flag reflects whether the partner has registered to receive an email alert when the product comes back in stock. The module is installed automatically when both the wishlist and stock modules are present.

WHY: Allowing customers to request a back-in-stock notification from the wishlist page reduces the chance of losing a sale to a stockout by re-engaging the customer when inventory is replenished.

BUSINESS RULE: The notification flag is computed from the product's stock notification partner list rather than stored independently, keeping a single source of truth.

---

## [N-U67-049] Wishlist Visibility in Variant Combination Info

WHAT: When the combination info endpoint is called from a context where wishlist status is needed, the is in wishlist field is included in the response for the specific product variant. A context flag gates this injection to avoid the wishlist query on every standard product page load. The variant controller sets this flag before delegating to the parent method.

WHY: The product listing and detail pages need to know whether each variant is already wishlisted to render the heart icon in the correct state without a separate API call.

BUSINESS RULE: The wishlist check is performed only for product variants, not for product templates, because the wishlist is linked to specific variants.

---

## [N-U67-050] Click and Collect Wishlist Bridge

WHAT: A bridge module between the click-and-collect and wishlist modules allows visitors to add a product to their wishlist when that product is not available at their selected pickup location. This provides an alternative to the dead-end "out of stock at this location" message.

WHY: A product unavailable for collection at a specific location may be purchasable for delivery or available at the location in future. The wishlist bridge preserves the customer's intent until the product becomes available.

BUSINESS RULE: The module is installed automatically when both the click-and-collect and wishlist modules are present.

---

## [N-U67-051] Product Attribute Category for Comparison

WHAT: A new model stores named attribute categories with a configurable sort order. Product attributes can be assigned to a category to group related attributes together in the eCommerce comparison table. Uncategorized attributes are placed in a default unnamed category at the end of the comparison display.

WHY: A comparison table with dozens of attributes is difficult to scan. Grouping attributes by category (such as dimensions, connectivity, or performance) helps shoppers evaluate products along logical dimensions.

BUSINESS RULE: The category field on a product attribute is optional; attributes without a category are handled gracefully rather than excluded from comparison.

---

## [N-U67-052] Comparison Grouped Attribute Display

WHAT: The comparison display logic builds a nested ordered dictionary where the outer level is attribute category and the inner level is individual attribute. For each attribute the values held by each compared product are listed. Products that use a no-variant configuration (where the attribute exists but no specific value is selected) show all possible values. The uncategorized group is positioned at the end of the outer dictionary.

WHY: Shoppers need to see differences between products side by side. Grouping by category reduces visual scanning effort compared to a flat list of all attributes.

BUSINESS RULE: Attributes are sorted following their default model order; categories are also sorted by their sequence and ID fields.

---

## [N-U67-053] Comparison Route and Product Selection

WHAT: The comparison page is accessed via a route that accepts a comma-separated list of product variant IDs as a query parameter. The controller parses and validates the IDs before searching for the corresponding records. If no valid IDs are provided the visitor is redirected to the main shop page.

WHY: The comma-separated ID approach allows bookmarking and sharing a specific comparison set via URL.

BUSINESS RULE: The product search applies standard read access rules, so only products the visitor is permitted to see are included in the comparison.

---

## [N-U67-054] Comparison Product Data Endpoint

WHAT: A JSONRPC endpoint returns display data for a list of product variant IDs for the comparison table. The response includes the display name, website URL, main image URL, current price, and a strikethrough price when a discount or compare list price exists. The strikethrough price uses the compare list price when it is higher than the current price, falling back to the list price for pricelist discounts.

WHY: The comparison table requires a consistent data shape for all products to render a properly aligned side-by-side layout. Separating this into a JSONRPC call allows the table to load asynchronously and update dynamically when products are added or removed.

BUSINESS RULE: A strikethrough price is shown only when it is strictly greater than the current selling price.

---

## [N-U67-055] Product Specs Table Attribute Display

WHAT: On individual product pages, attribute lines are grouped by their category and rendered as a specifications table. A filtered variant of this grouping excludes attribute lines where the single available value is marked as a custom input value, because custom values do not represent fixed technical specifications.

WHY: The specifications table communicates fixed technical attributes of a product. Custom-input attributes (such as engraving text) are not fixed specifications and should not appear in the table.

BUSINESS RULE: The category grouping uses the same OrderedDict structure as the comparison display, ensuring consistent category ordering between the product page and the comparison page.

---

## [N-U67-056] Comparison and Wishlist Bridge

WHAT: A bridge module links the product comparison and wishlist features to allow a visitor to initiate a comparison from the wishlist page by selecting products from their saved list. The module is installed automatically when both parent modules are present.

WHY: A visitor who has saved several products to compare may want to access the comparison view directly from the wishlist page rather than navigating back to the shop.

BUSINESS RULE: The bridge adds only frontend template overrides; no new models or database columns are introduced.

---

## [N-U67-057] Newsletter Mailing List Association on Website

WHAT: The website configuration model gains a field that links the site to a specific mailing list. This list is used as the subscription target for all newsletter sign-up actions on that website, including checkout opt-in forms.

WHY: Different websites (for example a B2B site and a B2C site) may want to subscribe visitors to different mailing lists. The website-level field scopes subscriptions correctly.

BUSINESS RULE: The newsletter list is shared across all newsletter sign-up entry points on the website that use the standard website newsletter integration.

---

## [N-U67-058] Checkout Newsletter Subscription

WHAT: During the checkout address step a newsletter opt-in checkbox can appear on the form. When the checkbox is checked and a valid email address has been entered, the system subscribes the email address to the website's configured mailing list as part of processing the extra form data submitted with the address.

WHY: The checkout is a high-intent interaction point where customers are most likely to provide accurate contact information. Capturing newsletter consent here maximizes the quality of the subscription list.

BUSINESS RULE: The subscription is only triggered when both conditions are met simultaneously: the newsletter field is present and truthy, and a non-empty email address was provided.

---

## [N-U67-059] Newsletter Block Enable Setting

WHAT: A configuration setting controls whether the newsletter sign-up block appears on the website checkout. The setting is computed from the active state of the newsletter view snippet. Saving the setting activates or deactivates the view accordingly. The computed field re-reads the view state whenever the active website changes in the settings form.

WHY: Enabling or disabling the newsletter block without code changes supports merchants who want to turn the feature on and off without developer involvement.

BUSINESS RULE: The setting is per-website; each website can have the feature independently enabled or disabled.

---

## [N-U67-060] SMS Phone Number Mailing List Subscription

WHAT: An extension to the website newsletter controller adds mobile phone number support alongside the existing email subscription flow. When the subscription type is identified as mobile, the controller looks up the phone number from the authenticated user's partner record or from a session key. A separate method maps the mobile subscription type to the correct contact field name used for storing the phone number on the mailing contact.

WHY: SMS marketing lists require a mobile phone number rather than an email address. The extension reuses the existing newsletter infrastructure while adding the mobile-specific resolution logic.

BUSINESS RULE: The module is installed automatically when both the website mass mailing and SMS mass mailing modules are present. A new website builder template block allows visitors to subscribe with their phone number.
